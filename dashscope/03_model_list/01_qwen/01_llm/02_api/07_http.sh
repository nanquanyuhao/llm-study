# SSE 关闭情况下的请求
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "qwen-turbo",
    "input":{
        "messages":[      
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "你好，哪个公园距离我最近？"
            }
        ]
    },
    "parameters": {
        "result_format": "message"
    }
}'

# SSE 开启情况下的请求
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'X-DashScope-SSE: enable' \
--data '{
    "model": "qwen-turbo",
    "input":{
        "messages":[      
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "你好，哪个公园距离我最近？"
            }
        ]
    },
    "parameters": {
        "result_format": "message"
    }
}'