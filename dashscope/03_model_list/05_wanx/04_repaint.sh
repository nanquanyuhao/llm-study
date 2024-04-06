# 请求示例，想要生成的风格化类型索引：
# 0 复古漫画
# 1 3D童话
# 2 二次元
# 3 小清新
# 4 未来科技
# 5 国画古风
# 6 将军百战
# 7 炫彩卡通
# 8 清雅国风
# 9 喜迎新年
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/image-generation/generation' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-style-repaint-v1",
    "input": {
        "image_url": "https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/public/dashscope/test.png",
        # 
        "style_index": 3
    }
}'

# 作业任务状态查询和结果获取接口
curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/941820ee-fb00-46b7-a330-e3e5e8d88150