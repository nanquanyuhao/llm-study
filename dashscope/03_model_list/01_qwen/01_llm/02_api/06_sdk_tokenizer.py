from dashscope import get_tokenizer

# 获取Tokenizer，目前只支持千问系列模型
tokenizer = get_tokenizer('qwen-turbo')

input_str = 'You are a helpful assistant.'

# convert string to token ids
tokens = tokenizer.encode(input_str)
print(tokens)
print('There are %s tokens' % len(tokens))

# convert token ids to string
decoded_str = tokenizer.decode(tokens)
print(decoded_str)