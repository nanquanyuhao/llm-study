import os
import qianfan
from qianfan.resources import Reranker
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

# 默认模型
r = Reranker()

# 使用指定reranker模型，固定值为bce-reranker-base_v1
# r = Reranker(model="bce-reranker-base_v1") 

res = r.do("北京的天气", ["北京今天12.5度，北风，阴天", "北京美食很多"])
print(res.body)