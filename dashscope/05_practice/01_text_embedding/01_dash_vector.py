from title import prepare_data
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

path = 'dashscope/05_practice/01_text_embedding/QBQTC/dataset/train.json'

# 指定集合名称和向量维度
rsp = client.create('sample', 1536)
assert rsp

collection = client.get('sample')
assert collection

batch_size = 10
for docs in list(prepare_data(path, batch_size)):
    # 批量 embedding
    embeddings = generate_embeddings([doc['title'] for doc in docs])

    # 批量写入数据
    rsp = collection.insert(
        [
            Doc(id=str(doc['id']), vector=embedding, fields={"title": doc['title']}) 
            for doc, embedding in zip(docs, embeddings)
        ]
    )
    assert rsp