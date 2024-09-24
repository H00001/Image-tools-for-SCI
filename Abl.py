import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 示例数据
x_labels = ['acc', 'nmi', 'ari', 'f1']
y_labels = ['-Base', '-C', '-F', '-Ours']

NMAE = "LETTER"
# 定义z_values
z_values_LETTER = np.array([
    [0.06, 0.12,0.03,0.122],  # 'acc'
    [0.15, 0.32,0.13,0.134],  # 'nmi'
    [0.18, 0.35,0.15,0.167] ,  # 'ari'
    [0.25, 0.43, 0.18, 0.24]  # 'ari'

])

z_values = np.array([
    [0.06, 0.12, 0.03, 0.122],  # 'acc'
    [0.15, 0.32, 0.13, 0.134],  # 'nmi'
    [0.18, 0.35, 0.15, 0.167],  # 'ari'
    [0.25, 0.43, 0.18, 0.24]    # 'f1'
])



z_values = np.array([
    [0.06, 0.12, 0.03, 0.122],  # 'acc'
    [0.15, 0.32, 0.13, 0.134],  # 'nmi'
    [0.18, 0.35, 0.15, 0.167],  # 'ari'
    [0.25, 0.43, 0.18, 0.24]    # 'f1'
])

z_values = z_values.T

x = np.arange(len(x_labels))
y = np.arange(len(y_labels))
X, Y = np.meshgrid(x, y)
Z = np.array(z_values).T  # 转置使之适合 meshgrid

# 创建 3D 图形
# fig = plt.figure()
fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(111, projection='3d')

# 绘制表面图
surf = ax.plot_surface(X, Y, Z, cmap='plasma')
ax.contourf(X, Y, Z, zdir='z', offset=0, cmap='plasma', alpha=0.5)

# cbar = fig.colorbar(surf, aspect=5, shrink=0.5)
# cbar.set_label('Intensity', fontsize=10, fontweight='bold', color='darkblue')

ax.set_zlabel('Score')

# 设置坐标轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_yticks(y)
ax.set_yticklabels(y_labels)

# 在3D图中添加五条分割线
for i in range(1, len(x)):
    ax.plot([i, i], [0, len(y_labels)-1], [0, 0], color='black', linestyle='--')


ax.view_init(elev=18, azim=-74)

# 设置背景颜色
ax.set_facecolor('white')
fig.patch.set_facecolor('white')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# 隐藏轴线
ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))


plt.savefig(f"./abl/_eps",dpi=1200)
plt.savefig(f"./abl/_eps.eps",bbox_inches='tight')

# plt.show()

