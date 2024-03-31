curl --location 'https://open.bigmodel.cn/api/paas/v4/chat/completions' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInNpZ25fdHlwZSI6IlNJR04iLCJ0eXAiOiJKV1QifQ.eyJhcGlfa2V5IjoiNjVkMDNjN2MxYjIxNGY3YTE2OGQ3ZGQ5Y2JiYjU5MjIiLCJleHAiOjE3MTE4NzA5NzYxMDgsInRpbWVzdGFtcCI6MTcxMTg3MDk2MTEwOH0.QWbwWJiM4zyupQ5pVDQnaxNgV6kdxoZMkvMH2YDEaMM' \
--header 'Content-Type: application/json' \
--data '{
    "model": "glm-4",
    "messages": [
        {
            "role": "user",
            "content": "你好"
        }
    ]
}'