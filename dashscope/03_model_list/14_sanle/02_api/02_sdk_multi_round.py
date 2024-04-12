# coding=utf-8
# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import dashscope
from dashscope import Generation
from http import HTTPStatus
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

'''试用报错
    Code: 403, status: AccessDenied, message: Access denied.
'''
response=Generation.call(
    model='sanle-v1',
    prompt='请简要介绍一下浙江大学',
    history=[
        {
            "bot": "我当然知道浙江大学",
            "user": "你知道浙江大学么",
        }
     ],
    api_key=api_key
  )

if response.status_code==HTTPStatus.OK:
    print(json.dumps(response.output, indent=4, ensure_ascii=False))
else:
    print('Code: %d, status: %s, message: %s' % (response.status_code, response.code, response.message))