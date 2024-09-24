import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
import seaborn as sns

name = "NMI"
if name == 'ACC':
    end = 90
if name == 'NMI':
    end = 4
if name == 'ARI':
    end = 8
if name == 'F1':
    end = 80
# 示例数据
y_labels = ['0.01', '0.1', '1', '10', '100']
x_labels = ['100', '10', '1', '0.1','0.01']
ACC_values = np.array([
    [81.2, 80.12, 80.03, 78.42, 75.03],  
    [80.1, 81.26, 80.13, 80.34, 78.01],  
    [79.1, 81.35, 81.26, 80.67, 80.86],  
    [78.6, 79.46, 80.18, 80.2, 80.41],  
    [75.2, 74.43, 79.22, 80.24, 81.26],  
])

ARI_values = np.array([
    [7.48, 6.12, 7.42, 6.42, 5.97],  
    [6.31, 7.5, 6.53, 6.40, 5.01],  
    [5.24, 6.85, 7.48, 6.7, 5.62],  
    [4.75, 6.0, 7.23, 7.44, 6.89],  
    [5.35, 5.43, 6.62, 6.46, 7.46],  
])

NMI_values = np.array([
    [3.8, 3.12, 3.23, 2.4, 1.7],  
    [2.8, 3.8, 3.45, 3.04, 2.5],  
    [3.18, 2.54, 3.8, 3.20, 1.9],  
    [2.75, 3.61, 3.18, 3.7, 2.0],  
    [2.544, 2.43, 2.86, 2.34, 3.8],  
])

F1_values = np.array([
    [77.26, 72.12, 75.66, 74.867, 75.11],  
    [83.15, 76.29, 74.3, 74.14, 76.01],  
    [74.18, 81.35, 77.28, 75.25, 74.76],  
    [72.13, 76.81, 76.69, 77.29, 72.3],  
    [70.25, 74.43, 72.38, 76.24, 78.29],  
])

z_values = eval(f"{name}_values").T

# 定义自定义颜色映射和颜色边界
def generate_green_palette(n):
    """生成 n 种绿色的颜色映射"""
    return [(0.0, i / n, 0.0) for i in range(n)]

# 创建99种绿色的颜色映射
num_colors = 99
cmap = sns.color_palette("summer", as_cmap=True)

norm = colors.BoundaryNorm(boundaries=np.linspace(np.min(z_values), np.max(z_values), 100), ncolors=cmap.N)

# 创建 x 和 y 的网格
x = np.arange(len(x_labels))
y = np.arange(len(y_labels))
X, Y = np.meshgrid(x, y)

# 创建 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制3D表面图，并在表面上进行颜色投影
surf = ax.plot_surface(X, Y, z_values, facecolors=cmap(norm(z_values)), shade=False)

# 在 z=0 平面上投影色块
ax.plot_surface(X, Y, np.zeros_like(z_values), facecolors=cmap(norm(z_values)), shade=False)
# ax.set_title(f'{name}', fontsize=16, pad=-10)  # Adjust fontsize and pad as needed

# 设置坐标轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_yticks(y)
ax.set_yticklabels(y_labels)
ax.set_zlabel(f"{name} (%)",rotation=90)
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$\beta$')

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


plt.savefig(f"./ICASSP/3d/{name}_para_600.png", dpi = 600)
plt.savefig(f"./ICASSP/3d/{name}_para_1200.png", dpi = 1200)

# plt.show()
