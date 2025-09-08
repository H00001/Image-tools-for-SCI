from multiprocessing.connection import Client

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
#
# # 读取Excel文件
# # data = pd.read_excel('DATA.xlsx', sheet_name=-1)  # 读取最后一个工作表
# data_acm = np.array([
# [0.6522, 0.7477, 0.664, 0.7104, 0.5489] ,
# [0.6923, 0.8051, 0.6968, 0.77, 0.6144] ,
# [0.8793, 0.9313, 0.8853, 0.9168, 0.8537] ,
# [0.8833, 0.9309, 0.886, 0.917, 0.8539] ,
# ])
# data_reut = np.array([
# [0.599, 0.6318, 0.538, 0.4049, 0.3464] ,
# [0.6008, 0.6628, 0.5499, 0.4437, 0.2496] ,
# [0.7663, 0.7907, 0.7484, 0.6708, 0.5719] ,
# [0.8016, 0.8312, 0.7821, 0.7226, 0.6239] ,
# ])
# data_usps = np.array([
# [0.8313, 0.8249, 0.7555, 0.4242, 0.3811] ,
# [0.7676, 0.772, 0.6756, 0.2553, 0.237] ,
# [0.7936, 0.7994, 0.7309, 0.4078, 0.3757] ,
# [0.8086, 0.8313, 0.7804, 0.4233, 0.3924] ,
# ])
# data_hhar = np.array([
# [0.7046, 0.8367, 0.8079, 0.6995, 0.4489] ,
# [0.6101, 0.7792, 0.7354, 0.6102, 0.3675] ,
# [0.6883, 0.8837, 0.8285, 0.6588, 0.4487] ,
# [0.7192, 0.88, 0.8346, 0.6944, 0.4881] ,
# ])
# data_cite = np.array([
# [0.4422, 0.4471, 0.4347, 0.4018, 0.3567] ,
# [0.4737, 0.4799, 0.4436, 0.3923, 0.3512] ,
# [0.6278, 0.6329, 0.6216, 0.6261, 0.5983] ,
# [0.7121, 0.7166, 0.6751, 0.6438, 0.6261] ,
# ])
# data_CiteSeer = np.array([
# [0.1658,0.1097,0.1958,0.1557,0.1482],  # 'nmi'
# [0.1270,0.1316,0.2187,0.1318,0.1041],  # 'ari'
# [0.2608,0.2426,0.2786,0.2460,0.2731],  # 'f1'
# [0.5321,0.5882,0.6335,0.5797,0.4962]   # 'acc'
# ])#client10
# data_PubMed = np.array([
# [0.0788,0.0845,0.1196,0.0568,0.0907],  # 'nmi'
# [0.1245,0.0780,0.1592,0.0667,0.1112],  # 'ari'
# [0.3984,0.3942,0.4699,0.3720,0.4087],  # 'f1'
# [0.6200,0.6339,0.6429,0.6076,0.5853]   # 'acc'
# ])#client10
# data_Computers = np.array([
# [0.1861,0.2185,0.2529,0.1996,0.2010],  # 'nmi'
# [0.1746,0.2262,0.3040,0.2063,0.2084],  # 'ari'
# [0.1873,0.2188,0.2509,0.2277,0.2290],  # 'f1'
# [0.6857,0.6423,0.7307,0.6556,0.6873]   # 'acc'
# ])#client10
# data_Photo = np.array([
# [0.2704,0.3017,0.3222,0.3064,0.3092],  # 'f1'
# [0.3055,0.3832,0.4040,0.3548,0.3611],  # 'nmi'
# [0.3449,0.4025,0.4777,0.4520,0.4532],  # 'ari'
# [0.6386,0.6566,0.7761,0.7096,0.7290]   # 'acc'
# ])#client5
#
# data = data_Photo
# plt.rcParams['font.sans-serif'] = ['msyh']
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
# xpos = xpos.flatten()
# ypos = ypos.flatten()
# zpos = np.zeros_like(xpos)
# # the width and height of block
# dx = 0.85
# dy = 0.85
# dz = data.flatten()
#
# # modify below if you want to change the color
# colors = ['#FAEE85','#7FCB82','#7BB2D6','#918AC2']
# # colors = ['#FFEB3B', '#A8E048', '#66B2FF', '#9C27B0']
#
# # i = 0.7
# # for y, color in zip(np.unique(ypos), colors):
# #     ax.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average',edgecolor='black',alpha = i)
# #     i+=0.1
# for y, color in zip(np.unique(ypos), colors):
#     ax.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
# # 绘制3D条形图shade=False, linewidth=10
# # ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=plt.cm.viridis(dz/float(max(dz))), zsort='average')
#
# # 设置坐标轴标签
# ax.set_xticks(np.arange(data.shape[1])+ 0.5)  # 设置刻度位置
# ax.set_xticklabels(['1', '5', '10', '15', '20'], fontsize=20)
# ax.set_yticks(np.arange(data.shape[0])+0.7)
# ax.set_yticklabels(['F1','NMI','ARI', 'ACC'], fontsize=20)
# ax.set_xlabel('k (%)', fontsize=20, labelpad=18)
# ax.set_ylabel('Metrics', fontsize=20, labelpad=22)
# ax.set_zlabel('Score', fontsize=20, labelpad=24)
# ax.view_init(elev=23, azim=-60, roll=0)
# # 设置Z轴限制
# ax.set_zlim(0, 0.75)
# # 设置Z轴的刻度和标签，并加粗字体
# ax.set_zticks([0, 0.2, 0.4, 0.6])  # 手动设置 Z 轴的刻度
# ax.set_zticklabels([f'{x:.1f}' for x in [0, 0.2, 0.4, 0.6]], fontsize=20)
# # 调整 ticklabels 的位置
# ax.tick_params(axis='x')
# ax.tick_params(axis='y')
# ax.tick_params(axis='z', labelsize=20,pad=8)
# ax.grid(False)
# plt.subplots_adjust(left=-0.1, bottom=0.03, right=1.0, top=1.05)
# plt.savefig(f'3D/Photo_600.png', dpi=600, transparent=False)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
import matplotlib.transforms as mtransforms

# Define the data for the four datasets
data_CiteSeer = np.array([
    [0.7116, 0.7144, 0.7288, 0.7200, 0.7051],  # 'nmi'
    [0.6716, 0.7044, 0.7588, 0.7200, 0.7151],  # 'ari'
    [0.7316, 0.7544, 0.8288, 0.7500, 0.8051],  # 'f1'
    [0.5321, 0.5882, 0.6335, 0.5797, 0.4962]   # 'acc'
])  # client10

data_PubMed = np.array([
        [0.3984, 0.4942, 0.5699, 0.6720, 0.6187],  # 'f1'

    [0.5545, 0.6780, 0.7592, 0.7667, 0.7512],  # 'ari'
        [0.5788, 0.6245, 0.6696, 0.6568, 0.5907],  # 'nmi'

    [0.6200, 0.6339, 0.6429, 0.6076, 0.5853]   # 'acc'
])  # client10

data_Computers = np.array([
    [0.1861, 0.2185, 0.2529, 0.1996, 0.2010],  # 'nmi'
    [0.1746, 0.2262, 0.3040, 0.2063, 0.2084],  # 'ari'
    [0.1873, 0.2188, 0.2509, 0.2277, 0.2290],  # 'f1'
    [0.6857, 0.6423, 0.7307, 0.6556, 0.6873]   # 'acc'
])  # client10

data_Photo = np.array([
    [0.2704, 0.3017, 0.3222, 0.3064, 0.3092],  # 'f1'
    [0.3055, 0.3832, 0.4040, 0.3548, 0.3611],  # 'nmi'
    [0.3449, 0.4025, 0.4777, 0.4520, 0.4532],  # 'ari'
    [0.6386, 0.6566, 0.7761, 0.7096, 0.7290]   # 'acc'
])  # client5

# Set up the 2x2 grid for the plots
fig = plt.figure(figsize=(16, 4))  # Adjusted figure size for tighter spacing

# Subplot 1 (CiteSeer)
ax1 = fig.add_subplot(141, projection='3d')
data = data_CiteSeer
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dx = dy = 0.85
dz = data.flatten()
colors = ['#FAEE85','#7FCB82','#7BB2D6','#918AC2']
for y, color in zip(np.unique(ypos), colors):
    ax1.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y]-0.2, color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)

ax1.set_xlabel(f'$\epsilon$', fontsize=20, labelpad=8)  # Adjust x-axis label distance
ax1.set_zlim(0, 0.75)
ax1.set_zticks([0.1, 0.3, 0.5, 0.7])
ax1.set_zticklabels([f'{x:.1f}' for x in [0.2, 0.4, 0.6, 0.8]], fontsize=18)

# Subplot 2 (PubMed)
ax2 = fig.add_subplot(142, projection='3d')
data = data_PubMed
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = data.flatten()
for y, color in zip(np.unique(ypos), colors):
    ax2.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y] -0.1, color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
ax2.set_yticks(np.arange(data.shape[0]) + 0.5)
ax2.set_yticklabels(['ACC', 'NMI', 'ARI', "F1"], fontsize=18, rotation=10)

yticks = ax2.get_yticks()

for label, y in zip(ax2.get_yticklabels(), yticks):
    label.set_position((0.9, y, 0))  # (x, y, z)

ax2.tick_params(axis='y', pad=1)  # 调整 y 轴刻度标签与轴的距离
ax2.tick_params(axis='x', pad=2)  # 调整 y 轴刻度标签与轴的距离

ax2.set_xlabel(f'$\epsilon$', fontsize=20, labelpad=8)  # Adjust x-axis label distance
ax2.set_zlim(0., 0.75)
ax2.set_zticks([0.2, 0.4, 0.6, 0.8 ])
ax2.set_zticklabels([f'{x:.1f}' for x in [0.1, 0.3, 0.5, 0.7]], fontsize=18)

# Subplot 3 (Computers)
ax3 = fig.add_subplot(143, projection='3d')
data = data_Computers
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = data.flatten()
for y, color in zip(np.unique(ypos), colors):
    ax3.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
ax3.set_yticks(np.arange(data.shape[0]) + 0.7)
ax3.set_xlabel('k (%)', fontsize=18, labelpad=12)  # Adjust x-axis label distance
ax3.set_zlim(0, 0.75)
ax3.set_zticks([0, 0.2, 0.4, 0.6])
ax3.set_zticklabels([f'{x:.1f}' for x in [0, 0.2, 0.4, 0.6]], fontsize=18)

# Subplot 4 (Photo)
ax4 = fig.add_subplot(144, projection='3d')
data = data_Photo
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = data.flatten()
for y, color in zip(np.unique(ypos), colors):
    ax4.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
ax4.set_yticks(np.arange(data.shape[0]) + 0.7)
ax4.set_zlim(0, 0.75)
ax4.set_zticks([0, 0.2, 0.4, 0.6])
ax4.set_zticklabels([f'{x:.1f}' for x in [0, 0.2, 0.4, 0.6]], fontsize=18)

# Adjust layout to make subplots closer
# plt.subplots_adjust(wspace=-0.3, hspace=0.1)


axs = [ax1, ax2, ax3, ax4]
for a in axs:
    a.set_xticks(np.arange(data.shape[1]) - 0)
    a.set_xticklabels(['5:1', '3:1', '1:1', '1:3', '1:5'], fontsize=18, rotation=-65)
    a.tick_params(axis='x', pad=-1)  # 调整 y 轴刻度标签与轴的距离
    a.set_yticks(np.arange(data.shape[0]) + 0.7)
    a.set_yticklabels(['ACC', 'NMI', 'ARI', "F1"], fontsize=16,  rotation=10 )
    a.tick_params(axis='y', pad=1)  # 调整 y 轴刻度标签与轴的距离
    a.set_ylabel('Metrics', fontsize=18, labelpad=8)  # Adjust y-axis label distance
    a.set_xlabel(f"$\\alpha$:$\\beta$", fontsize=18, labelpad=6)  # Adjust x-axis label distance


ax4.set_zlabel('Score', fontsize=18, labelpad=12, rotation=0)  # Adjust z-axis label distance

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=1, wspace=0.1, hspace=0)

plt.tight_layout()

# Save and show the plot
# plt.savefig('./projects/ASPIRE/output/hyper.png', dpi=600, transparent=False)

plt.show()
