# AI 面试助手

基于阿里云百炼通义千问 API 的交互式 AI 面试助手。

## 功能
- 随机抽题
- 用户输入回答
- 调用通义千问 API 进行评分和反馈
- 无 API Key 时自动降级为模拟反馈

## 技术栈
Python、Requests、阿里云百炼 API、Prompt 工程

## 运行
```bash
pip install -r requirements.txt
export DASHSCOPE_API_KEY=你的key
python main.py