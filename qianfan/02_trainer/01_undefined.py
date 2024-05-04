import os 
import qianfan
from dotenv import load_dotenv

load_dotenv()
# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
print(os.environ["QIANFAN_ACCESS_KEY"])
print(os.environ["QIANFAN_SECRET_KEY"])


# 如果希望打印过程日志，通过调用enable_log(logging.INFO)启用打印日志功能
#from qianfan.utils import enable_log
#import logging
#enable_log(logging.INFO)  # 设置打印日志的最低级别

from qianfan.dataset import Dataset
from qianfan.trainer import LLMFinetune

'''
    目前没有数据集，以后再说
'''
# 加载千帆平台上的数据集，is_download_to_local=False表示不下载数据集到本地，而是直接使用
ds: Dataset = Dataset.load(qianfan_dataset_id="your_dataset_id", is_download_to_local=False)

# 新建trainer LLMFinetune，需最少传入train_type和dataset
# 注意fine-tune任务需要指定的数据集类型要求为有标注的非排序对话数据集。
trainer = LLMFinetune(
    train_type="ERNIE-xx",
    dataset=ds, 
)

trainer.run()

# 如果突发断电或者任务停止，可以使用resume函数重启任务
# trainer.resume()