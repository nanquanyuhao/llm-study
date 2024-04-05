from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

# 以下为测试过可使用的模型
model = 'qwen-turbo'
# model = 'qwen-plus'
# model = 'qwen-7b-chat'
# model = 'qwen-14b-chat'

def tokenizer():
    response = dashscope.Tokenization.call(model = model,
                                 messages=[{'role': 'user', 'content': '你好？'}],
                                 )
    if response.status_code == HTTPStatus.OK:
        print('Result is: %s' % response)
    else:
        print('Failed request_id: %s, status_code: %s, code: %s, message:%s' %
              (response.request_id, response.status_code, response.code,
               response.message))

if __name__ == '__main__':
    tokenizer()