from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

# 请填写您自己的APIKey
client = ZhipuAI(api_key=api_key)
response = client.chat.completions.create(
    # 填写需要调用的模型名称
    model="glm-4", 
    messages=[
        {"role": "user", "content": "你好！你叫什么名字"},
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta)