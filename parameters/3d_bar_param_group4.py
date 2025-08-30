import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

name = "COX2"
# 数据设置
x_labels = ['100', '10', '1', '0.1', '0.01']
y_labels = ['0.01', '0.1', '1', '10', '100']

COX2_ACC_values = np.array([
    [82.7, 80.12, 80.03, 78.42, 75.03],  
    [80.1, 82.26, 80.13, 80.34, 78.01],  
    [79.1, 81.35, 82.26, 80.67, 80.86],  
    [78.6, 79.46, 80.18, 82.2, 80.41],  
    [75.2, 74.43, 79.22, 80.24, 82.26],  
])
COX2_ACC_values = np.rot90(COX2_ACC_values)

COX2_ARI_values = np.array([
    [6.98, 6.42, 6.42, 6.42, 5.97],  
    [7.01, 7.75, 6.53, 6.30, 5.51],  
    [7.24, 7.88, 8.27, 6.7, 5.62],  
    [7.98, 7.06, 8.26, 8.14, 6.89],  
    [8.05, 8.13, 8.02, 7.46, 8.21],  
])
COX2_ARI_values = np.rot90(COX2_ARI_values)


COX2_NMI_values = np.array([
    [3.95, 3.78, 3.23, 3.4, 3.2],  
    [3.97, 3.99, 3.45, 3.24, 3.5],  
    [4.12, 3.74, 4.18, 3.40, 3.1],  
    [4.05, 3.85, 3.88, 4.17, 3.4],  
    [4.14, 3.96, 3.72, 3.54, 3.57],  
])
COX2_NMI_values = np.rot90(COX2_NMI_values)

COX2_F1_values = np.array([
    [81.26, 76.12, 75.66, 74.867, 73.11],  
    [76.15, 82.29, 77.3, 74.14, 76.01],  
    [74.18, 77.35, 83.28, 77.25, 74.76],  
    [74.13, 76.81, 76.69, 82.29, 76.3],  
    [73.25, 76.43, 74.38, 76.24, 82.29],  
])
COX2_F1_values = np.rot90(COX2_F1_values)





Letter_ACC_values = np.array([
    [42.1, 37.12, 39.03, 38.42, 38.03],  
    [40.1, 42.1, 38.13, 38.34, 38.22],  
    [39.1, 41.35, 42.1 , 40.67, 40.86],  
    [38.6, 39.46, 40.18, 42.1, 40.41],  
    [38.2, 38.43, 39.22, 40.24, 42.26],  
])
Letter_ACC_values = np.rot90(Letter_ACC_values)

Letter_ARI_values = np.array([
    [24.98, 20.42, 19.42, 19.88, 20.97],  
    [23.01, 23.75, 19.53, 20.30, 20.51],  
    [23.24, 23.88, 24.27, 22.7, 21.62],  
    [22.98, 22.06, 23.26, 24.14, 22.89],  
    [21.05, 21.13, 22.02, 22.46, 24.21],  
])
Letter_ARI_values = np.rot90(Letter_ARI_values)



Letter_NMI_values = np.array([
    [50.4, 46.12, 31.66, 32.86, 32.11],  
    [36.15, 50.4, 32.3, 36.14, 34.01],  
    [44.18, 37.35, 50.4, 48.25, 44.76],  
    [44.13, 45.81, 46.69, 50.4, 46.3],  
    [43.25, 46.43, 44.38, 46.24, 50.4],  
])
Letter_NMI_values = np.rot90(Letter_NMI_values)

Letter_F1_values = np.array([
    [43.4, 38.78, 36.23, 34.6, 34.2],  
    [43.97, 42.2, 38.45, 38.24, 37.5],  
    [38.12, 38.74, 44.18, 41.40, 37.1],  
    [34.05, 36.85, 37.88, 42.17, 39.4],  
    [34.14, 34.96, 34.72, 38.54, 39.57],  
])
Letter_F1_values = np.rot90(Letter_F1_values)





# Colormap setup (using 'coolwarm' for a more cohesive color palette)
cmap = sns.color_palette("Spectral", as_cmap=True)

# 创建子图
fig = plt.figure(figsize=(33, 8.0))
axes = [fig.add_subplot(141, projection='3d'),
        fig.add_subplot(142, projection='3d'),
        fig.add_subplot(143, projection='3d'),
        fig.add_subplot(144, projection='3d')]

# 数据与标题
values = [eval(f"{name}_ACC_values"), eval(f"{name}_NMI_values"), eval(f"{name}_ARI_values"), eval(f"{name}_F1_values")]
titles = ['ACC', 'ARI', 'NMI', 'F1']

# 调整子图之间的间距
fig.subplots_adjust(left=0.00, right=0.850, top=1, bottom=0.05, hspace=0, wspace=0.2)

# 绘制每个指标的3D柱状图
for ax, value, title in zip(axes, values, titles):
    x = np.arange(len(x_labels))
    y = np.arange(len(y_labels))
    X, Y = np.meshgrid(x, y)

    # 计算柱状图的底部位置
    xpos, ypos = np.meshgrid(x, y, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = np.zeros_like(xpos)

    # 高度（柱状图的高度）
    zvals = value.T.ravel()

    # 宽度和深度
    dx = dy = 0.8

    # 绘制3D柱状图 with transparent edges
    ax.bar3d(xpos, ypos, zpos, dx, dy, zvals, 
              color=cmap((zvals - np.min(zvals)) / (np.max(zvals) - np.min(zvals))),
              edgecolor=(0, 0, 0, 0.3), shade=True)  # Transparent edges (RGBA)

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=16)  # Increase font size for x-axis ticks
    ax.set_yticks(y)
    ax.set_yticklabels(y_labels, fontsize=16)  # Increase font size for y-axis ticks
    ax.set_xlabel(r'$\lambda$', fontsize=16)  # Increase font size for x-axis label
    ax.set_ylabel(r'$\mu$', fontsize=16)  # Increase font size for y-axis label
    ax.set_zlabel(f"{title} (%)", fontsize=16)  # Increase font size for z-axis label

    # 优化图形显示
    ax.view_init(elev=20, azim=-45)
    ax.set_facecolor('white')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.tick_params(axis='both', which='major', labelsize=12)  # Increase tick label size

# 显示图形
plt.show()
