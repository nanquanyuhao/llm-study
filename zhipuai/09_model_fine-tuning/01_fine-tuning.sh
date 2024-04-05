# 整体权限不足，整体看不到效果

# 创建微调任务
curl 'https://open.bigmodel.cn/api/paas/v4/fine_tuning/jobs' \
-X POST \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data '{
    "model": "chatglm3-6b",
    "training_file": "file-xxx",
    "validation_file": "file-yyy",
    "suffix": "<self-defined>"
}'

# 查询微调任务事件
curl 'https://open.bigmodel.cn/api/paas/v4/fine_tuning/jobs/<job_id>/events?limit=50' --header 'Authorization: Bearer <token>'

# 询微调任务
curl 'https://open.bigmodel.cn/api/paas/v4/fine_tuning/jobs/<job_id>' --header 'Authorization: Bearer <token>'

# 查询个人微调任务
curl 'https://open.bigmodel.cn/api/paas/v4/fine_tuning/jobs' --header 'Authorization: Bearer <token>'