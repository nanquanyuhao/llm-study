from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

'''
检索知识库
'''
knowledge_id = 1774449593111793664

client = ZhipuAI(api_key=api_key)
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "user", "content": "产品打造"},
    ],
    tools=[
            {
                "type": "retrieval",
                "retrieval": {
                    "knowledge_id": knowledge_id,
                    "prompt_template": "从文档\n\"\"\"\n{{knowledge}}\n\"\"\"\n中找问题\n\"\"\"\n{{question}}\n\"\"\"\n的答案，找到答案就仅使用文档语句回答问题，找不到答案就用自身知识回答并且告诉用户该信息不是来自文档。\n不要复述问题，直接开始回答。"
                }
            }
            ],
    stream=True,
)

for chunk in response:
    print(chunk.choices[0].delta)