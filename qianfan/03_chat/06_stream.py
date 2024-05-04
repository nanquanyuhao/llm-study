import os
import qianfan
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

chat_comp = qianfan.ChatCompletion()

resp = chat_comp.do(model="ERNIE-Bot-turbo", messages=[{
    "role": "user",
    "content": "你好"
}], stream=True)

for r in resp:
    print(r)
# 输出：
# 您好！
# 有什么我可以帮助你的吗？