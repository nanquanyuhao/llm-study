
from dashvector import Client

from embedding import generate_embeddings
from dotenv import load_dotenv
import os

load_dotenv()

def search_relevant_news(question):
    # 初始化 dashvector client
    client = Client(
      api_key=os.getenv('DASHVECTOR_API_KEY'),
      endpoint=os.getenv('DASHVECTOR_CLUSTER_ENDPOINT')
    )

    # 获取刚刚存入的集合
    collection = client.get('news_embedings')
    assert collection

    # 向量检索：指定 topk = 1 
    rsp = collection.query(generate_embeddings(question), output_fields=['raw'],
                           topk=1)
    assert rsp
    return rsp.output[0].fields['raw']