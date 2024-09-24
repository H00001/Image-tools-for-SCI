import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 读取Excel文件
# data = pd.read_excel('DATA.xlsx', sheet_name=-1)  # 读取最后一个工作表
data_acm = np.array([
[0.6522, 0.7477, 0.664, 0.7104, 0.5489] ,
[0.6923, 0.8051, 0.6968, 0.77, 0.6144] ,
[0.8793, 0.9313, 0.8853, 0.9168, 0.8537] ,
[0.8833, 0.9309, 0.886, 0.917, 0.8539] ,
])
data_reut = np.array([
[0.599, 0.6318, 0.538, 0.4049, 0.3464] ,
[0.6008, 0.6628, 0.5499, 0.4437, 0.2496] ,
[0.7663, 0.7907, 0.7484, 0.6708, 0.5719] ,
[0.8016, 0.8312, 0.7821, 0.7226, 0.6239] ,
])
data_usps = np.array([
[0.8313, 0.8249, 0.7555, 0.4242, 0.3811] ,
[0.7676, 0.772, 0.6756, 0.2553, 0.237] ,
[0.7936, 0.7994, 0.7309, 0.4078, 0.3757] ,
[0.8086, 0.8313, 0.7804, 0.4233, 0.3924] ,
])
data_hhar = np.array([
[0.7046, 0.8367, 0.8079, 0.6995, 0.4489] ,
[0.6101, 0.7792, 0.7354, 0.6102, 0.3675] ,
[0.6883, 0.8837, 0.8285, 0.6588, 0.4487] ,
[0.7192, 0.88, 0.8346, 0.6944, 0.4881] ,
])
data_cite = np.array([
[0.4422, 0.4471, 0.4347, 0.4018, 0.3567] ,
[0.4737, 0.4799, 0.4436, 0.3923, 0.3512] ,
[0.6278, 0.6329, 0.6216, 0.6261, 0.5983] ,
[0.7121, 0.7166, 0.6751, 0.6438, 0.6261] ,
])


data = data_acm
plt.rcParams['font.sans-serif'] = ['Times New Roman']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0])) 
xpos = xpos.flatten()  
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
# the width and height of block
dx = 0.85
dy = 0.85
dz = data.flatten()

# modify below if you want to change the color
colors = ['#b0d992', '#fccccb', '#bdb5e1', '#99b9e9']

i = 0.7
for y, color in zip(np.unique(ypos), colors):
    ax.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average',edgecolor='black',alpha = i)
    i+=0.1

# 绘制3D条形图
# ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=plt.cm.viridis(dz/float(max(dz))), zsort='average')

# 设置坐标轴标签
ax.set_xticks(np.arange(data.shape[1])+ 0.5)  # 设置刻度位置
ax.set_xticklabels(['0.01', '0.1', '1', '10', '100'])
ax.set_yticks(np.arange(data.shape[0])+0.7)
ax.set_yticklabels(['NMI', 'ARI', 'F1','ACC'])
ax.set_xlabel('λ')
ax.set_ylabel('Metrics')
ax.set_zlabel('Score')

# 设置Z轴限制
ax.set_zlim(0, 1)
ax.grid(False)

plt.show()
