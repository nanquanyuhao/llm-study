# 作业提交接口调用
# 图片输入
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/wordart/texture' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "model": "wordart-texture",
    "input": {
        "image": 
        {
            "image_url": "https://dmshared.oss-cn-hangzhou.aliyuncs.com/junyan.hjy/wordart/lcy/example.png"
        },
        "prompt": "水果，蔬菜，温暖的色彩空间",
        "texture_style": "material"
    },
    "parameters": 
    {
        "image_short_size": 704,
        "n": 2,
        "alpha_channel": false
    }
}'

curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/7f390aeb-283c-4f93-b8a5-9a2d7537ed86


# 文字输入
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/wordart/texture' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "model": "wordart-texture",
    "input": {
        "text": 
        {
            "text_content": "文字创意",
            "font_name": "dongfangdakai",
            "output_image_ratio": "1:1"
        },
        "prompt": "水果，蔬菜，温暖的色彩空间",
        "texture_style": "material"
    },
    "parameters": 
    {
        "image_short_size": 704,
        "n": 2,
        "alpha_channel": false
    }
}'

curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/f6ca6b3f-a80f-46ce-93c1-bf2406208512