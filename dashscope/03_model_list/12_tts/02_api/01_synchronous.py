# coding=utf-8

import dashscope
from dashscope.audio.tts import SpeechSynthesizer
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

path = 'dashscope/03_model_list/12_tts/01_quick_start'

result = SpeechSynthesizer.call(model='sambert-zhichu-v1',
                                text='今天周几啊兄嘚，兄弟？',
                                sample_rate=48000,
                                format='wav')

if result.get_audio_data() is not None:
    with open('{}/temp/output.wav'.format(path), 'wb') as f:
        f.write(result.get_audio_data())
print('  get response: %s' % (result.get_response()))