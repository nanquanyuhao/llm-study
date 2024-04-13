# 提交任务接口调用
# 请求示例（SSE关闭）
# 未开通权限报错：{"code":"AccessDenied","message":"Access denied.","request_id":"59ac1e09-9b5f-96c0-bfd8-d970bb0e3d0e"}
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "dolly-12b-v2",
    "input": {
        "prompt": "就当前的海洋污染的情况，写一份限塑的倡议书提纲，需要有理有据地号召大家克制地使用塑料制品"
    },
    "parameters": {
    }
}'

# 请求示例（SSE开启），权限未开通报错如下
# id:1
# event:error
# :HTTP_STATUS/403
# data:{"code":"AccessDenied","message":"Access denied.","request_id":"3b10c53e-0507-9f27-b3df-5dcbb3a0f283"}
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'X-DashScope-SSE: enable' \
--data '{
    "model": "dolly-12b-v2",
    "input": {
        "prompt": "就当前的海洋污染的情况，写一份限塑的倡议书提纲，需要有理有据地号召大家克制地使用塑料制品"
    },
    "parameters": {
    }
}'