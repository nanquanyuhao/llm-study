from dashscope import MultiModalConversation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_local_file():
    """Sample of use local file.
       linux&mac file schema: file:///home/images/test.png
       windows file schema: file://D:/images/abc.png
    """
    local_file_path1 = 'file://D:/code/github/llm-study/dashscope/03_model_list/01_qwen/02_qwen_vl/02_api/images/doctor.jpeg'
    local_file_path2 = 'file://D:/code/github/llm-study/dashscope/03_model_list/01_qwen/02_qwen_vl/02_api/images/weixin_room.jpg'
    
    messages = [{
        'role': 'system',
        'content': [{
            'text': 'You are a helpful assistant.'
        }]
    }, {
        'role':
        'user',
        # 比较奇怪的是，其只分析一张图，并且分析哪张图并没有摸到规律
        'content': [
            {
                'image': local_file_path1
            },
            {
                'image': local_file_path2
            },
            {
                'text': '图片里有什么东西?'
            },
        ]
    }]
    response = MultiModalConversation.call(model='qwen-vl-plus', messages=messages, api_key=api_key)
    print(response)


if __name__ == '__main__':
    call_with_local_file()