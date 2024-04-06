from dashscope import BatchTextEmbedding
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def call():
    result = BatchTextEmbedding.call(BatchTextEmbedding.Models.text_embedding_async_v1,
                                     url="https://modelscope.oss-cn-beijing.aliyuncs.com/resource/text_embedding_file.txt",
                                     api_key=api_key,
                                     text_type="document")
    print(result)


if __name__ == '__main__':
    call()