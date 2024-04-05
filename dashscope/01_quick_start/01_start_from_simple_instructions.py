# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

from http import HTTPStatus
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

'''
当前示例为通过 prompt 调用的方式
'''
def sample_sync_call():

    prompt_text = '用萝卜、土豆、茄子做饭，给我个菜谱。'
    resp = dashscope.Generation.call(
        model='qwen-turbo',
        prompt=prompt_text
    )
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if resp.status_code == HTTPStatus.OK:
        # 输出完整响应查看结构
        print('完整响应 resp 为：{}'.format(resp))
        print('响应输出 resp.output 为：{}'.format(resp.output))  # The output text
        print('响应用量 resp.usage 为：{}'.format(resp.usage))  # The usage information
    else:
        print(resp.code)  # The error code.
        print(resp.message)  # The error message.

sample_sync_call()