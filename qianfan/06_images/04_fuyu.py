import os
import qianfan
import base64
from qianfan.resources import Image2Text
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

local_path = 'D:/code/github/llm-study/qianfan/06_images/temp'

# 请替换图片对应的路径地址
with open('%s/%s' % (local_path, 'image.jpg'), "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# 使用model参数
i2t = Image2Text(model="Fuyu-8B")
resp = i2t.do(prompt="分析一下图片画了什么", image=encoded_string)

print(resp["result"])