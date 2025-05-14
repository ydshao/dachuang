from dscribe.descriptors import SOAP
from 

# 创建SOAP描述符
soap = SOAP(
    species=["H", "O"],
    periodic=False,
    rcut=5.0,
    nmax=8,
    lmax=6,
)

# 计算SOAP描述符(这本身就是"最后一层"输出)
soap_descriptors = soap.create(system)

from tensorflow.keras.models import Model

# 假设已有一个训练好的模型
base_model = ...  # 您的预训练模型

# 创建一个新模型，输出最后一层
descriptor_model = Model(
    inputs=base_model.input,
    outputs=base_model.layers[-1].output
)

# 获取描述符
descriptors = descriptor_model.predict(input_data)
