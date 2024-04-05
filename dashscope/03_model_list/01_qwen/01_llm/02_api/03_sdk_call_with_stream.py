from http import HTTPStatus
from dashscope import Generation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

'''
不同于之前使用方式，本次 incremental_output=True 表示增量输出
'''
def call_with_stream():
    messages = [
        {'role': 'user', 'content': '如何做西红柿炖牛腩？'}]
    responses = Generation.call("qwen-turbo",
                                # 设置 api_key
                                api_key = api_key,
                                messages=messages,
                                result_format='message',  # set the result to be "message" format.
                                stream=True, # set stream output.
                                incremental_output=True  # get streaming output incrementally.
                                )
    full_content = ''  # with incrementally we need to merge output.
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            full_content += response.output.choices[0]['message']['content']
            print(response)
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    print('Full response:\n' + full_content)


if __name__ == '__main__':
    call_with_stream()