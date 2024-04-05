# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_prompt():
    response = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_turbo,
        prompt='如何做炒西红柿鸡蛋？'
    )
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if response.status_code == HTTPStatus.OK:
        print(response.output)  # The output text
        print(response.usage)  # The usage information
    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.

if __name__ == '__main__':
    call_with_prompt()