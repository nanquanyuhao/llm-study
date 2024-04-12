# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import json
import dashscope
from dashscope import Generation
from http import HTTPStatus
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

responses = Generation.call(
    model='sanle-v1',
    prompt='请简要介绍一下浙江大学',
    api_key=api_key,
    stream=True,
)
# The response status_code is HTTPStatus.OK indicate success,
# otherwise indicate request is failed, you can get error code
# and message from code and message.
for response in responses:
    if response.status_code==HTTPStatus.OK:
        print(json.dumps(response.output, indent=4, ensure_ascii=False))
    else:
        print('Code: %d, status: %s, message: %s' % (response.status_code, response.code, response.message))