# AI 面试助手

基于阿里云百炼通义千问 API 的交互式 AI 面试助手。

## 项目简介

用户随机抽取面试题，输入自己的回答，程序调用通义千问 API，从**准确性、完整性、表达清晰度**三个维度评分，并给出改进建议和参考答案。

支持无 API Key 时自动降级为模拟反馈，保证程序在任何环境下都能运行。

## 功能

- 随机抽题（Python、机器学习、大模型、项目、测试等方向）
- 用户输入回答
- 调用通义千问 API 进行评分和反馈
- 结构化 Prompt 模板，输出固定格式
- 异常处理与降级机制，无 Key 也能跑
- 环境变量管理 API Key，避免泄露

## 技术栈

- Python
- Requests
- 阿里云百炼通义千问 API
- Prompt 工程
- 数据标注与效果迭代

## 项目结构
ai-interviewer/
├── main.py # 主程序，交互逻辑与 API 调用
├── prompts.py # Prompt 模板
├── questions.json # 面试题库
├── requirements.txt # 依赖
├── .env.template # 环境变量模板
├── .gitignore # Git 忽略规则
├── LICENSE # MIT 许可证
├── README.md # 项目说明
├── screenshot.png # 运行截图
└── tests/
└── test_main.py # 单元测试

## 运行方式

### 1. 安装依赖

```bash
pip install -r requirements.txt