# 目前没有权限，需要申请开通
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer <your-dashscope-api-key>' \
--header 'Content-Type: application/json' \
--data '{
    "model": "llama2-7b-chat-v2",
    "input":{
        "messages":[
            {"content":"Where is the capital of Zhejiang?","role":"user"},
            {"content":"Thank you for asking! The capital of Zhejiang is Hangzhou.","role":"assistant"},
            {"content":"What are the interesting places there?","role":"user"}
        ]
    }
}'