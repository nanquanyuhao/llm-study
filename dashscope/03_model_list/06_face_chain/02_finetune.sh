# 请求示例
curl --location 'https://dashscope.aliyuncs.com/api/v1/fine-tunes' \
--header 'Authorization: Bearer <YOUR-DASHSCOPE-API-KEY>' \
--header 'Content-Type: application/json' \
--data '{ "model":"facechain-finetune", 
"training_file_ids":[ "https://dashscope.oss-cn-beijing.aliyuncs.com/samples/fine-tune/facechain/sample1.jpg","https://dashscope.oss-cn-beijing.aliyuncs.com/samples/fine-tune/facechain/sample2.jpg","https://dashscope.oss-cn-beijing.aliyuncs.com/samples/fine-tune/facechain/sample3.jpg"],
    }'

# 检查定制任务状态接口
curl --location 'https://dashscope.aliyuncs.com/api/v1/fine-tunes/ft-202308291948-edc2' \ 
--header 'Authorization: Bearer <YOUR-DASHSCOPE-API-KEY>' \
--header 'Content-Type: application/json' 