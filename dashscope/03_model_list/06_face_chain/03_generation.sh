# 作业提交接口调用
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/album/gen_potrait' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer <your-dashscope-api-key>' \
--header 'Content-Type: application/json' \
--data '{
    "model": "facechain-generation",
    "parameters": {
        "style": "f_idcard_female", 
        "size": "512*512",
        "n":4
    },
    "resources": [
        {
            "resource_id": "women_model",
            "resource_type": "facelora"
        }
    ]
}'

# 作业任务状态查询和结果获取接口
curl -X GET \
--header 'Authorization: Bearer <your-dashscope-api-key>' \
https://dashscope.aliyuncs.com/api/v1/tasks/86ecf553-d340-4e21-af6e-a0c6a421c010