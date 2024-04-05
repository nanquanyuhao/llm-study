from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

'''
注意：每次调用需要 0.25 元
'''
client = ZhipuAI(api_key=api_key)
response = client.images.generations(
    model="cogview-3", 
    prompt="一辆在四驱车专用跑道上疾驰的三角箭四驱车",
)
print(response.data[0].url)
print(str(response))