import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
import seaborn as sns

# ==== 设置指标类型 ====
name = "ACC"
if name == 'ACC':
    end = 0.9
if name == 'NMI':
    end = 5
if name == 'ARI':
    end = 10
if name == 'F1':
    end = 90

# ==== 标签设置 ====
x_labels = ['100', '10', '1', '0.1', '0.01']        # 横轴 λ（5 列）
y_labels = ['0.01', '0.1', '1', '10', '100']        # 纵轴 μ（5 行）

# ==== 5x5 ACC 数据 ====
ACC_values = np.array([
    [0.7238, 0.7241, 0.7241, 0.7244, 0.7244],
    [0.6928, 0.7244, 0.7253, 0.7244, 0.7244],
    [0.6486, 0.6943, 0.7244, 0.7256, 0.7241],
    [0.5942, 0.6417, 0.6946, 0.7241, 0.7256],
    [0.5861, 0.5927, 0.6423, 0.6943, 0.7241],
])

z_values = ACC_values  # shape = (5, 5)

# ==== 自定义颜色映射 ====
cmap = sns.color_palette("light:#0080FF", as_cmap=True)
norm = colors.BoundaryNorm(boundaries=np.linspace(np.min(z_values), np.max(z_values), 100), ncolors=cmap.N)

# ==== 构造网格 ====
x = np.arange(len(x_labels))  # 5
y = np.arange(len(y_labels))  # 5
X, Y = np.meshgrid(x, y)      # shape = (5, 5)

# ==== 创建 3D 图形 ====
fig = plt.figure(figsize=(10, 8))  # Increase figure size
ax = fig.add_subplot(111, projection='3d')

# 绘制 3D 表面图
surf = ax.plot_surface(X, Y, z_values, facecolors=cmap(norm(z_values)),
                       shade=False, edgecolor='k', linewidth=0.5, antialiased=True)

# z=0 平面投影
ax.plot_surface(X, Y, np.zeros_like(z_values), facecolors=cmap(norm(z_values)),
                shade=False, edgecolor="k", linewidth=0.5)

# ==== 坐标轴设置 ====
ax.set_xticks(x)
ax.set_xticklabels(x_labels, fontsize=14)  # Increase font size for x-axis labels
ax.set_yticks(y)
ax.set_yticklabels(y_labels, fontsize=14)  # Increase font size for y-axis labels

# 隐藏默认 z 轴刻度和标签
ax.set_zticks([])
ax.set_zlabel('', fontsize=14)

ax.set_xlabel(r'$\mu$', fontsize=16)  # Increase font size for x-axis label
ax.set_ylabel(r'$\lambda$', fontsize=16)  # Increase font size for y-axis label
ax.set_zlim(0.6, end)

# ==== 手动绘制 z 轴刻度和刻度标签（放在对立面） ====
z_tick_positions = np.linspace(0.6, end, 5)  # 5个刻度，和默认5个刻度一样
x_pos = x[0] - 0.3  # 比 x 最小值更左边一些
y_pos = y[-1] + 0.3  # 比 y 最大值更远一些

for z_tick in z_tick_positions:
    ax.plot([x_pos, x_pos + 0.1], [y_pos, y_pos], [z_tick, z_tick], color='black')
    ax.text(x_pos - 0.05, y_pos, z_tick, f"{z_tick:.2f}", fontsize=12, ha='right', va='center')  # Increase font size

# ==== 添加手动的 z 轴标签 ====
ax.text(x_pos - 0.15, y_pos, (0.6 + end)/2, f"{name} (%)", rotation=90, fontsize=16, ha='center', va='center')  # Increase font size

# ==== 调整视角，让“对立面柱子”更显眼 ====
ax.view_init(elev=19, azim=135)

# 美化外观
ax.set_facecolor('white')
fig.patch.set_facecolor('white')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

plt.show()
