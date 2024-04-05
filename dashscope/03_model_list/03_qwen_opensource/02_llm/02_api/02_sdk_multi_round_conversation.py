import random
from http import HTTPStatus
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def multi_round_conversation():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '请介绍一下上海有什么好玩的地方'}]
    response = Generation.call(
        'qwen1.5-72b-chat',
        api_key=api_key,
        messages=messages,
        # set the random seed, optional, default to 1234 if not set
        seed=random.randint(1, 10000),
        result_format='message',  # set the result to be "message"  format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
        messages.append({'role': response.output.choices[0]['message']['role'],
                         'content': response.output.choices[0]['message']['content']})
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
    messages.append({'role': Role.USER, 'content': '能否缩短一些，只讲三点'})
    response = Generation.call(
        'qwen1.5-72b-chat',
        api_key=api_key,
        messages=messages,
        result_format='message',  # set the result to be "message"  format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    multi_round_conversation()