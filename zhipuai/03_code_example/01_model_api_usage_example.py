from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

'''
System Prompt
'''
client = ZhipuAI(api_key=api_key)
response = client.chat.completions.create(
    model="glm-4", 
    messages=[
              {"role": "system", "content": "你是一个聪明且富有创造力的小说作家"},
              {"role": "user", "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"}
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta)


'''
函数调用
'''
client = ZhipuAI(api_key=api_key)

response = client.chat.completions.create(
    model="glm-4",
    messages = [
        {
            "role": "user",
            "content": "你能帮我查询2024年1月1日从北京南站到上海的火车票吗？"
        }
    ],
    tools = [
        {
            "type": "function",
            "function": {
                "name": "query_train_info",
                "description": "根据用户提供的信息，查询对应的车次",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "departure": {
                            "type": "string",
                            "description": "出发城市或车站",
                        },
                        "destination": {
                            "type": "string",
                            "description": "目的地城市或车站",
                        },
                        "date": {
                            "type": "string",
                            "description": "要查询的车次日期",
                        },
                    },
                    "required": ["departure", "destination", "date"],
                },
            }
        }
    ],
    # 控制模型如何选择函数调用，auto 为默认值，此时模型根据上下文信息自行选择是否返回函数调用（目前函数调用仅支持 auto 模式）
    tool_choice="auto",
)
print(response.choices[0].message)


'''
检索
'''
client = ZhipuAI(api_key=api_key) # 请填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": "你好！你叫什么名字"},
    ],
    tools=[
        {
            "type": "retrieval",
            "retrieval": {
                "knowledge_id": "your knowledge id",
                "prompt_template": "从文档\n\"\"\"\n{{knowledge}}\n\"\"\"\n中找问题\n\"\"\"\n{{question}}\n\"\"\"\n的答案，找到答案就仅使用文档语句回答问题，找不到答案就用自身知识回答并且告诉用户该信息不是来自文档。\n不要复述问题，直接开始回答。"
            }
        }
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta)