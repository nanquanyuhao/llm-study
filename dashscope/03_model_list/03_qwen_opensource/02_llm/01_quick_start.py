from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_messages():

    messages = [
        {'role': 'user', 'content': '用萝卜、土豆、茄子做饭，给我个菜谱'}]
    response = dashscope.Generation.call(
        'qwen1.5-72b-chat',
        messages=messages,
        result_format='message',  # set the result is message format.
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