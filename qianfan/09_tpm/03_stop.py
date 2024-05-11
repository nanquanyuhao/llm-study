import os
from qianfan.resources.console.charge import Charge
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

model = "ernie-4.0-8k"
instance_id = 'tpm-40PAcd2s'
resp = Charge.stop(model, instance_id)
print(resp)