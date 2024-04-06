# 作业提交接口调用
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding/text-embedding' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'X-DashScope-Async: enable' \
--data '{
    "model": "text-embedding-async-v1",
    "input": {
        "url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/text_embedding_file.txt"
    },
    "parameters": {
        "text_type": "query"
    }
}'

# 作业任务状态查询和结果获取接口
curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/d9bc2be9-dc6e-434c-8a95-6dab3aa0f7b2