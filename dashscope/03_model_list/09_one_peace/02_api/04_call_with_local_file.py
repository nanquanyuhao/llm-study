from dashscope import MultiModalEmbedding
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

local_file_path1 = 'file://D:/code/github/llm-study/dashscope/03_model_list/01_qwen/02_qwen_vl/02_api/images/doctor.jpeg'
local_file_path2 = 'file://D:/code/github/llm-study/dashscope/03_model_list/01_qwen/02_qwen_vl/02_api/images/weixin_room.jpg'

def call_with_local_file():
    """Sample of use local file.
       linux&mac file format: file:///home/images/test.png
       windows file format: file://D:/images/abc.png
    """
    # file path must absolute path
    input = [{'image': local_file_path1},
             {'image': local_file_path2}]
    result = MultiModalEmbedding.call(
        model=MultiModalEmbedding.Models.
        multimodal_embedding_one_peace_v1,
        input=input,
        api_key=api_key,
        auto_truncation=True)
    print(result)


if __name__ == '__main__':
    call_with_local_file()