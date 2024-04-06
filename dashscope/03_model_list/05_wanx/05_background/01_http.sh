# 请求示例
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/background-generation/generation/' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-background-generation-v2",
    "input": {
        "base_image_url": "https://vision-poster.oss-cn-shanghai.aliyuncs.com/lllcho.lc/data/test_data/images/main_images/new_main_img/a.png",
        "ref_image_url": "https://vision-poster.oss-cn-shanghai.aliyuncs.com/lllcho.lc/data/test_data/images/ref_images/d1faf4f26c8c4ea798d043a8bf3784bb_2.png",
        "ref_prompt": "放在布满苔藓的土地上，被蕨类植物叶片包围，背景是茂盛的植被，丰富的光影细节",
        "reference_edge": {
            "foreground_edge": [
                "https://vision-poster.oss-cn-shanghai.aliyuncs.com/lllcho.lc/data/test_data/images/huaban_soft_edge/6cdd13941cef1b11d885aea1717b983ae566b8efc9094-vcsvxa_fw658webp.png"
            ]
        }
    },
    "parameters": {
        "n": 4,
        "noise_level": 300,
        "ref_prompt_weight": 0.5,
        "scene_type": "GENERAL"
    }
}'

# 作业任务状态查询和结果获取接口
curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/8342a52f-fb22-471b-8396-a8a0479cf28d