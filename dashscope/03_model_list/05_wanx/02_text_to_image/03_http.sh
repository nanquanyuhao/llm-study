# 作业提交
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-v1",
    "input": {
        "prompt": "一只奔跑的猫"
    },
    "parameters": {
        "style": "<sketch>", 
        "size": "1024*1024",
        "n":4, 
        "seed":42
    }
}'

# 作业任务状态查询和结果获取
curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/1bd7c9b9-276f-4036-ab12-a91fc577bed2

