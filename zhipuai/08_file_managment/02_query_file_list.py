from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

client = ZhipuAI(api_key=api_key)
# 以下返回的内容没有东西
client.files.list()