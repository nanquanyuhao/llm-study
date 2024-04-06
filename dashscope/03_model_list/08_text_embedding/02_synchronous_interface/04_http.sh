curl --location 'https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding/text-embedding' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "text-embedding-v1",
    "input": {
        "texts": [
        "风急天高猿啸哀",
        "渚清沙白鸟飞回", 
        "无边落木萧萧下", 
        "不尽长江滚滚来"
        ]
    },
    "parameters": {
    		"text_type": "query"
    }
}'