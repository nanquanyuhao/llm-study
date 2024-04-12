from http import HTTPStatus
from dashscope import Generation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_messages():
    messages = [
        {'role': 'system', 'content':'You are a helpful assistant.'},
        {'role': 'user', 'content': '介绍下杭州'}]
    gen = Generation()
    response = gen.call(
        'chatglm3-6b',
        api_key=api_key,
        messages=messages,
        result_format='message',  # set the result is message format.
    )
    print(response)

if __name__ == '__main__':
    call_with_messages()