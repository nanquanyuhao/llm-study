from http import HTTPStatus
from dashscope import MultiModalConversation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def conversation_call():
    """Sample of multiple rounds of conversation.
    """
    messages = [
        {
            "role": "user",
            "content": [
                {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"},
                {"text": "这是什么?"},
            ]
        }
    ]
    response = MultiModalConversation.call(model='qwen-vl-plus',
                                           messages=messages,
                                           api_key=api_key)
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.
    messages.append({'role': response.output.choices[0].message.role,
                     'content': response.output.choices[0].message.content})
    messages.append({"role": "user",
                     "content": [
                         {"text": "她们在干什么?", }
                     ]})
    
    # 用的时候导入 json
    import json
    print(json.dumps(messages, ensure_ascii=False))
    response = MultiModalConversation.call(model='qwen-vl-plus',
                                           messages=messages,
                                           api_key=api_key)
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.


if __name__ == '__main__':
    conversation_call()