import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 数据
labels = ['K=1', 'K=3', 'K=5', 'K=10']
metrics = ['ACC', 'NMI', 'ARI', 'F1']

Letter_data = np.array([
    [87.4, 89.2, 88.5, 87.5],  # ACC
    [83.2, 84.3, 83.2, 82.5],  # NMI
    [78.7, 79.2, 78.6, 77.8],  # ARI
    [86.4, 90.0, 89.8, 84.4],  # F1
])

COLLAB_data = np.array([
    [81.9, 83.3, 82.6, 82.3],  # ACC
    [61.2, 64.0, 63.2, 61.7],  # NMI
    [62.1, 66.2, 64.3, 63.1],  # ARI
    [67.7, 70.0, 69.2, 68.5],  # F1
])

# 颜色方案
colors = ['#b0d992', '#fccccb', '#bdb5e1', '#99b9e9']

# 3D 柱状图参数
dx, dy = 0.75, 0.75  # 柱体尺寸
zpos = np.zeros_like(Letter_data.flatten())  # Z轴起始点

# 画图
fig = plt.figure(figsize=(14, 6))

# 画 Letter 数据集
ax1 = fig.add_subplot(121, projection='3d')
xpos, ypos = np.meshgrid(np.arange(Letter_data.shape[1]), np.arange(Letter_data.shape[0])) 
xpos, ypos = xpos.flatten(), ypos.flatten()
dz = Letter_data.flatten()

i = 1
for y, color in zip(np.unique(ypos), colors):
    ax1.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], 
              color=color, edgecolor='black', alpha=i, zsort='average')
    i -= 0.15

ax1.set_xticks(np.arange(len(labels)) + 0.5)
ax1.set_xticklabels(labels, fontsize=14)
ax1.set_yticks(np.arange(len(metrics)) + 0.5)
ax1.set_yticklabels(metrics, fontsize=16)
ax1.set_zlabel('Score (%)', fontsize=16)
ax1.zaxis.set_tick_params(labelsize=16)  

# ax1.set_title('Letter Dataset', fontsize=14)
ax1.view_init(elev=20, azim=-35)  # 设置3D视角

# 画 COLLAB 数据集
ax2 = fig.add_subplot(122, projection='3d')
xpos, ypos = np.meshgrid(np.arange(COLLAB_data.shape[1]), np.arange(COLLAB_data.shape[0])) 
xpos, ypos = xpos.flatten(), ypos.flatten()
dz = COLLAB_data.flatten()

i = 1
for y, color in zip(np.unique(ypos), colors):
    ax2.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], 
              color=color, edgecolor='black', alpha=i, zsort='average')
    i -= 0.15

ax2.set_xticks(np.arange(len(labels)) + 0.5)
ax2.set_xticklabels(labels, fontsize=12)
ax2.set_yticks(np.arange(len(metrics)) + 0.5)
ax2.set_yticklabels(metrics, fontsize=16)
ax2.set_zlabel('Score (%)', fontsize=16)
ax2.zaxis.set_tick_params(labelsize=16)  

ax1.set_title('HHAR', fontsize=18, y=-0.05)  # 增大 y 让标题稍微上移
ax2.set_title('REUT', fontsize=18, y=-0.05)  # 增大 y 让标题稍微上移

ax1.view_init(elev=25, azim=150)  # 设置3D视角
ax2.view_init(elev=25, azim=150)  # 设置3D视角

plt.subplots_adjust(left=0.1, right=0.9, top=1, bottom=0.1, wspace=0.100, hspace=0.0)
# plt.tight_layout()
plt.tight_layout(rect=[0, 0.00, 1, 1])

# plt.show()
plt.savefig("./NPL/k-hyper-0.png", dpi=600)
 