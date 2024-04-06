from dashscope import MultiModalEmbedding
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def multimodal_with_factor_embedding():
    input = [{'factor': 1, 'text': '你好'},
             {'factor': 2, 'audio': 'https://dashscope.oss-cn-beijing.aliyuncs.com/audios/cow.flac'},
             {'factor': 3, 'image': 'https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png'}]
    result = MultiModalEmbedding.call(model=MultiModalEmbedding.Models.multimodal_embedding_one_peace_v1,
                                      input=input,
                                      api_key=api_key,
                                      auto_truncation=True)
    print(result)


if __name__ == '__main__':
    multimodal_with_factor_embedding()