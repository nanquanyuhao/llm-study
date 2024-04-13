# 权限需要申请，否则报 {"code":"AccessDenied","message":"Access denied.","request_id":"1caa373d-3caa-9fce-8e70-6c5fc7170f62"}
# 提交接口调用
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "ziya-llama-13b-v1",
    "input": {
        "prompt": "<human>:帮我写一份去西安的旅游计划\n<bot>:"
    },
    "parameters":{
    }
}'