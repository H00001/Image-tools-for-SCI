import matplotlib.pyplot as plt
import numpy as np
import sys
import os
# labels = ['SP', 'GK', 'RW', 'WL', "HRW"]
SM = np.array([[54.2, 57.6, 60.1, 59.9, 58.3],
               [58.6, 54.3, 62.5, 63.5, 59.6],
               [65.2, 63.1, 62.2, 61.7, 62.4],
               [60.8, 61.7, 64.5, 65.5, 63.4]])/100
SM_BIO = np.array([[66.4, 68.5, 71.7, 73.2, 64.3],
                   [64.3, 72.1, 70.2, 68.4, 66.6],
                   [78, 79.2, 80.5, 84.8, 83],
                   [99.1, 99.9, 99.5, 99.9, 99]])/100

sm1 = np.array([
    [473,  130,77.5,  44.9, 67],
    [580,  215,104,  47.8,86],
    [94.8,   85,122, 9, 63],
    [106,   127,48,10, 62]
])
sm2 = np.array([
   [20.12,22.05,16.22, 16.87,   17.16],
    [21.35,19.42,16.32,   16.52, 17.18],
    [22.40,18.45,17.18,  16.61,  18.92],
    [20.27,19.91,17.20,  16.66,  16.37]
])

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


fig = plt.figure(figsize=(8, 3.2))  # Adjusted figure size for tighter spacing

# Subplot 1 (CiteSeer)
ax1 = fig.add_subplot(121, projection='3d')
data = sm1
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dx = dy = 0.85
dz = data.flatten()
colors = ['#FAEE85','#7FCB82','#7BB2D6','#918AC2']
for y, color in zip(np.unique(ypos), colors):
    ax1.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
ax1.set_xticks(np.arange(data.shape[1]) + 0.0)
ax1.set_xticklabels(
    [ 'SDGG','CARE', 'MUSE','HC-G',  "OURS"], 
    fontsize=14, 
    rotation=20,
    # ha='right',
    # pad=0  # 直接在这里设置 pad
)


ax1.tick_params(axis='x', pad=-1)  # 调整 y 轴刻度标签与轴的距离
ax1.tick_params(axis='y', pad=-2)  # 调整 y 轴刻度标签与轴的距离

ax1.set_yticks(np.arange(data.shape[0]) +0.8)
ax1.set_yticklabels(['DHFR', "IMDB", 'BZR'  ,'COX2'], fontsize=14,  rotation=-15 )
ax1.set_xlabel("Methods", fontsize=16, labelpad=10, rotation=0) 

 # Adjust x-axis label distance
ax1.set_ylabel('Datasets', fontsize=16, labelpad=8)  # Adjust y-axis label distance
# ax1.set_zlabel('Score', fontsize=18, labelpad=10)  # Adjust z-axis label distance
ax1.set_zlim(0, 601)
ax1.set_zticks([0, 200, 400, 600])
ax1.set_zticklabels([f'{x:}' for x in [0, 200, 400, 600]], fontsize=18)

# Subplot 2 (PubMed)
ax2 = fig.add_subplot(122, projection='3d')
data = sm2
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = data.flatten()
for y, color in zip(np.unique(ypos), colors):
    ax2.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
ax2.set_xticks(np.arange(data.shape[1]) + 0.5)
ax2.set_yticks(np.arange(data.shape[0]) + 0.8)
ax2.set_xticklabels(
    ["SDGG","MUSE", "HC-G",  "CARE", "OURS"], 
    fontsize=14, 
    rotation=20,
    # ha='right',
    # pad=0  # 直接在这里设置 pad
)
ax2.set_yticklabels(['DHFR', "IMDB", 'BZR'  ,'COX2'], fontsize=14,  rotation=-15 )


ax2.set_xlabel("Methods", fontsize=16, labelpad=10, rotation=0)  # Adjust x-axis label distance

yticks = ax2.get_yticks()

# for label, y in zip(ax2.get_yticklabels(), yticks):
#     label.set_position((0.9, y, 0))  # (x, y, z)

ax2.tick_params(axis='y', pad=-2)  # 调整 y 轴刻度标签与轴的距离
ax2.tick_params(axis='x', pad=-1)  # 调整 y 轴刻度标签与轴的距离
# ax2.label_params(axis='x', pad=-1)

# ax2.set_xlabel(f'K', fontsize=18, labelpad=8, rotation=-0)  # Adjust x-axis label distance
ylab = ax2.set_ylabel('Datasets', fontsize=16, labelpad=8, horizontalalignment='right')  # Adjust y-axis label distance
# ylab.set_position((1, 0.3))  # x 和 y 是相对坐标（0-1）

# ax2.set_zlabel('Score', fontsize=18, labelpad=6, rotation=0)  # Adjust z-axis label distance
ax2.set_zlim(0., 26)
ax2.set_zticks([5, 10, 15, 20, 25])
ax2.set_zticklabels([f'{x:.1f}' for x in [5, 10, 15, 20, 25]], fontsize=18)
ax1.view_init(elev=26, azim=-45)
ax2.view_init(elev=26, azim=-45)


plt.subplots_adjust(left=0, bottom=0.1, right=0.9, top=1, wspace=-0.0, hspace=0)
plt.tight_layout()

# Save and show the plot
# plt.savefig('./projects/GLAD/output/hyper-3D.png', dpi=600, transparent=False)

ax1.text2D(1.18, 0.88, 'Runtime (ms)', transform=ax1.transAxes, fontsize=14, ha='right', va='top',  bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='#222222',
        boxstyle='round,pad=0.2'
    ))
ax2.text2D(1.18, 0.88, 'Memory (MB)', transform=ax2.transAxes, fontsize=16, ha='right', va='top',bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='#222222',
        boxstyle='round,pad=0.2'
    ))


script_path = sys.argv[0]
current_dir = os.path.dirname(__file__)
script_name = os.path.basename(sys.argv[0])

plt.savefig(f"{current_dir}/output/{script_name}.png", dpi=600)
#

plt.show()
