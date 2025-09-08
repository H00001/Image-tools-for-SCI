import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
import seaborn as sns

# 标签
x_labels = ['100', '10', '1', '0.1', '0.01']
y_labels = ['0.01', '0.1', '1', '10', '100']
x = np.arange(len(x_labels))
y = np.arange(len(y_labels))
X, Y = np.meshgrid(x, y)

# 数据
metric_dict = {
    "ACC": np.array([
        [78.7, 77.12, 74.03, 75.42, 75.03],
        [77.1, 79.26, 76.13, 74.34, 72.01],
        [76.1, 76.35, 78.26, 75.67, 77.86],
        [77.6, 75.46, 77.18, 78.2, 76.41],
        [75.2, 74.43, 74.22, 76.24, 79.26],
    ]),
    "ARI": np.array([
        [27.98, 28.72, 25.42, 25.42, 26.97],
        [26.01, 26.21, 28.53, 26.30, 25.51],
        [26.24, 26.88, 26.7, 28.7, 25.62],
        [24.98, 27.06, 25.26, 26.8,28.19],
        [24.05, 24.13, 24.02, 25.46, 27.0],
    ]),
    "NMI": np.array([
        [35.95, 37.78, 36.23, 32.4, 32.2],
        [32.97, 35.99, 37.45, 36.24, 33.5],
        [34.12, 32.74, 34.18, 37.40, 36.1],
        [32.05, 33.85, 33.88, 34.17, 37.4],
        [31.14, 32.96, 33.72, 33.54, 33.57],
    ]),
    "F1": np.array([
        [67.26, 63.12, 65.66, 64.867, 63.11],
        [65.15, 63.29, 66.3, 64.14, 66.01],
        [64.18, 64.35, 65.28, 65.25, 64.76],
        [62.13, 62.81, 62.69, 66.29, 66.3],
        [63.25, 64.43, 62.38, 63.24, 62.29],
    ]),
}

z_max = {"ACC": 90, "ARI": 40, "NMI": 40, "F1": 70}

# 设置颜色映射
cmap = sns.color_palette("light:#0080FF", as_cmap=True)

# 创建横排4图
fig = plt.figure(figsize=(18, 4))

for i, (name, data) in enumerate(metric_dict.items()):
    z = np.rot90(data).T
    norm = colors.BoundaryNorm(boundaries=np.linspace(np.min(z), np.max(z), 100), ncolors=cmap.N)

    ax = fig.add_subplot(1, 4, i + 1, projection='3d')
    ax.plot_surface(X, Y, z, facecolors=cmap(norm(z)), shade=False, edgecolor='k', linewidth=0.3)
    ax.plot_surface(X, Y, np.zeros_like(z), facecolors=cmap(norm(z)), shade=False, edgecolor='k', linewidth=0.3)

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=12)
    ax.set_yticks(y)
    ax.set_yticklabels(y_labels, fontsize=14)
    ax.set_zlabel(f"{name} (%)", rotation=90, fontsize=14)
    ax.set_xlabel(r'$\alpha_1$', fontsize=14)
    ax.set_ylabel(r'$\alpha_2$',fontsize=14)
    ax.tick_params(axis='both', labelsize=12)  # 刻度字体

    # ax.set_title(name)
    ax.set_zlim(0, z_max[name])
    ax.view_init(elev=18, azim=-50)

    # 美化
    ax.set_facecolor('white')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.line.set_color((1, 1, 1, 0))
    ax.yaxis.line.set_color((1, 1, 1, 0))
    ax.zaxis.line.set_color((1, 1, 1, 0))

plt.subplots_adjust(wspace=0.2, hspace=0.15, left=0.029, bottom=0.04,right=0.9,top=1)

plt.tight_layout()
plt.show()
# plt.savefig("./output/param.png", dpi= 600)
