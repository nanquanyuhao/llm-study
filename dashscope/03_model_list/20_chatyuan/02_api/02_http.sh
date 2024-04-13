# 提交接口调用
# 权限未开通，报错：{"code":"AccessDenied","message":"Access denied.","request_id":"b1aa0b1f-4269-9230-b381-834ded89b7be"}
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "chatyuan-large-v2",
    "input": {
        "prompt": "用户:帮我写个请假条,我因为感冒不舒服,需要请假1天,请领导批准\\n小元"
    },
    "parameters":{
    }
}'