from http import HTTPStatus
from dashscope import Generation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_stream():
    messages = [
        {'role': 'user', 'content': '介绍下杭州？'}]
    responses = Generation.call(
        model='yi-34b-chat',
        api_key=api_key,
        messages=messages,
        result_format='message',  # set the result to be "message" format.
        stream=True,
        incremental_output=True  # get streaming output incrementally
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