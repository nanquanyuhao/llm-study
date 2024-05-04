import os
import qianfan
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

comp = qianfan.Completion()

# 使用自行发布的模型，目前还未进行定制，定制了再弄
resp = comp.do(endpoint="your_custom_endpoint", prompt="你好")

# 可以通过resp["body"]获取接口返回的内容
print(resp)