# 请求示例
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/image-generation/generation' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-style-cosplay-v1",
    "input": {
        "model_index": 1,
        "face_image_url": "https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/public/dashscope/test.png",
        "template_image_url": "https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/public/dashscope/test.png"
    }
}'

# 作业任务状态查询和结果获取接口
curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/9f3ee24b-73ab-4aea-9f54-730d6fb1fe61