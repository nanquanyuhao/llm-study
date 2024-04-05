from dashscope import MultiModalConversation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

'''
其实只是流式输出
'''
def simple_multimodal_conversation_call():
    """Simple single round multimodal conversation call.
    """
    messages = [
        {
            "role": "user",
            "content": [
                {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"},
                {"text": "这是什么?"}
            ]
        }
    ]
    responses = MultiModalConversation.call(model='qwen-vl-plus',
                                           messages=messages,
                                           api_key=api_key,
                                           stream=True)
    for response in responses:
        print(response)


if __name__ == '__main__':
    simple_multimodal_conversation_call()