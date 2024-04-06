from http import HTTPStatus
from dashscope import TextEmbedding
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

local_path='D:/code/github/llm-study/dashscope/03_model_list/08_text_embedding/02_synchronous_interface'

def embed_with_file_content():
    # 文件中最多支持25条，每条最长支持2048tokens
    with open('%s/tests_to_embedding.txt' % (local_path), 'r', encoding='utf-8') as f:
        resp = TextEmbedding.call(
            model=TextEmbedding.Models.text_embedding_v1,
            api_key=api_key,
            input=f)
        if resp.status_code == HTTPStatus.OK:
            print(resp)
        else:
            print(resp)


if __name__ == '__main__':
    embed_with_file_content()