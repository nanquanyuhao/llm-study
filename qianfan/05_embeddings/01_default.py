# Embedding 基础功能

import os
import qianfan
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

emb = qianfan.Embedding()

resp = emb.do(texts=[  # 省略 model 时则调用默认模型 Embedding-V1
    "世界上最高的山"
])
print(resp['data'][0]['embedding'])