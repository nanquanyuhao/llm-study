from http import HTTPStatus
from dashscope import ImageSynthesis
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

# 创建异步任务
def create_async_task():
    rsp = ImageSynthesis.async_call(model=ImageSynthesis.Models.wanx_v1,
                                    prompt='Eagle flying in blue sky',
                                    api_key=api_key,
                                    n=4,
                                    size='1024*1024')
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
    return rsp


# 获取异步任务信息
def fetch_task_status(task):
    status = ImageSynthesis.fetch(task, api_key)
    print(status)
    if status.status_code == HTTPStatus.OK:
        print(status.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (status.status_code, status.code, status.message))


# 等待异步任务结束
def wait_task(task):
    rsp = ImageSynthesis.wait(task, api_key)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


# 取消异步任务，只有处于PENDING状态的任务才可以取消
def cancel_task(task):
    rsp = ImageSynthesis.cancel(task, api_key)
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