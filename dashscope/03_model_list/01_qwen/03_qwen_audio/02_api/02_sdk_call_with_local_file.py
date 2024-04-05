from dashscope import MultiModalConversation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

'''情况说明
    目前来看，方法整体有问题，串了其他人的资源
'''
def call_with_local_file():
    """Sample of use local file.
       linux&mac file schema: file:///home/audios/test.wav
       windows file schema: file://D:/audios/abc.wav
    """
    local_file_path1 = 'file://D:/code/github/llm-study/dashscope/03_model_list/01_qwen/03_qwen_audio/02_api/audios/healing_words.wav'
    local_file_path2 = 'file://D:/code/github/llm-study/dashscope/03_model_list/01_qwen/03_qwen_audio/02_api/audios/model.wav'
    messages = [{
        'role': 'system',
        'content': [{
            'text': 'You are a helpful assistant.'
        }]
    }, {
        'role':
        'user',
        'content': [
            {
                'audio': local_file_path1
            },
            {
                'audio': local_file_path2
            },
            {
                'text': '音频里在说什么?'
            },
        ]
    }]
    response = MultiModalConversation.call(model='qwen-audio-turbo', messages=messages, api_key=api_key)
    print(response)


if __name__ == '__main__':
    call_with_local_file()