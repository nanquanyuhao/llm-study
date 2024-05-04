import os
import qianfan
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

chat_comp = qianfan.ChatCompletion()

# 下面是一个与用户对话的例子
msgs = qianfan.Messages()
while True:
    msgs.append(input("输入："))         # 增加用户输入
    resp = chat_comp.do(messages=msgs)
    print(resp)                  # 模型的输出
    msgs.append(resp)            # 追加模型输出