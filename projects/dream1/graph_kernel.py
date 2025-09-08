import matplotlib.pyplot as plt
import numpy as np

labels = ['SP', 'GK', 'RW', 'WL', "HRW"]
SM = np.array([[20.3, 22.1, 19.5, 20.2, 27],[24.2, 26.6, 23.4, 24.4, 34],[62.1, 61.7, 62.5, 63.5, 71],[64.3, 63.1, 63.5, 63.9, 77]])/100
SM_BIO = np.array([[19.3, 14, 13.2, 15.5, 21.4],[20.7, 15.5, 17.2, 19.7, 24.1],[53.8, 55.9, 54.2, 56.8, 63],[65.1, 63.9, 66.5, 62.9, 73]])/100

# x = np.arange(len(labels))

# colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B3']

# fig, axs = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)  # 2列1行，y轴共享

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


fig = plt.figure(figsize=(9, 3.5))  # Adjusted figure size for tighter spacing

# Subplot 1 (CiteSeer)
ax1 = fig.add_subplot(121, projection='3d')
data = SM
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dx = dy = 0.85
dz = data.flatten()
colors = ['#FAEE85','#7FCB82','#7BB2D6','#918AC2']
for y, color in zip(np.unique(ypos), colors):
    ax1.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
ax1.set_xticks(np.arange(data.shape[1]) + 0.5)
ax1.set_xticklabels(
    ['SP', 'LT', 'RW', 'WL', "HRW"], 
    fontsize=16, 
    rotation=20,
    # ha='right',
    # pad=0  # 直接在这里设置 pad
)


ax1.tick_params(axis='x', pad=-1)  # 调整 y 轴刻度标签与轴的距离
ax1.tick_params(axis='y', pad=-2)  # 调整 y 轴刻度标签与轴的距离

ax1.set_yticks(np.arange(data.shape[0]) +0.8)
ax1.set_yticklabels(['NMI', 'ARI',  "F1",'ACC',], fontsize=16,  rotation=-20 )
ax1.set_xlabel(f'SM', fontsize=16, labelpad=8, rotation=-40)  # Adjust x-axis label distance
ax1.set_ylabel('Metrics', fontsize=16, labelpad=8)  # Adjust y-axis label distance
# ax1.set_zlabel('Score', fontsize=18, labelpad=10)  # Adjust z-axis label distance
ax1.set_zlim(0, 0.82)
ax1.set_zticks([0, 0.2, 0.4, 0.6, 0.8])
ax1.set_zticklabels([f'{x:.1f}' for x in [0, 0.2, 0.4, 0.6, 0.8]], fontsize=18)

# Subplot 2 (PubMed)
ax2 = fig.add_subplot(122, projection='3d')
data = SM_BIO
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = data.flatten()
for y, color in zip(np.unique(ypos), colors):
    ax2.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
ax2.set_xticks(np.arange(data.shape[1]) + 0.5)
ax2.set_xticklabels(['SP', 'LT', 'RW', 'WL', "HRW"], fontsize=16,rotation=15)
ax2.set_yticks(np.arange(data.shape[0]) + 0.8)
ax2.set_yticklabels(['NMI', 'ARI', "F1", 'ACC'], fontsize=16, rotation=-25)

yticks = ax2.get_yticks()

for label, y in zip(ax2.get_yticklabels(), yticks):
    label.set_position((0.9, y, 0))  # (x, y, z)

ax2.tick_params(axis='y', pad=-2)  # 调整 y 轴刻度标签与轴的距离
ax2.tick_params(axis='x', pad=-1)  # 调整 y 轴刻度标签与轴的距离
# ax2.label_params(axis='x', pad=-1)

ax2.set_xlabel(f'SM-BIO', fontsize=16, labelpad=8, rotation=-40)  # Adjust x-axis label distance
ax2.set_ylabel('Metrics', fontsize=16, labelpad=8)  # Adjust y-axis label distance
ax2.set_zlabel('Score', fontsize=18, labelpad=6)  # Adjust z-axis label distance
ax2.set_zlim(0., 0.72)
ax2.set_zticks([0.1, 0.3, 0.5, 0.7 ])
ax2.set_zticklabels([f'{x:.1f}' for x in [0.1, 0.3, 0.5, 0.7]], fontsize=18)
ax1.view_init(elev=22, azim=-44)
ax2.view_init(elev=22, azim=-44)
fig.patch.set_alpha(0)

# 设置坐标轴背景透明
ax1.patch.set_alpha(0)
ax2.patch.set_alpha(0)
ax1.set_facecolor('white')
fig.patch.set_facecolor('white')
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=1, wspace=0, hspace=0)
plt.tight_layout()

# Save and show the plot
plt.savefig('./projects/dream1/output/GK.png', dpi=600, transparent=False)

# plt.show()
