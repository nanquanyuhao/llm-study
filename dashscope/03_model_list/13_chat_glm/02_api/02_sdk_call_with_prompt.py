from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_prompt():
    prompt = '介绍下杭州'
    rsp = dashscope.Generation.call(model='chatglm3-6b',
                                    prompt=prompt,
                                    history=[],
                                    api_key=api_key)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    call_with_prompt()