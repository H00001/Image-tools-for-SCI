import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
import seaborn as sns

name = "F1"
if name == 'ACC':
    end = 90
if name == 'NMI':
    end = 5
if name == 'ARI':
    end = 10
if name == 'F1':
    end =90
# 示例数据
x_labels = ['100', '10', '1', '0.1', '0.01']
y_labels = ['0.01', '0.1', '1', '10','100']
ACC_values = np.array([
    [82.7, 80.12, 80.03, 78.42, 75.03],  
    [80.1, 82.26, 80.13, 80.34, 78.01],  
    [79.1, 81.35, 82.26, 80.67, 80.86],  
    [78.6, 79.46, 80.18, 82.2, 80.41],  
    [75.2, 74.43, 79.22, 80.24, 82.26],  
])
ACC_values = np.rot90(ACC_values)

ARI_values = np.array([
    [6.98, 6.42, 6.42, 6.42, 5.97],  
    [7.01, 7.75, 6.53, 6.30, 5.51],  
    [7.24, 7.88, 8.27, 6.7, 5.62],  
    [7.98, 7.06, 8.26, 8.14, 6.89],  
    [8.05, 8.13, 8.02, 7.46, 8.21],  
])
ARI_values = np.rot90(ARI_values)

NMI_values = np.array([
    [3.95, 3.78, 3.23, 3.4, 3.2],  
    [3.97, 3.99, 3.45, 3.24, 3.5],  
    [4.12, 3.74, 4.18, 3.40, 3.1],  
    [4.05, 3.85, 3.88, 4.17, 3.4],  
    [4.14, 3.96, 3.72, 3.54, 3.57],  
])

NMI_values = np.rot90(NMI_values)


F1_values = np.array([
    [81.26, 73.12, 75.66, 74.867, 75.11],  
    [77.15, 82.29, 77.3, 74.14, 76.01],  
    [74.18, 77.35, 83.28, 77.25, 74.76],  
    [72.13, 76.81, 76.69, 82.29, 76.3],  
    [73.25, 74.43, 72.38, 76.24, 82.29],  
])
F1_values = np.rot90(F1_values)

z_values = eval(f"{name}_values").T

# 定义自定义颜色映射和颜色边界
def generate_green_palette(n):
    """生成 n 种绿色的颜色映射"""
    return [(0.0, i / n, 0.0) for i in range(n)]


num_colors = 99

def create_custom_cmap():
    # 创建一个从蓝色到白色的颜色映射
    blue_to_white = sns.color_palette("Blues", 256)
    # 创建一个从白色到蓝色的颜色映射
    white_to_blue = sns.color_palette("Blues", 256)[::-1]
    # 结合两个颜色映射，使中间区域颜色变化更明显
    custom_cmap = np.vstack((blue_to_white[:128], white_to_blue[128:]))
    return sns.color_palette(custom_cmap)

# 应用自定义颜色映射
custom_cmap = create_custom_cmap()
cmap = sns.color_palette("light:#0080FF", as_cmap=True)
# cmap = custom_cmap
norm = colors.BoundaryNorm(boundaries=np.linspace(np.min(z_values), np.max(z_values), 100), ncolors=cmap.N)


x = np.arange(len(x_labels))
y = np.arange(len(y_labels))
X, Y = np.meshgrid(x, y)

# 创建 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制3D表面图，并在表面上进行颜色投影
surf = ax.plot_surface(X, Y, z_values, facecolors=cmap(norm(z_values)), shade=False, edgecolor='k', linewidth=0.5, antialiased=True)

# 在 z=0 平面上投影色块
ax.plot_surface(X, Y, np.zeros_like(z_values), facecolors=cmap(norm(z_values)), shade=False,edgecolor="k", linewidth=0.5)
# ax.set_title(f'{name}', fontsize=16, pad=-10)  # Adjust fontsize and pad as needed

# 设置坐标轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_yticks(y)
ax.set_yticklabels(y_labels)
ax.set_zlabel(f"{name} (%)",rotation=90)
ax.set_xlabel(r'$\lambda$')
ax.set_ylabel(r'$\mu$')

# 调整视角
ax.view_init(elev=19, azim=-45)

# 美化图形
ax.set_facecolor('white')
fig.patch.set_facecolor('white')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.set_zlim(0,end)
ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

fig.patch.set_alpha(0)

# 设置坐标轴背景透明
ax.patch.set_alpha(0)
# plt.savefig(f"./ACCESS/3d/{name}_para_600.png", dpi = 600)
# plt.savefig(f"./ACCESS/3d/{name}_para_1200.png", dpi = 1200)

plt.show()
