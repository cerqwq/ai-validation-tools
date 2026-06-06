# ✅ AI Validation Tools

AI验证工具，支持数据验证、输入验证、Schema验证。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 验证系统设计
- 📝 Pydantic模型生成
- 📋 JSON Schema生成
- 📱 表单验证生成
- 🧹 输入清理规则
- 🔌 API验证设计

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_validation_tools import create_tools

tools = create_tools()

# 验证系统设计
validation = tools.design_validation_system("用户注册")

# Pydantic模型
pydantic = tools.generate_pydantic_models("用户信息：姓名、邮箱、年龄")

# JSON Schema
schema = tools.generate_json_schema(data_model)

# 表单验证
form = tools.generate_form_validation(form_fields, "react")

# 输入清理
sanitization = tools.generate_sanitization_rules(["邮箱", "电话", "URL"])

# API验证
api = tools.design_api_validation(endpoints)
```

## 📁 项目结构

```
ai-validation-tools/
├── tools.py       # 验证工具核心
└── README.md
```

## 📄 许可证

MIT License