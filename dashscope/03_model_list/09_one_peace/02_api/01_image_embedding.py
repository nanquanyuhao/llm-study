from dashscope import MultiModalEmbedding
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def image_embedding():
    input = [{'image': 'https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png'},
             ]
    result = MultiModalEmbedding.call(model=MultiModalEmbedding.Models.multimodal_embedding_one_peace_v1,
                                      input=input,
                                      api_key=api_key,
                                      auto_truncation=True)
    print(result)


if __name__ == '__main__':
    image_embedding()