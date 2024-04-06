# 文字生成示例
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/anytext/generation' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-anytext-v1",
    "input": {
        "prompt": "一只浣熊站在黑板前，上面写着“深度学习”",
        "mask_image_url": "http://public-vigen-video.oss-cn-shanghai.aliyuncs.com/yuxiang.tyx/test_anytext/gen1.png"
    },
    "parameters": {
       "seed": 81808278
    }
}'

curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/8bca6512-53b8-4671-a988-c8e6d8711b9c

# 文字编辑示例
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/anytext/generation' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-anytext-v1",
    "input": {
        "prompt": "精美的书法作品，上面写着“给” “我” “饭” “钱”",
        "mask_image_url": "http://public-vigen-video.oss-cn-shanghai.aliyuncs.com/yuxiang.tyx/test_anytext/edit10.png",
        "base_image_url": "http://public-vigen-video.oss-cn-shanghai.aliyuncs.com/yuxiang.tyx/test_anytext/ref10.jpg"
    },
    "parameters": {
       "seed": 98053044
    }
}'

curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/d18f8b05-8f77-4ae2-997f-883ec4c998e9