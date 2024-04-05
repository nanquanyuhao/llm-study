from dashscope import MultiModalConversation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

def simple_multimodal_conversation_call():
    """Simple single round multimodal conversation call.
    """
    messages = [
        {
            "role": "user",
            "content": [
                {"audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/2channel_16K.wav"},
                {"text": "这段音频在说什么?"}
            ]
        }
    ]
    responses = MultiModalConversation.call(model='qwen-audio-turbo',
                                           messages=messages,
                                           api_key=api_key,
                                           stream=True)
    for response in responses:
        print(response)


if __name__ == '__main__':
    simple_multimodal_conversation_call()