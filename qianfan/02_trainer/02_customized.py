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
from qianfan.trainer.configs import TrainConfig

'''
    目前没有数据集，以后再说
'''
# 加载千帆平台上的数据集。
# qianfan_dataset_id是数据集id，类型要求为有标注的非排序对话数据集is_download_to_local=False表示不下载数据集到本地，直接使用
ds: Dataset = Dataset.load(qianfan_dataset_id="your_dataset_id", is_download_to_local=False)

# 发起训练任务。以基础模型ERNIE-xx为例，需要指定的数据集类型要求为有标注的非排序对话数据集。
trainer = LLMFinetune(
    train_type="ERNIE-xx",
    dataset=ds,
    peft_type="LoRA",
    # 自定义训练参数
    train_config=TrainConfig(
        epochs=1, # 迭代轮次（Epoch），控制训练过程中的迭代轮数。
        # batch_size=32, # 批处理大小（BatchSize）表示在每次训练迭代中使用的样本数。较大的批处理大小可以加速训练.部分模型可能无需填写该字段
        learning_rate=0.00004, # 学习率（LearningRate）是在梯度下降的过程中更新权重时的超参数，过高会导致模型难以收敛，过低则会导致模型收敛速度过慢，
    )
)

trainer.run()

# 如果突发断电或者任务停止，可以使用resume函数重启任务
# trainer.resume()