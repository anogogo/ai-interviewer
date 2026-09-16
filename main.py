import os
from dotenv import load_dotenv
load_dotenv()
import json
import random
import requests
from prompts import SYSTEM_PROMPT, build_user_prompt

API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
MODEL = "qwen-plus"

def load_questions(path="questions.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def mock_feedback(user_prompt):
    return """总分：24/30
优点：
- 回答覆盖了主要概念，表达较清晰。
不足：
- 部分细节不够深入，缺少具体例子。
改进建议：
- 结合项目实际说明，补充具体场景。
参考答案：
- 请根据题目自行整理。"""

def call_qwen(system_prompt, user_prompt, timeout=30):
    if not API_KEY:
        return mock_feedback(user_prompt)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7
    }

    try:
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"调用大模型失败：{e}\n\n（已切换到模拟反馈）\n" + mock_feedback(user_prompt)
    except (KeyError, IndexError) as e:
        return f"解析响应失败：{e}\n\n（已切换到模拟反馈）\n" + mock_feedback(user_prompt)

def main():
    questions = load_questions()
    print("=== AI 面试助手（输入 q 退出）===")
    while True:
        item = random.choice(questions)
        print(f"\n[{item['category']}] {item['question']}")
        answer = input("你的回答：").strip()

        if answer.lower() == "q":
            break
        if not answer:
            print("回答不能为空。")
            continue

        user_prompt = build_user_prompt(item["question"], answer)
        feedback = call_qwen(SYSTEM_PROMPT, user_prompt)
        print("\n--- 面试官反馈 ---")
        print(feedback)

if __name__ == "__main__":
    main()