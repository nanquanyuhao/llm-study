import os
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

from qianfan.resources.tools import tokenizer

text = "这是1段text(混合中英文）"
token_cnt = tokenizer.Tokenizer().count_tokens(
    text=text,
    mode='remote',
    model="ernie-bot-4"
)
print(token_cnt)