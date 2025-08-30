import numpy as np

# 设置均值和方差
mean = 40.9  # 均值
std_dev = 1.0  # 标准差
size = 1000  # 数据点数量

# 根据均值和标准差生成数据
data = np.random.normal(loc=mean, scale=std_dev, size=size)

print()
# 打印生成的数据的前5个元素
data_rounded = np.round(data, 1)

# 打印生成的数据的前5个元素
for k in data_rounded[:10]:
    print("\multicolumn{1}{c|}{" ,k ,"}", end="&")

# # 计算生成数据的均值和标准差，验证是否符合设置的参数
# print("Generated Data Mean:", np.mean(data))
# print("Generated Data Std Dev:", np.std(data))
