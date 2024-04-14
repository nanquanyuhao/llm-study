# 请求示例（SSE关闭）
curl -v --location --request POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'X-DashScope-Plugin: {"calculator":{}}' \
--data '{
    "model": "qwen-plus",
    "input": {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "12345*98765是多少"
            }
        ]
    },
    "parameters": {
        "result_format": "message",
        "seed": 42
    }
}'