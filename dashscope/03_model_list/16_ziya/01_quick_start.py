# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import dashscope
from http import HTTPStatus
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

'''权限不足
    AccessDenied
    Access denied.
'''
response = dashscope.Generation.call(
    model='ziya-llama-13b-v1',
    prompt='<human>:帮我写一份去西安的旅游计划\n<bot>:'
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