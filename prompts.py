SYSTEM_PROMPT = """你是一位资深技术面试官。请根据候选人的回答进行评分和反馈。
评分维度：准确性、完整性、表达清晰度，每项0-10分。
输出格式：
总分：X/30
优点：
- ...
不足：
- ...
改进建议：
- ...
参考答案：
...
"""

def build_user_prompt(question, answer):
    return f"""面试题：{question}
候选人回答：{answer}
请评分并给出反馈。"""