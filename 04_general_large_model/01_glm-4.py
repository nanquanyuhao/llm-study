from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os
import time

load_dotenv()
api_key = os.getenv('API_KEY')

'''
同步调用
'''
client = ZhipuAI(api_key=api_key)
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的slogan"},
        {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "智谱AI开放平台"},
        {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
        {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
    ],
)
print(response.choices[0].message)
print(str(response))


'''
流式调用
'''
client = ZhipuAI(api_key=api_key) # 请填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "system", "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},
        {"role": "user", "content": "我对太阳系的行星非常感兴趣，特别是土星。请提供关于土星的基本信息，包括其大小、组成、环系统和任何独特的天文现象。"},
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta)
    print(str(chunk))


'''
函数调用
'''
client = ZhipuAI(api_key=api_key)
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
]
messages = [
    {
        "role": "user",
        "content": "你能帮我查询2024年1月1日从北京南站到上海的火车票吗？"
    }
]
response = client.chat.completions.create(
    model="glm-4",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
print(response.choices[0].message)
print(response)


'''
异步调用
'''
client = ZhipuAI(api_key=api_key)
response = client.chat.asyncCompletions.create(
    model="glm-4",
    messages=[
        {
            "role": "user",
            "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"
        }
    ],
)
print(response)

task_id = response.id
task_status = response.task_status
get_cnt = 0
print('任务 ID 为：{}，请求 ID 为：{}，模型为：{}，任务状态为：{}'.format(task_id, response.request_id, response.model, task_status))

while task_status != 'SUCCESS' and task_status != 'FAILED' and get_cnt <= 40:
    result_response = client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
    print(result_response)
    task_status = result_response.task_status

    time.sleep(2)
    get_cnt += 1