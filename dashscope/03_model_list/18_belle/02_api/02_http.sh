# 提交接口调用
# 权限不足，报错：{"code":"AccessDenied","message":"Access denied.","request_id":"92fe8e31-3390-9208-ba2f-95b49e9e2859"}
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "belle-llama-13b-2m-v1",
    "input": {
        "prompt": "Human:你好\n\nAssistant:"
    },
    "parameters":{
    }
}'