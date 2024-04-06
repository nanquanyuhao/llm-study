# 目前没有权限，需要申请开通
# 请求示例
curl --location --request POST 'https://dashscope.aliyuncs.com/api/v1/services/vision/facedetection/detect' \
--header 'Authorization: Bearer <your-dashscope-api-key>' \
--header 'Content-Type: application/json' \
--data '{
  "model": "facechain-facedetect",
  "input": {
    "images": [
      "http://finetune-swap-wulanchabu.oss-cn-wulanchabu.aliyuncs.com/zhicheng/tmp/1E1D5AFA-3C3A-4B6F-ABD6-8742CA983C42.png",
      "http://finetune-swap-wulanchabu.oss-cn-wulanchabu.aliyuncs.com/zhicheng/tmp/3.JPG",
      "http://finetune-swap-wulanchabu.oss-cn-wulanchabu.aliyuncs.com/zhicheng/tmp/F2EA3984-6EE2-44CD-928F-109B7276BCB6.png"
    ]
  },
  "parameters": {
  }
}'