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
    model='ziya-llama-13b-v1',
    prompt='<human>:帮我写一份去西安的旅游计划\n<bot>:'
  )

if response.status_code==HTTPStatus.OK:
    print(json.dumps(response, indent=4, ensure_ascii=False))
else:
    print('Code: %d, status: %s, message: %s' % (response.status_code, response.code, response.message))