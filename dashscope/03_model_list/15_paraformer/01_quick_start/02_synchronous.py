# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import requests
from http import HTTPStatus

import dashscope
from dashscope.audio.asr import Recognition
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

path = 'dashscope/03_model_list/15_paraformer/01_quick_start/temp/'

r = requests.get(
    'https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/paraformer/hello_world_female2.wav'
)
with open('{}asr_example.wav'.format(path), 'wb') as f:
    f.write(r.content)

recognition = Recognition(model='paraformer-realtime-v1',
                          format='wav',
                          sample_rate=16000,
                          callback=None)

result = recognition.call('{}asr_example.wav'.format(path))
if result.status_code == HTTPStatus.OK:

    # 需要显示添加 encoding='utf8' 保证不出现中文乱码
    with open('{}asr_result.txt'.format(path), 'w+', encoding='utf8') as f:
        for sentence in result.get_sentence():
            f.write(str(sentence) + '\n')
    print('Recognition done!')
else:
    print('Error: ', result.message)