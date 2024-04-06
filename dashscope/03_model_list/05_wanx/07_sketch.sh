# 请求示例
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/image2image/image-synthesis/' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-sketch-to-image-lite",
    "input": {
        "sketch_image_url": "https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6609471071/p743851.jpg",
        "prompt": "一棵参天大树"
    },
    "parameters": 
    {
        "size": "768*768",
        "n": 2,
        "sketch_weight": 3,
        "style": "<watercolor>",
        "sketch_extraction": false,
        "sketch_color": [
        	[0, 0, 0],
          [123, 123, 123]
    		]
    }
}'

# 作业任务状态查询和结果获取接口
curl -X GET \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
https://dashscope.aliyuncs.com/api/v1/tasks/8bbd66da-d34f-49ac-a549-bb60a363e892