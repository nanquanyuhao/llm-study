# 提交接口调用
# 请求示例（SSE 关闭）
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "sanle-v1",
    "input": {
        "prompt": "请简要介绍一下浙江大学",
        "history":[
            {
                "user": "你知道浙江大学么",
                "bot": "我当然知道浙江大学"
            }
        ]
    },
    "parameters": {
        "top_p": 0.8,
        "top_k": 50,
        "seed": 42
    }
}'

# 请求示例（SSE开启）
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'X-DashScope-SSE: enable' \
--data '{
    "model": "sanle-v1",
    "input": {
        "prompt": "请简要介绍一下浙江大学",
        "history":[
            {
                "user":"你知道浙江大学么",
                "bot":"我当然知道浙江大学"
            }
        ]
    },
    "parameters": {
        "top_p": 0.8,
        "top_k": 50,
        "seed": 42, 
        "enable_search": false
    }
}'