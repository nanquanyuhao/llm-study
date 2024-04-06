from dashscope import BatchTextEmbedding
from http import HTTPStatus
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

# 创建异步任务
def create_async_task():
    rsp = BatchTextEmbedding.async_call(model=BatchTextEmbedding.Models.text_embedding_async_v1,
                                        url="https://modelscope.oss-cn-beijing.aliyuncs.com/resource/text_embedding_file.txt",
                                        api_key=api_key,
                                        text_type="document")
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
    return rsp


# 获取异步任务信息
def fetch_task_status(task):
    status = BatchTextEmbedding.fetch(task, api_key)
    print(status)
    if status.status_code == HTTPStatus.OK:
        print(status.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (status.status_code, status.code, status.message))


# 等待异步任务结束，内部封装轮询逻辑，会一直等待任务结束
def wait_task(task):
    rsp = BatchTextEmbedding.wait(task, api_key)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


# 取消异步任务，只有处于PENDING状态的任务才可以取消
def cancel_task(task):
    rsp = BatchTextEmbedding.cancel(task, api_key)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    task_info = create_async_task()
    fetch_task_status(task_info)
    wait_task(task_info)