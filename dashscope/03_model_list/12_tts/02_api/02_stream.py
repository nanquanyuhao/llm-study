# coding=utf-8

import dashscope
import sys
from dashscope.api_entities.dashscope_response import SpeechSynthesisResponse
from dashscope.audio.tts import ResultCallback, SpeechSynthesizer, SpeechSynthesisResult
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

class Callback(ResultCallback):
    def on_open(self):
        print('Speech synthesizer is opened.')

    def on_complete(self):
        print('Speech synthesizer is completed.')

    def on_error(self, response: SpeechSynthesisResponse):
        print('Speech synthesizer failed, response is %s' % (str(response)))

    def on_close(self):
        print('Speech synthesizer is closed.')

    def on_event(self, result: SpeechSynthesisResult):
        if result.get_audio_frame() is not None:
            print('audio result length:', sys.getsizeof(result.get_audio_frame()))

        if result.get_timestamp() is not None:
            print('timestamp result:', str(result.get_timestamp()))

callback = Callback()
SpeechSynthesizer.call(model='sambert-zhichu-v1',
                       text='今天周几啊兄嘚？',
                       sample_rate=48000,
                       callback=callback,
                       word_timestamp_enabled=True,
                       phoneme_timestamp_enabled=True)