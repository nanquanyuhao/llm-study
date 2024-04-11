# 作业提交接口调用
# 权限不足，显示：{"code":"AccessDenied","message":"Access denied.","request_id":"7d409f78-03f8-96f0-8c23-b395382e95a3"}
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "stable-diffusion-xl",
    "input": {
        "prompt": "a running cat",
        "negative_prompt": "yellow cat"
    },
    "parameters": {
        "size": "512*512",
        "n":4, 
        "seed":42
    }
}'

# 作业任务状态查询和结果获取接口
# 权限不足，显示：{"request_id":"77a5ea1b-b57c-9c01-8620-7f8570797a77","output":{"task_id":"86ecf553-d340-4e21-af6e-a0c6a421c010��","task_status":"UNKNOWN"}}
curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/86ecf553-d340-4e21-af6e-a0c6a421c010