import os
import qianfan
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

chat_comp = qianfan.ChatCompletion()

# 调用默认模型，ERNIE-Lite-8K-0922（即ERNIE-Bot-turbo）
resp = chat_comp.do(messages=[{
    "role": "user",
    "content": "介绍下千帆大模型平台"
}])

print(resp)
# 只打印一下返回的文字内容
print(resp['body']['result'])
print(resp.body.get('result'))