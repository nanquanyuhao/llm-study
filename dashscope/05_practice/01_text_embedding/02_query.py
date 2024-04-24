from embedding import generate_embeddings
from dashvector import Client, Doc
from dotenv import load_dotenv
import os

load_dotenv()

# 初始化 DashVector client
client = Client(
  api_key=os.getenv('DASHVECTOR_API_KEY'),
  endpoint=os.getenv('DASHVECTOR_CLUSTER_ENDPOINT')
)

collection = client.get('sample')
assert collection

# 基于向量检索的语义搜索
rsp = collection.query(generate_embeddings('应届生 招聘'), output_fields=['title'])

for doc in rsp.output:
    print(f"id: {doc.id}, title: {doc.fields['title']}, score: {doc.score}")