import os
import qianfan
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

chat_comp = qianfan.ChatCompletion()

# 多轮对话
resp = chat_comp.do(messages=[{       # 调用默认模型，即 ERNIE-Bot-turbo
    "role": "user",
    "content": "你好"
},
{
    "role": "assistant",
    "content": "你好，请问有什么我可以帮助你的吗？"
},
{
    "role": "user",
    "content": "我在北京，周末可以去哪里玩？"
},
])
print(resp)