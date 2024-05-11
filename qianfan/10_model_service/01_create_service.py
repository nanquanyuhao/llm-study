import os
from qianfan import resources
from qianfan.resources.console.consts import DeployPoolType
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

# 创建服务
svc = resources.Service.create(
    model_id=123,
    model_version_id=456,
    name="sdk_test",
    uri="svc_uri",
    replicas=1,
    pool_type=DeployPoolType.PrivateResource,
)
print(svc)