curl --location 'https://dashscope.aliyuncs.com/api/v1/tokenizer' \
--header 'Authorization: Bearer sk-36e6672ae3a343cd8b0c6430172e35ae' \
--header 'Content-Type: application/json' \
--data '{
    "model": "qwen-plus",
    "input":{
        "messages":[
            {
                "role": "user",
                "content": "北京有哪些好玩地方？"
            },
            {
                "role": "assistant",
                "content": "故宫、颐和园、天坛等都是可以去游玩的景点哦。"
            },
            {
                "role": "user",
                "content": "帮我安排一些行程"
            }
        ]
    },
    "parameters": {
    }
}'