# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import pyaudio
import dashscope
from dashscope.audio.asr import (Recognition, RecognitionCallback,
                                 RecognitionResult)
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

mic = None
stream = None

# 创建Recognition示例并使用上文创建的参数来调用基于回调方式的流式实时识别
class Callback(RecognitionCallback):
    def on_open(self) -> None:
        global mic
        global stream
        print('RecognitionCallback open.')
        mic = pyaudio.PyAudio()
        stream = mic.open(format=pyaudio.paInt16,
                          channels=1,
                          rate=16000,
                          input=True)

    def on_close(self) -> None:
        global mic
        global stream
        print('RecognitionCallback close.')
        stream.stop_stream()
        stream.close()
        mic.terminate()
        stream = None
        mic = None

    def on_event(self, result: RecognitionResult) -> None:
        # 获取当前识别的句子及时间戳信息
        print('RecognitionCallback sentence: ', result.get_sentence())

callback = Callback()
# 创建一个使用 paraformer-realtime-v1 模型，使用 16k 采样率，PCM 音频格式的实时识别请求参数
recognition = Recognition(model='paraformer-realtime-v1',
                          format='pcm',
                          sample_rate=16000,
                          callback=callback)
recognition.start()

# 在一段循环中通过 Recognition 对象的 send_audio_frame 来发送二进制音频数据
while True:
    if stream:
        data = stream.read(3200, exception_on_overflow = False)
        recognition.send_audio_frame(data)
    else:
        break

recognition.stop()