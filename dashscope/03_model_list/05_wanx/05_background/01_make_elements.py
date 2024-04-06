from PIL import Image
from controlnet_aux.processor import Processor

hed_processor = Processor('softedge_hed')
name = 'D:/code/github/llm-study/dashscope/03_model_list/05_wanx/05_background/images/football.jpg'

'''报错情况
    分析报错来看，会连接 huggingface.co 网站进行交互，所以失败了
'''
def make_elements(name):
    img=Image.open(name)
    r,g,b,a=img.split()
    img=img.convert('RGB')
    hed_img = hed_processor(img, to_pil=True).resize(img.size).convert('RGB')
    hed_img.putalpha(a)
    hed_img.save('result.png')

make_elements(name)