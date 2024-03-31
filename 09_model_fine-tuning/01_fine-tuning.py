from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

'''
创建微调任务

会报错，实际只有花钱升级为开发者 Pro 解决：
zhipuai.core._errors.APIStatusError: 
Error code: 404, with error text {"error":{"code":"1600","message":"微调功能未开放，请联系客服开放"}}
'''
client = ZhipuAI(api_key=api_key)
job = client.fine_tuning.jobs.create(
    model="chatglm3-6b",
    training_file="file-20240114063454130-bnm25",   # 请填写已成功上传的文件id
    validation_file="file-yyy", # 请填写已成功上传的文件id
    suffix="<self-defined>",
)
job_id = job.id

print(job_id)

'''
查询微调任务事件
'''
client = ZhipuAI(api_key=api_key)

paged_events = client.fine_tuning.jobs.list_events(
    job_id,  # job_id 来自于创建任务返回的信息
    limit=50,
)
print(paged_events)


'''
查询微调任务
'''
client = ZhipuAI(api_key=api_key)

fine_tuning_job = client.fine_tuning.jobs.retrieve(
    # job_id 来自于创建任务返回的信息
    fine_tuning_job_id = job_id,
)
print(fine_tuning_job)


'''
查询个人微调任务
'''
client = ZhipuAI(api_key=api_key)

client.fine_tuning.jobs.list()