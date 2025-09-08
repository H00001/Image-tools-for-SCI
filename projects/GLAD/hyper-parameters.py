import matplotlib.pyplot as plt
import numpy as np

# labels = ['SP', 'GK', 'RW', 'WL', "HRW"]
SM = np.array([[54.2, 57.6, 60.1, 59.9, 58.3],[58.6, 54.3, 62.5, 63.5, 59.6],[65.2, 63.1, 62.2, 61.7, 62.4],[60.8, 61.7, 64.5, 65.5, 63.4]])/100
SM_BIO = np.array([[66.4, 68.5, 71.7, 73.2, 67.3],[64.3, 72.1, 70.2, 68.4, 66.6],[78, 79.2, 80.5, 82.8, 84],[99.1, 99.9, 99.5, 99.9, 99]])/100


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


fig = plt.figure(figsize=(8, 3.2))  # Adjusted figure size for tighter spacing

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
    ['2', '4', '6', '8', "10"], 
    fontsize=20, 
    rotation=0,
    # ha='right',
    # pad=0  # 直接在这里设置 pad
)


ax1.tick_params(axis='x', pad=-1)  # 调整 y 轴刻度标签与轴的距离
ax1.tick_params(axis='y', pad=-2)  # 调整 y 轴刻度标签与轴的距离

ax1.set_yticks(np.arange(data.shape[0]) +0.8)
ax1.set_yticklabels(['ENZY', "DHFR", 'COX2'  ,'IMDB'], fontsize=14,  rotation=-5)
ax1.set_xlabel("K", fontsize=18, labelpad=8, rotation=0)  # Adjust x-axis label distance
ax1.set_ylabel('Datasets', fontsize=16, labelpad=6)  # Adjust y-axis label distance
# ax1.set_zlabel('Score', fontsize=18, labelpad=10)  # Adjust z-axis label distance
ax1.set_zlim(0, 0.82)
ax1.set_zticks([0, 0.2, 0.4, 0.6, 0.8])
ax1.set_zticklabels([f'{x:.1f}' for x in [0, 0.2, 0.4, 0.6, 0.8]], fontsize=16)

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
ax2.set_xticklabels(['2', '4', '6', '8', "10"], fontsize=18,rotation=0)
ax2.set_yticks(np.arange(data.shape[0]) + 0.8)
ax2.set_yticklabels(['PROT', 'BZR', 'DD', "AIDS" ], fontsize=14, rotation=-5)

yticks = ax2.get_yticks()

for label, y in zip(ax2.get_yticklabels(), yticks):
    label.set_position((0.9, y, 0))  # (x, y, z)

ax2.tick_params(axis='y', pad=-2)  # 调整 y 轴刻度标签与轴的距离
ax2.tick_params(axis='x', pad=-1)  # 调整 y 轴刻度标签与轴的距离
# ax2.label_params(axis='x', pad=-1)

ax2.set_xlabel(f'K', fontsize=18, labelpad=8, rotation=-0)  # Adjust x-axis label distance
ylab = ax2.set_ylabel('Datasets', fontsize=16, labelpad=6, horizontalalignment='right')  # Adjust y-axis label distance
# ylab.set_position((1, 0.3))  # x 和 y 是相对坐标（0-1）

ax2.set_zlabel('Score', fontsize=18, labelpad=6, rotation=0)  # Adjust z-axis label distance
ax2.set_zlim(0., 1.02)
ax2.set_zticks([0.1, 0.3, 0.5, 0.7, 0.9])
ax2.set_zticklabels([f'{x:.1f}' for x in [0.1, 0.3, 0.5, 0.7, 0.9]], fontsize=16)
ax1.view_init(elev=26, azim=-52)
ax2.view_init(elev=26, azim=-52)


plt.subplots_adjust(left=0, bottom=0.1, right=0.9, top=1, wspace=-0.15, hspace=0)
plt.tight_layout()

# Save and show the plot
plt.savefig('./projects/GLAD/output/hyper-3D.png', dpi=600, transparent=False)

plt.show()
