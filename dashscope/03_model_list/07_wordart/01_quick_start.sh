curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/wordart/texture' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-DashScope-DataInspection: enable' \
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