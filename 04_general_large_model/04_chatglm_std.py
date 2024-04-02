import zhipuai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

'''
调用智谱 AI API
'''
# 填写环境变量中获取的 APIKey 信息
zhipuai.api_key = api_key
# 用于配置大模型版本，chatglm_std 已经宣布弃用日期为 2024 年 12 月 31 日
# 弃用后，会将其自动路由至新的模型 glm-3-turbo。注意需在弃用日期之前将编码更新为 glm-3-turbo，以确保服务的顺畅过渡
model = 'chatglm_std'
# model = 'glm-3-turbo'

def getText(role, content, text = []):
    # role 是指定角色，content 是 prompt 内容
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

question = getText("user", "你好")

# 请求模型
response = zhipuai.model_api.invoke(
    model=model,
    prompt=question
)
print(response)


'''
使用 LangChain 调用智谱 AI
'''
# zhipuai_model = ZhipuAILLM(model = model, temperature = 0, zhipuai_api_key = zhipuai.api_key)