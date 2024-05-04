import os
import qianfan
from PIL import Image
import io
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])

t2i = qianfan.Text2Image()
resp = t2i.do(prompt="A Ragdoll cat with a bowtie.", with_decode="base64")
img_data = resp["body"]["data"][0]["image"]

img = Image.open(io.BytesIO(img_data))
img.show(img)