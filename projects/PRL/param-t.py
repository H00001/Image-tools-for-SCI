import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 读取Excel文件
# data = pd.read_excel('DATA.xlsx', sheet_name=-1)  # 读取最后一个工作表
data_reut = np.array([
[0.6278, 0.6280, 0.6304, 0.6300,0.6300] ,
[0.6623, 0.6687, 0.6702,0.6700,0.6689] ,
[0.6640, 0.6670, 0.6670,0.6670,0.6672] ,
[0.8178, 0.8189, 0.8200,0.8201,0.8200] ,

])
data_hhar = np.array([
[0.7780, 0.7760, 0.7781, 0.7770, 0.7781] ,
[0.8186, 0.8170, 0.8270, 0.8260, 0.8271] ,
[0.8900, 0.8900, 0.8900, 0.8902, 0.8888] ,
[0.8877, 0.8903, 0.8912, 0.8906, 0.8900] ,
])
data_acm = np.array([
[0.7887, 0.7888, 0.7900, 0.7900, 0.7900] ,
[0.7211, 0.7262, 0.7340, 0.7341, 0.7340] ,
[0.9247, 0.9228, 0.9300, 0.9310, 0.9309] ,
[0.9277, 0.9268, 0.9311, 0.9320, 0.9310] ,
])
data_cite = np.array([
[0.4703, 0.4736, 0.4713, 0.4703, 0.4703] ,
[0.4500, 0.4524, 0.4521, 0.4509, 0.4521] ,
[0.6212, 0.6220, 0.6208, 0.6102, 0.6208] ,
[0.7140, 0.7190, 0.7180, 0.7180, 0.7180] ,
])
data_dblp = np.array([
[0.4813, 0.4815, 0.4790, 0.4790, 0.4730] ,
[0.4419, 0.4436, 0.4425, 0.4413, 0.4409] ,
[0.7544, 0.7581, 0.7605, 0.7603, 0.7605] ,
[0.7718, 0.7810, 0.7710, 0.7710, 0.7760] 
])

data_aids = np.array([
[0.1918, 0.1966, 0.2004, 0.2010, 0.2010] ,
[0.1577, 0.1589, 0.1601, 0.1623, 0.1616] ,
[0.2716, 0.2744, 0.2844, 0.2833, 0.2825] ,

[0.6740, 0.6770, 0.6792, 0.6788, 0.6762] 
])


name = "reut"
data = eval("data_"+name)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

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

# i = 0.7
# 按 y 从大到小排序（保证远处的柱子先绘制）
for y, color in sorted(zip(np.unique(ypos), colors), key=lambda x: -x[0]):
    ax.bar3d(
        xpos[ypos == y], 
        ypos[ypos == y], 
        zpos[ypos == y], 
        dx, dy, dz[ypos == y], 
        color=color, 
        edgecolor='black',
        alpha=1,  # 远处的柱子更透明
        zsort='average'  # 尝试不同的 zsort 选项
    )
    # i += 0.1  # 近处的柱子更不透明
# 设置坐标轴标签
ax.set_xticks(np.arange(data.shape[1])+ 0.5)  # 设置刻度位置
ax.set_xticklabels(['1e-2', '1e-5', '1e-8', '1e-11', '1e-14'])
ax.set_yticks(np.arange(data.shape[0])+0.7)
ax.set_yticklabels([ 'ARI', 'NMI', 'F1','ACC'])
ax.set_xlabel('λ',fontsize=14)
# ax.set_ylabel('Metrics')
ax.set_zlabel('Score', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)  # X 和 Y 轴主刻度字体大小为 12

# 设置Z轴限制
ax.set_zlim(0, 1)
ax.grid(False)
ax.view_init(elev=28, azim=-45)  # 自定义视角角度（可以调试这两个值）

plt.tight_layout()
# 28 , -33
plt.savefig(name+"abl.png", dpi=300)
# plt.show()
