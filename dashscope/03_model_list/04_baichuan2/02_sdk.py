from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '介绍下故宫？'}]
    response = dashscope.Generation.call(
        model='baichuan2-7b-chat-v1',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


def call_with_prompt():
    prompt = '介绍下故宫'
    rsp = dashscope.Generation.call(model='baichuan2-7b-chat-v1',
                                    prompt=prompt)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    type = 'message'
    if type == 'prompt':
        call_with_prompt()
    elif type == 'message':
        call_with_messages()
    else:
        print("call type not support")