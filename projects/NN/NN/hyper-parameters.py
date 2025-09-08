import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns

# 标签
x_labels = ['100', '10', '1', '0.1', '0.01']
y_labels = ['0.01', '0.1', '1', '10', '100']
x = np.arange(len(x_labels))
y = np.arange(len(y_labels))
X, Y = np.meshgrid(x, y)

SM = { "ACC": np.array([[75.7, 76.1, 74.3, 75.4, 75.0], 
                        [77.1, 76.2, 76.5, 74.0, 72.0], 
                        [76.1, 76.3, 78.6, 75.7, 77.8], 
                        [77.6, 75.5, 77.1, 79.2, 76.4],
                        [75.2, 74.4, 74.2, 76.2, 78.6], ]), 
    "NMI": np.array([   [25.9, 26.7, 25.4, 25.2, 26.9],
                        [26.0, 26.2, 28.5, 26.3, 25.5], 
                        [26.24, 26.8, 26.7, 28.7, 25.62],
                        [24.98, 27.1, 25.26, 26.8,28.19], 
                        [24.05, 24.2, 24.02, 25.46, 27.0], ]), 
    "ARI": np.array([   [33.95, 34.78, 36.23, 32.4, 32.2], 
                        [32.97, 36.99, 37.45, 36.24, 33.5], 
                        [34.12, 32.74, 34.18, 37.40, 36.1], 
                        [32.05, 33.85, 33.88, 34.17, 37.4], 
                        [31.14, 32.96, 33.72, 33.54, 33.57], ]),
    "F1": np.array([    [62.26, 63.12, 65.66, 64.87, 63.11], 
                        [65.15, 63.29, 66.3, 64.14, 66.01], 
                        [64.18, 64.35, 67.28, 65.25, 64.76],                           
                        [62.13, 62.81, 62.69, 66.29, 66.3], 
                        [63.25, 64.43, 62.38, 63.24, 62.29], ]), } 
SM_BIO = { "ACC": np.array([    [70.7, 71.12, 71.0, 72.42, 73.03],
                                [71.1, 71.36, 73.13, 74.3,73.01], 
                                [71.4, 72.35, 74.2, 74.6, 75.86], 
                                [72.6, 73.5, 72.2, 75.6, 74.41], 
                                [73.2, 73.43, 72.2, 72.24, 72.3], ]), 
           "NMI": np.array([ [7.9,  8.5,  9.2,  10.4, 12.2], 
                             [10.6, 11.3, 13.5, 11.2, 13.5], 
                             [12.4, 13.5, 16.8, 14.6, 15.1], 
                             [14.0, 15.8, 17.2, 15.4, 14.4], 
                             [14.1, 15.3, 16.7, 16.3, 17.5], ]), 
            "ARI": np.array([
                        [20.98, 21.72, 22.42, 24.42, 24.97], 
                        [22.01, 24.21, 25.53, 26.30, 25.51],  
                        [23.24, 25.88, 26.7, 27.7, 25.62], 
                        [22.98, 23.06, 28.26, 27.8,27.19], 
                        [21.05, 22.13, 24.02, 27.46, 25.0], ]), 
            "F1": np.array([
                        [58.5, 61.7,  62.6, 63.1, 62.2],
                        [59.1, 62.3, 63.3, 64.4, 63.0], 
                        [61.2, 63.3, 63.4, 64.2, 61.76], 
                        [62.1, 62.8, 63.6, 64.5, 62.3], 
                        [60.8, 61.4, 62.3, 62.1, 62.0], ]), } 
SM_BIO_SY = { "ACC": np.array([ [70.8, 71.1, 71.5, 72.42, 73.0],
                                [71.1, 71.2, 73.1, 74.34, 72.0], 
                                [72.1, 72.8, 74.4, 73.9, 73.8], 
                                [71.6, 72.4, 72.9, 74.2, 73.4],
                                [70.2, 72.4, 72.22, 72.5, 72.3], ]), 
        "NMI": np.array([   [15.9, 17.7, 18.2, 18.4, 18.2], 
                            [14.9, 15.9, 19.7, 18.2, 20.5], 
                            [16.1, 17.7, 20.2, 19.4, 19.1],
                            [15.0, 16.8, 21.8, 18.4, 18.3], 
                            [16.1, 17.9, 17.7, 17.5, 18.2] ]), 
        "ARI": np.array([   [22.9, 24.7, 25.4, 25.4, 27.3], 
                            [23.0, 26.1, 26.5, 26.3, 26.5], 
                            [23.8, 26.8, 26.2, 25.7, 27.6], 
                            [24.5, 25.6, 27.4, 26.4, 26.5], 
                            [24.7, 24.3, 25.0, 25.2, 25.3], ]), 
        "F1": np.array([    [58.9, 59.6, 60.6, 61.5, 61.7], 
                            [59.1, 61.7, 63.3, 62.3, 61.0], 
                            [60.2, 62.8, 63.4, 63.8, 62.7], 
                            [61.3, 62.9, 62.6, 63.1, 62.3], 
                            [62.2, 62.0, 62.2, 62.8, 62.8], ]), }
SN = { "ACC": np.array([    [65.7, 67.0, 68.9, 68.4, 64.5], 
                            [67.4, 67.1, 66.4, 68.5, 64.01], 
                            [67.1, 67.5, 69.2, 69.1, 67.4], 
                            [67.6, 67.6, 67.3, 69.2, 66.41], 
                            [65.2, 66.7, 68.2, 68.0, 68.1], ]),
        "NMI": np.array([ 
            [26.9, 27.7, 28.4, 27.4, 27.2], 
            [30.9, 31.2, 30.3, 29.2, 29.5], 
            [32.1, 31.7, 33.1, 31.4, 30.1], 
            [30.0, 30.5, 34.8, 32.1, 29.4], 
            [29.1, 30.9, 31.7, 30.5, 28.5], ]), 
        "ARI": np.array([ 
            [25.9, 27.7, 28.4, 29.4, 30.9], 
            [27.0, 29.2, 29.5, 31.3, 27.5], 
            [28.2, 30.9, 34.2, 33.5, 31.6], 
            [28.9, 27.1, 35.2, 34.8, 30.3], 
            [27.6, 24.2, 32.0, 34.5, 29.0], ]), 
        "F1": np.array([ 
                [48.2, 49.1, 53.7, 55.8, 54.1], 
                [48.3, 51.2, 52.3, 56.1, 56.0], 
                [48.1, 53.6, 57.3, 56.5, 55.7], 
                [49.1, 52.8, 55.6, 57.9, 56.3],
                [48.2, 51.4, 54.3, 55.2, 56.9], ]), }
CV = { "ACC": np.array([ [30.2, 32.12, 34.03, 35.4, 35.03], 
                         [31.1, 33.4, 36.13, 36.3, 36.01], 
                         [32.1, 34.35, 38.6, 37.8, 36.86], 
                        [33.6, 35.46, 36.18, 38.2, 37.41], 
                        [34.2, 36.43, 36.22, 38.4, 37.3], ]), 
        "NMI": np.array([[25.98, 26.7, 28.4, 32.4, 30.9], 
                         [26.01, 27.2, 32.5, 33.0, 31.5], 
                         [27.24, 30.8, 37.7, 34.5, 32.6], 
                         [29.98, 31.5, 35.2, 34.8, 33.1], 
                         [28.05, 30.2, 34.0, 33.4, 32.0], ]), 
        "ARI": np.array([ [16.7, 16.8, 18.2, 22.4, 21.2],
                          [17.2, 18.6, 22.3, 24.7, 22.5],
                          [18.9, 19.5, 24.5, 24.0, 26.1], 
                          [22.3, 23.7, 23.6, 23.9, 22.4], 
                          [20.4, 21.1, 22.8, 23.5, 21.8], ]),
         "F1": np.array([[25.5, 27.2, 29.7, 30.8, 32.4], 
                         [26.5, 28.3, 32.3, 32.5, 32.0], 
                         [27.6, 29.3, 34.6, 34.5, 32.5], 
                         [27.5, 30.1, 33.6, 36.1, 31.1], 
                         [26.2, 29.5, 32.3, 35.2, 30.2], ]), }

# 数据集（你可以继续加第四组、第五组）
datasets = {
    "SM": SM,
    "SM-BIO": SM_BIO,
    "SM-BIO-SY": SM_BIO_SY,
    "SN":SN,
    "CV":CV
    # "SM_X": SM_X,
    # "SM_Y": SM_Y,
}

# z轴上限
z_max = {"ACC": 90, "ARI": 40, "NMI": 40, "F1": 70}

# 颜色映射
cmap = sns.color_palette("light:#0080FF", as_cmap=True)

# 创建 5行4列 图
fig, axes = plt.subplots(len(datasets), 4,
                         figsize=(14, 16),
                         subplot_kw={'projection': '3d'})

if len(datasets) == 1:
    axes = np.expand_dims(axes, 0)  # 保证二维

for row, (dname, dataset) in enumerate(datasets.items()):
    for col, (metric, data) in enumerate(dataset.items()):
        basic = 0
        max = None
        z = np.rot90(data).T
        norm = colors.BoundaryNorm(boundaries=np.linspace(np.min(z), np.max(z), 100), ncolors=cmap.N)

        ax = axes[row, col]
        ax.plot_surface(X, Y, z, facecolors=cmap(norm(z)),
                        shade=False, edgecolor='k', linewidth=0.3)
        if col ==1 and row ==1:
            basic = 0
            max = 21
        elif col==1 and row ==2:
            basic = 0
            max = 31
        elif (col==0 or col == 3) and row ==4:
            basic = 0
            max = 41
        elif col ==0 and row == 4:
            basic = 0
            max = 51
        elif (col==0 and row !=4) or col==3:
            basic = 40

        else:
            basic = 0
        
        ax.plot_surface(X, Y, np.zeros_like(z)+basic, facecolors=cmap(norm(z)),
                        shade=False, edgecolor='k', linewidth=0.3)
        if max == None:
            ax.set_zlim(basic, z_max[metric])
        else:
            ax.set_zlim(basic, max)

        ax.set_xticks(x)
        ax.set_xticklabels(x_labels, fontsize=9.5, rotation=40)
        ax.set_yticks(y)
        ax.set_yticklabels(y_labels, fontsize=9.5, rotation=-40)
      
        # ax.set_zlabel(f"{metric} (%)", fontsize=12, rotation=90)
        ax.set_xlabel(r'$\alpha_1$', fontsize=12, labelpad=0)
        ax.set_ylabel(r'$\alpha_2$', fontsize=12, labelpad=0)

        # for i, label in enumerate(x_labels):
        #     ax.text(x[i], -0.5, 0, label,  # 这里 (x[i], y, z) 是放置位置
        #     rotation=40,
        #     ha='right', va='center', fontsize=10)




        ax.view_init(elev=18, azim=-50)

        ax.tick_params(axis='x', pad=-4)  # 数字越小越靠近轴
        ax.tick_params(axis='y', pad=-4)
        ax.tick_params(axis='z', pad=1)

        # # 第一行加标题（指标名）3
        # if row == 0:
        #     ax.set_title(metric, fontsize=14)

        # 第一列加行名（数据组）
        if row ==0:
            if col == 0:
                ax.set_title("ACC(%)",fontsize=16,pad=-2)
            elif col == 1:
                ax.set_title("NMI(%)",fontsize=16,pad=-2)
            elif col == 2:
                ax.set_title("ARI(%)",fontsize=16,pad=-2)
            else:
                ax.set_title("F1(%)",fontsize=16,pad=-2)
        if col == 0:
            ax.text2D(-0.10, 0.5, dname,
                     transform=ax.transAxes, fontsize=16, rotation=90,
                     va='center', ha='right')

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.95, wspace=0.0, hspace=0.1)
# plt.tight_layout()
fig.canvas.draw()

plt.savefig('./output/addition_hyper_alpha.png', dpi=600)


# plt.show()
