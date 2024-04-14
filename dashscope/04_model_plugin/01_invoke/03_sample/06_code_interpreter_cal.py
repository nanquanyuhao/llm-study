from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_messages():
    plugins = {'code_interpreter': {}}  # choose the desired plugin(s).
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '有若干只鸡兔同在一个笼子里，从上面数，有100个头，从下面数，有334只脚。问笼中各有多少只鸡和兔?'}]
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