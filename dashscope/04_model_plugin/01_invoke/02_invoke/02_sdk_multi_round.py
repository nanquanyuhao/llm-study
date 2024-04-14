from http import HTTPStatus
import dashscope
from dashscope.api_entities.dashscope_response import Role
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_messages():
    plugins = {'calculator': {}}  # choose the desired plugin(s).
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '12345 * 98765是多少'}]
    response = dashscope.Generation.call(
        model='qwen-plus',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
        plugins=plugins,
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
        messages.extend(response.output.choices[0]['messages'])
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        
    messages.append({'role': Role.USER, 'content': '调用插件计算一下再加上22222是多少'})
    response = dashscope.Generation.call(
        model='qwen-plus',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
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