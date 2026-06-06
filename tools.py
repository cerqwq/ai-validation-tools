"""
AI Validation Tools - AI验证工具
支持数据验证、输入验证、Schema验证
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIValidationTools:
    """
    AI验证工具
    支持：数据、输入、Schema
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_validation_system(self, application: str) -> Dict:
        """设计验证系统"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{application}设计验证系统：

请返回JSON格式：
{{
    "validation_layers": ["验证层"],
    "rules": [
        {{"field": "字段", "type": "类型", "constraints": ["约束"]}}
    ],
    "error_messages": "错误消息策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"validation": content}

    def generate_pydantic_models(self, data_description: str) -> str:
        """生成Pydantic模型"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下描述生成Pydantic模型：

{data_description}

要求：
1. 字段验证
2. 自定义验证器
3. 错误消息"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_json_schema(self, data_model: Dict) -> str:
        """生成JSON Schema"""
        if not self.client:
            return "LLM客户端未配置"

        model_text = json.dumps(data_model, ensure_ascii=False)

        prompt = f"""请根据以下数据模型生成JSON Schema：

{model_text}

要求：
1. 完整的Schema定义
2. 验证规则
3. 错误消息"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def generate_form_validation(self, form_fields: List[Dict], framework: str = "react") -> str:
        """生成表单验证"""
        if not self.client:
            return "LLM客户端未配置"

        fields_text = json.dumps(form_fields, ensure_ascii=False)

        prompt = f"""请生成{framework}表单验证：

字段：{fields_text}

要求：
1. 实时验证
2. 错误提示
3. 提交验证"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_sanitization_rules(self, input_types: List[str]) -> Dict:
        """生成清理规则"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        types_text = ", ".join(input_types)

        prompt = f"""请生成输入清理规则：

输入类型：{types_text}

请返回JSON格式：
{{
    "rules": [
        {{"type": "类型", "sanitization": "清理规则"}}
    ],
    "security": ["安全措施"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"sanitization": content}

    def design_api_validation(self, endpoints: List[Dict]) -> Dict:
        """设计API验证"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        endpoints_text = json.dumps(endpoints, ensure_ascii=False)

        prompt = f"""请设计API验证方案：

端点：{endpoints_text}

请返回JSON格式：
{{
    "request_validation": "请求验证",
    "response_validation": "响应验证",
    "error_format": "错误格式"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"api_validation": content}


def create_tools(**kwargs) -> AIValidationTools:
    """创建验证工具"""
    return AIValidationTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Validation Tools")
    print()

    # 测试
    validation = tools.design_validation_system("用户注册")
    print(json.dumps(validation, ensure_ascii=False, indent=2))
