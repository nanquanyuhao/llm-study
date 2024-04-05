from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

'''
同步调用
'''
client = ZhipuAI(api_key=api_key)
response = client.chat.completions.create(
    model="glm-4v",
    messages=[
       {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "图里有什么"
          },
          {
            "type": "image_url",
            "image_url": {
                "url" : "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"
            }
          }
        ]
      }
    ]
)
print(response.choices[0].message)
print(str(response))


'''
流式调用
'''
client = ZhipuAI(api_key=api_key)
response = client.chat.completions.create(
    model="glm-4v",
    messages=[
        {"role": "user",
          "content": [
          {
            "type": "text",
            "text": "图里有什么"
          },
          {
            "type": "image_url",
            "image_url": {
                "url" : "https://static001.infoq.cn/resource/image/5f/6e/5f36806314a58af989b842a83dbc426e.jpg"
            }
          }
        ]
        },
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta)
    print(str(chunk))