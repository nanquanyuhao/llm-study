# 提交接口调用
# 未开通权限报错：{"code":"AccessDenied","message":"Access denied.","request_id":"27a85b3d-fa90-90ec-b764-011da7849c00"}
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "billa-7b-sft-v1",
    "input": {
        "prompt": "Human: Write a Python function that checks if a given number is even or odd.\nAssistant: "
    },
    "parameters":{
    }
}'