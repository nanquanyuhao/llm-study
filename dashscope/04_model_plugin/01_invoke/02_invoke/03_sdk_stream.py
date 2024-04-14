from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_messages():
    plugins = {'calculator': {}}  # choose the desired plugin(s).
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '12345*98765是多少'}]
    responses = dashscope.Generation.call(
        model='qwen-plus',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
        plugins=plugins,
        stream=True,
    )
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            print(response)
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))


if __name__ == '__main__':
    call_with_messages()