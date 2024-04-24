import os

import dashscope
from dashscope import TextEmbedding

from dashvector import Client, Doc
from dotenv import load_dotenv
import os

load_dotenv()

path = 'dashscope/05_practice/02_dash_vector_x/CEC-Corpus/raw corpus/allSourceText'

def prepare_data(path, batch_size=25):
    batch_docs = []
    for file in os.listdir(path):
        with open(path + '/' + file, 'r', encoding='utf-8') as f:
            batch_docs.append(f.read())
            if len(batch_docs) == batch_size:
                yield batch_docs
                batch_docs = []

    if batch_docs:
        yield batch_docs


def generate_embeddings(news):
    rsp = TextEmbedding.call(
        model=TextEmbedding.Models.text_embedding_v1,
        input=news
    )
    embeddings = [record['embedding'] for record in rsp.output['embeddings']]
    return embeddings if isinstance(news, list) else embeddings[0]


if __name__ == '__main__':
    dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')
    
    # 初始化 dashvector client
    client = Client(
      api_key=os.getenv('DASHVECTOR_API_KEY'),
      endpoint=os.getenv('DASHVECTOR_CLUSTER_ENDPOINT')
    )

    # 创建集合：指定集合名称和向量维度, text_embedding_v1 模型产生的向量统一为 1536 维
    rsp = client.create('news_embedings', 1536)
    assert rsp

    # 加载语料
    id = 0
    collection = client.get('news_embedings')
    for news in list(prepare_data(path)):
        ids = [id + i for i, _ in enumerate(news)]
        id += len(news)
        
        vectors = generate_embeddings(news)
        # 写入 dashvector 构建索引
        rsp = collection.upsert(
            [
                Doc(id=str(id), vector=vector, fields={"raw": doc})
                for id, vector, doc in zip(ids, vectors, news)
            ]
        )
        assert rsp