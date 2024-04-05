from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

'''
上传文件

会报错，实际只有花钱升级为开发者 Pro 解决：
zhipuai.core._errors.APIStatusError: 
Error code: 434, with error text {"error":{"code":"1623","message":"没有上传文件权限，请 联系客服开放"}}
'''
client = ZhipuAI(api_key=api_key)
result = client.files.create(
    file=open("08_file_managment\data.jsonl", "rb"),
    purpose="fine-tune"
)
print(result.id)