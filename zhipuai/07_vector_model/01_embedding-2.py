from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

client = ZhipuAI(api_key=api_key) 
response = client.embeddings.create(
    model="embedding-2",
    input="你好",
)

print(response)