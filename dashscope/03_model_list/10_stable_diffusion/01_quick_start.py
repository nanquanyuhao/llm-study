from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

model = "stable-diffusion-xl"
prompt = "Eagle flying freely in the blue sky and white clouds"

'''情况说明
    整体需要申请开通才可调用
'''
def simple_call():
    rsp = dashscope.ImageSynthesis.call(model=model,
                                        prompt=prompt,
                                        negative_prompt="garfield",
                                        n=1,
                                        size='1024*1024')
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
        # save file to current directory
        for result in rsp.output.results:
            file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
            with open('./%s' % file_name, 'wb+') as f:
                f.write(requests.get(result.url).content)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    simple_call()