from http import HTTPStatus
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def multi_round():
    messages = [{'role': Role.SYSTEM, 'content': 'You are a helpful assistant.'},
                {'role': Role.USER, 'content': '如何做西红柿炖牛腩？'}]
    response = Generation.call("qwen-turbo",
                               messages=messages,
                               # set the result to be "message" format.
                               result_format='message',
                               )
    if response.status_code == HTTPStatus.OK:
        print(response)

        # append result assistant response to messages.
        messages.append({'role': response.output.choices[0]['message']['role'],
                         'content': response.output.choices[0]['message']['content']})
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        # 如果失败，将最后一条user message从message列表里删除，确保user/assistant消息交替出现
        messages = messages[:-1]
    messages.append({'role': Role.USER, 'content': '不放糖可以吗？'})

    # 最后一次调用前输出一下 messages
    print('最后一次调用前 messages 内容为：{}'.format(messages))

    # make second round call
    response = Generation.call("qwen-turbo",
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


if __name__ == '__main__':
    multi_round()