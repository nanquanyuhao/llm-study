from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

'''权限申请中，报错如下：
    Request id: baa9fc12-794c-9452-91e1-f09af4e8fb47, Status code: 403, error code: InvalidPlugin.AccessDenied, error message: Plugin ["ocr"] access denied.
'''
def call_with_messages():
    plugins = {'ocr': {}}  # choose the desired plugin(s).
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user',
                    'content': '识别一下这个图片上的文字：https://dashscope.oss-cn-beijing.aliyuncs.com/samples/plugin/20231124161643.jpg'
                }]
    response = dashscope.Generation.call(
        model='qwen-plus',
        messages=messages,
        result_format='message',  # set the result to be 'message' format.
        plugins=plugins,
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    call_with_messages()