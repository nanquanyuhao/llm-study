# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
import dashscope
from http import HTTPStatus
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

'''试用报错
    AccessDenied
    Access denied.
'''
response = dashscope.Generation.call(
    model='sanle-v1',
    prompt='请简要介绍一下浙江大学',
    api_key=api_key
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