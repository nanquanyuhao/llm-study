# 作业提交接口调用
curl --location --request POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/wordart/semantic' \
--header 'X-DashScope-Async: enable' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--data '{
    "model": "wordart-semantic",
    "input": {
        "text": "文字创意",
        "prompt": "水果，蔬菜，温暖的色彩空间"
    },
    "parameters": {
        "steps": 80,
        "n": 2,
        "output_image_ratio": "1024x1024",
        "font_name": "dongfangdakai"
    }
}'

# 作业任务状态查询和结果获取接口
curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/15319a49-8221-409b-9a30-46a7c82b8a41