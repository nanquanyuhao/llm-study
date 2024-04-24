import dashscope
from dashscope import TextEmbedding
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')


def generate_embeddings(text):
    rsp = TextEmbedding.call(model=TextEmbedding.Models.text_embedding_v1,
                             input=text)
    
    embeddings = [record['embedding'] for record in rsp.output['embeddings']]
    return embeddings if isinstance(text, list) else embeddings[0]


# 查看下embedding向量的维数，后面使用 DashVector 检索服务时会用到，目前是1536
print(len(generate_embeddings('hello')))