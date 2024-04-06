# 作业提交接口调用
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/embeddings/multimodal-embedding/multimodal-embedding' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "multimodal-embedding-one-peace-v1",
    "input": {
        "contents": [ 
             {
                 "image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/the_starry_night.jpg", 
                 "factor": "5" 
              },
              {
                 "text": "what is your name",
                  "factor": "0.5"
              },
              {
                 "audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/cow.flac"
              }
        ]
    },
    "parameters": {
    		"auto_truncation": true
    }
}'