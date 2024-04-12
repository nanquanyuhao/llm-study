# coding=utf-8
# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

from dashscope import Understanding
from http import HTTPStatus
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

response = Understanding.call(
    model='opennlu-v1',
    sentence='老师今天表扬我了',
    labels='积极，消极',
    task='classification',
    api_key=api_key)

if response.status_code == HTTPStatus.OK:
    print(json.dumps(response.output, indent=4, ensure_ascii=False))
    # 打印整个响应体
    print(response)
else:
    print('Code: %d, status: %s, message: %s' % (response.status_code, response.code, response.message))