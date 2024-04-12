# coding=utf-8

import dashscope
from dashscope.audio.tts import SpeechSynthesizer
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

path = 'dashscope/03_model_list/12_tts/01_quick_start/temp/'

result = SpeechSynthesizer.call(model='sambert-zhichu-v1',
                                text='今天周几啊兄嘚？',
                                sample_rate=48000)
if result.get_audio_data() is not None:
    with open('{}output.wav'.format(path), 'wb') as f:
        f.write(result.get_audio_data())