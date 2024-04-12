# 提交接口调用
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/nlp/nlu/understanding' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "opennlu-v1",
    "input":{
        "sentence":"老师今天表扬我了",
        "task": "classification",
        "labels":"积极，消极"
    },
    "parameters": {

    }
}'