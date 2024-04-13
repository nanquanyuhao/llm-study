# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import dashscope
from dashscope import Generation
from http import HTTPStatus
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

'''未开通权限报错如下：
    AccessDenied
    Access denied.
'''
response = Generation.call(
    model='chatyuan-large-v2',
    prompt='翻译成英文：春天来了，花朵都开了。'
)
# The response status_code is HTTPStatus.OK indicate success,
# otherwise indicate request is failed, you can get error code
# and message from code and message.
if response.status_code == HTTPStatus.OK:
    print(response.output)  # The output text
else:
    print(response.code)  # The error code.
    print(response.message)  # The error message.