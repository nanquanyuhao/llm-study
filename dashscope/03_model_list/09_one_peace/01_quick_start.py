import dashscope
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def image_call():
    input = [{'image': 'https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png'},
             ]
    result = dashscope.MultiModalEmbedding.call(model=dashscope.MultiModalEmbedding.Models.multimodal_embedding_one_peace_v1,
                                      input=input,
                                      auto_truncation=True)
    print(result)

if __name__ == '__main__':
    image_call()