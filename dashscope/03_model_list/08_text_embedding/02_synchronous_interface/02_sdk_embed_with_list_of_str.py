from typing import Generator, List
import dashscope
from http import HTTPStatus
from dotenv import load_dotenv
import os

load_dotenv()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

# 最多支持25条，每条最长支持2048tokens
DASHSCOPE_MAX_BATCH_SIZE = 25

def batched(inputs: List,
            batch_size: int = DASHSCOPE_MAX_BATCH_SIZE) -> Generator[List, None, None]:
    for i in range(0, len(inputs), batch_size):
        yield inputs[i:i + batch_size]


def embed_with_list_of_str(inputs: List):
    result = None  # merge the results.
    batch_counter = 0
    for batch in batched(inputs):
        resp = dashscope.TextEmbedding.call(
            model=dashscope.TextEmbedding.Models.text_embedding_v1,
            input=batch)
        if resp.status_code == HTTPStatus.OK:
            if result is None:
                result = resp
            else:
                for emb in resp.output['embeddings']:
                    emb['text_index'] += batch_counter
                    result.output['embeddings'].append(emb)
                result.usage['total_tokens'] += resp.usage['total_tokens']
        else:
            print(resp)
        batch_counter += len(batch)
    print(result)


if __name__ == '__main__':
    inputs = ['风急天高猿啸哀', '渚清沙白鸟飞回', '无边落木萧萧下', '不尽长江滚滚来']
    embed_with_list_of_str(inputs)