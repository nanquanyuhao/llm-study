import random
from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": [
                            "celsius",
                            "fahrenheit"
                        ]
                    }
                },
                "required": [
                    "location"
                ]
            }
        }
    }
]


def call_with_messages():
    messages = [
        {
            "content": "What is the weather like in Boston?",
            "role": "user"
        },
        {
            "role": "assistant",
            "content": "",
            "tool_calls": [
                {
                    "function": {
                        "name": "get_current_weather",
                        "arguments": "{\"location\": \"Boston\", \"unit\": \"fahrenheit\"}"
                    },
                    "id": "",
                    "type": "function"
                }
            ]
        },
        {
            # 这里就是本地工具调用后需要追加到消息上下文中的结果，最终还需要反馈给 LLM 进行最终的回复
            "content": "Boston is raining.",
            "name": "get_current_weather",
            "role": "tool"
        }
    ]
    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        tools=tools,
        seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    call_with_messages()