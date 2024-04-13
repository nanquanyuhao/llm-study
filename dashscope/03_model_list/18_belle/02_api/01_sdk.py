# coding=utf-8
# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import dashscope
from dashscope import Generation
from http import HTTPStatus
import json
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

'''权限不足
    Code: 403, status: AccessDenied, message: Access denied.
'''
response=Generation.call(
    model='belle-llama-13b-2m-v1',
    prompt='Human:你好\n\nAssistant:'
    )

if response.status_code==HTTPStatus.OK:
    print(json.dumps(response, indent=4, ensure_ascii=False))
else:
    print('Code: %d, status: %s, message: %s' % (response.status_code, response.code, response.message))