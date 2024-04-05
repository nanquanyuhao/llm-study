# 同样没有上传文件的权限，报错如下：
# {"error":{"code":"1623","message":"没有上传文件权限，请联系客服开放"}}
curl 'https://open.bigmodel.cn/api/paas/v4/files' \
-X POST \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInNpZ25fdHlwZSI6IlNJR04iLCJ0eXAiOiJKV1QifQ.eyJhcGlfa2V5IjoiNjVkMDNjN2MxYjIxNGY3YTE2OGQ3ZGQ5Y2JiYjU5MjIiLCJleHAiOjE3MTE4OTQ1OTYzNDcsInRpbWVzdGFtcCI6MTcxMTg5NDU4MTM0N30.F1eZUhdgxGWsORqKralsx793alPOKzP1UUaQWYvCO3M' \
--form 'file=@"08_file_managment\data.jsonl"' \
--form 'purpose="fine-tune"'