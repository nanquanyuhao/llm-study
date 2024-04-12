# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import json
from urllib import request
from http import HTTPStatus

import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

# 以异步调用的方式向文件转写服务提交一个任务，返回被提交任务的信息
task_response = dashscope.audio.asr.Transcription.async_call(
    model='paraformer-v1',
    file_urls=[
        'https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/paraformer/hello_world_female2.wav',
        'https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/paraformer/hello_world_male2.wav'
    ])

# 以阻塞的方式等待异步任务结束（即到达 SUCCEEDED 或 FAILED 状态），返回任务的状态和文件转写结果
transcribe_response=dashscope.audio.asr.Transcription.wait(task=task_response.output.task_id)
if transcribe_response.status_code == HTTPStatus.OK:
    print(json.dumps(transcribe_response.output, indent=4, ensure_ascii=False))
    print('transcription done!')