from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_messages():
    plugins = {'code_interpreter': {}}  # choose the desired plugin(s).
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '画一个y=x^2的函数图'}]
    response = dashscope.Generation.call(
        model='qwen-plus',
        messages=messages,
        result_format='message',  # set the result to be 'message' format.
        plugins=plugins,
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