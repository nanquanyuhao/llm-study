from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv('API_KEY')

'''
Function Call 流程实践
'''
client = ZhipuAI(api_key=api_key)
messages = []
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_flight_number",
            "description": "根据始发地、目的地和日期，查询对应日期的航班号",
            "parameters": {
                "type": "object",
                "properties": {
                    "departure": {
                        "description": "出发地",
                        "type": "string"
                    },
                    "destination": {
                        "description": "目的地",
                        "type": "string"
                    },
                    "date": {
                        "description": "日期",
                        "type": "string",
                    }
                },
                "required": [ "departure", "destination", "date" ]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ticket_price",
            "description": "查询某航班在某日的票价",
            "parameters": {
                "type": "object",
                "properties": {
                    "flight_number": {
                        "description": "航班号",
                        "type": "string"
                    },
                    "date": {
                        "description": "日期",
                        "type": "string",
                    }
                },
                "required": [ "flight_number", "date"]
            },
        }
    },
]

# 我们想查询2024年1月20日从北京前往上海的航班。我们向模型提供这个信息
messages.append({"role": "user", "content": "帮我查询从2024年1月20日，从北京出发前往上海的航班"})
response = client.chat.completions.create(
    model="glm-4",
    messages=messages,
    tools=tools,
)
print(response.choices[0].message)
messages.append(response.choices[0].message.model_dump())

# 尝试提供信息，触发模型对 get_ticket_price 函数的调用
messages = []
messages.append({"role": "system", "content": "不要假设或猜测传入函数的参数值。如果用户的描述不明确，请要求用户提供必要信息"})
messages.append({"role": "user", "content": "帮我查询2024年1月20日1234航班的票价"})
response = client.chat.completions.create(
    model="glm-4",
    messages=messages,
    tools=tools,
)
print(response.choices[0].message)
messages.append(response.choices[0].message.model_dump())

# 强制模型使用特定函数
# 通过设置 tool_choice 为 {"type": "function", "function": {"name": "get_ticket_price"}} 以强制模型生成调用 get_ticket_price 的参数
messages = []
messages.append({"role": "system", "content": "不要假设或猜测传入函数的参数值。如果用户的描述不明确，请要求用户提供必要信息"})
messages.append({"role": "user", "content": "帮我查询1234航班的票价"})
response = client.chat.completions.create(
    model="glm-4",
    messages=messages,
    tools=tools,
    # 此时模型被强制触发对 get_ticket_price 函数的调用，参数为：date="2022-01-01", flight_number="1234"。注意到此时模型假设了一个 date
    tool_choice={"type": "function", "function": {"name": "get_ticket_price"}},
)
print(response.choices[0].message)
messages.append(response.choices[0].message.model_dump())


'''
使用模型生成的参数调用函数
'''
# 获取班次号的函数定义
def get_flight_number(date:str , departure:str , destination:str):

    flight_number = {
        "北京":{
            "上海" : "1234",
            "广州" : "8321",
        },
        "上海":{
            "北京" : "1233",
            "广州" : "8123",
        }
    }
    return { "flight_number":flight_number[departure][destination] }

# 获取票价的函数定义
def get_ticket_price(date:str , flight_number:str):

    return {"ticket_price": "1000"}

# Function call 的函数定义
def parse_function_call(model_response, messages):

    # 打印一下传入的响应看一下结构
    print('解析后的 Function call 结构：{}'.format(model_response))

    # 处理函数调用结果，根据模型返回参数，调用对应的函数。
    # 调用函数返回结果后构造 tool message，再次调用模型，将函数结果输入模型
    # 模型会将函数调用结果以自然语言格式返回给用户。
    if model_response.choices[0].message.tool_calls:

        tool_call = model_response.choices[0].message.tool_calls[0]
        args = tool_call.function.arguments
        function_result = {}
        if tool_call.function.name == "get_flight_number":
            function_result = get_flight_number(**json.loads(args))
        if tool_call.function.name == "get_ticket_price":
            function_result = get_ticket_price(**json.loads(args))

        messages.append({
            "role": "tool",
            # {"flight_number": "8321"}
            "content": f"{json.dumps(function_result)}",
            "tool_call_id":tool_call.id
        })
        response = client.chat.completions.create(
            model="glm-4",
            messages=messages,
            tools=tools,
        )
        print(response.choices[0].message)
        messages.append(response.choices[0].message.model_dump())
        print('最终返回结构：{}'.format(messages))

# 查询北京到广州的航班
messages = []
messages.append({"role": "system", "content": "不要假设或猜测传入函数的参数值。如果用户的描述不明确，请要求用户提供必要信息"})
messages.append({"role": "user", "content": "帮我查询1月23日，北京到广州的航班"})

response = client.chat.completions.create(
    model="glm-4", 
    messages=messages,
    tools=tools,
)
print(response.choices[0].message)
messages.append(response.choices[0].message.model_dump())

parse_function_call(response, messages)

# 查询北京到广州的航班
messages.append({"role": "user", "content": "这趟航班的价格是多少？"})
response = client.chat.completions.create(
    model="glm-4",
    messages=messages,
    tools=tools,
)
print(response.choices[0].message)
messages.append(response.choices[0].message.model_dump())

parse_function_call(response, messages)