# SSE 关闭情况下的请求
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "qwen-vl-plus",
    "input":{
        "messages":[
            {
                "role": "system",
                "content": [
                    {"text": "You are a helpful assistant."}
                ]
            },
            {
                "role": "user",
                "content": [
                    {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"},
                    {"text": "这个图片是哪里？"}
                ]
            }
        ]
    },
    "parameters": {
    }
}'

# SSE 开启情况下的请求
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'X-DashScope-SSE: enable' \
--data '{
    "model": "qwen-vl-plus",
    "input":{
        "messages":[
            {
                "role": "system",
                "content": [
                    {"text": "You are a helpful assistant."}
                ]
            },
            {
                "role": "user",
                "content": [
                    {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"},
                    {"text": "这个图片是哪里？"}
                ]
            }
        ]
    },
    "parameters": {
    }
}'