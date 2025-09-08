import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 18

# 数据定义
subgraph_ratios = [2, 5, 10, 15, 20, 30, 40, 50]
selected_indices = [0, 2, 4, 5, 6, 7]
metrics = ["Cora", "Amazon", "Weibo", "Disney", "Reddit"]

sm = np.array([
    [76.6, 77.7, 78.1, 80.7, 82.1, 83.9, 82.3, 75.0],
    [75.6, 77.6, 81.5, 82.5, 83.2, 82.4, 80.6, 77.5], 
    [78.1, 80.8, 81.9, 81.2, 82.5, 82.6, 81.6, 81.2],
    [72.1, 74.3, 73.8, 73.4, 72.6, 72.6, 71.2, 70.8],
    [60.8, 61.6, 62.4, 63.0, 62.1, 61.8, 61.5, 61.6]
]).T



gamma_1= np.array([
    [81.2, 82.3, 82.6, 82.4, 83.3, 82.2, 81.5, 81.5],
    [76.3, 76.6, 78.8, 78.4, 74.2, 73.4, 72.6, 73.5], 
    [81.7, 80.8, 80.9, 81.2, 81.5, 81.6, 78.3, 78.2],
    [69.1, 68, 68.8, 66.4, 65.6, 64.6, 63.2, 62.8],
        [60.8, 60.6, 61.4, 62.0, 62.1, 62.8, 63.5, 62.6]

]).T

gamma_2= np.array([
    [78.2, 79.3, 80.6, 79.4, 79.3, 79.2, 78.5, 77.5],
    [71.3, 73.6, 71.8, 72.4, 73.2, 74.4, 71.6, 72.5], 
    [82.7, 82.8, 82.9, 83.2, 84.5, 82.6, 81.6, 81.2],
    [67.1, 68.3, 68.8, 68.4, 68.6, 63.6, 65.2, 66.8],
        [63.8, 62.6, 62.4, 63.0, 64.1, 63.8, 62.5, 62.6]

]).T

gamma_3= np.array([
    [84.2, 83.3, 84.6, 83.4, 82.3, 81.2, 82.5, 82.5],
    [72.3, 72.6, 73.8, 73.4, 74.2, 75.4, 75.6, 75.5], 
    [82.7, 82.8, 82.9, 84.2, 84.5, 83.6, 83.6, 83.2],
    [65.1, 66.3, 68.8, 67.4, 66.6, 67.6, 64.2, 65.8],
    [66, 65.6, 65.4, 65.0, 64.1, 64.8, 64.5, 64.6]
]).T

colors1 = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd',
           '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd']

def draw_3d_subplot(ax, dataset, title="", title2=""):
    somevalue = 55
    for i in selected_indices:
        ratio = subgraph_ratios[i]
        x = list(range(len(metrics)))
        y = [ratio] * len(metrics)
        z = dataset[i]
        alpha = 0.3 + 0.5 * (1 - i/len(metrics))
        # ax.plot(x, y, z, color=colors1[i], linewidth=2, alpha=alpha)

    for metric_idx, metric in enumerate(metrics):
        y_values = subgraph_ratios
        z_values = [dataset[i][metric_idx] for i in range(len(subgraph_ratios))]
        x_position = metric_idx
        alpha = 0.2 + 0.5 * (1 - metric_idx/len(metrics))
        ax.plot(
            [x_position] * len(selected_indices),
            [y_values[i] for i in selected_indices],
            [z_values[i] for i in selected_indices],
            color='black',
            linewidth=1,
            alpha=alpha,
            zorder=5
        )
        verts = [list(zip([x_position] * len(y_values), y_values, z_values)) +
                 [(x_position, y_values[-1], somevalue), (x_position, y_values[0], somevalue)]]
        poly = Poly3DCollection(verts, facecolors=colors1[metric_idx], alpha=alpha)
        ax.add_collection3d(poly)
        ax.scatter(
            [x_position] * len(selected_indices),
            [y_values[i] for i in selected_indices],
            [z_values[i] for i in selected_indices],
            color=colors1[metric_idx],
            s=100,
            edgecolor=colors1[metric_idx],
            zorder=10
        )


        for i in selected_indices:
            ax.plot(
            [x_position, x_position],  # 相同的X坐标
            [y_values[i], y_values[i]],  # 相同的Y坐标
            [z_values[i], somevalue],  # 从数据点到最低点
            color=colors1[metric_idx+5],
            linestyle='--',  # 虚线样式
            alpha=alpha +0.3,  # 比主线条更透明
            linewidth=1,
            zorder=metric_idx *5 +1  # 确保在主要元素下方
        )

    ax.set_xlabel(title2, labelpad=23, fontsize=18)
    ax.set_xticks([x - 0.5 for x in range(len(metrics))])
    ax.set_xticklabels(metrics, fontsize=16, rotation=12)

    ax.set_ylabel(title, labelpad=10, fontsize=18)
    ax.set_yticks(subgraph_ratios)
    yticklabels = [f"2", "", "10", "", "20", "30", "40", "50"]
    ax.set_yticklabels(yticklabels, fontsize=16)

    ax.set_zlim(somevalue, 91)
    ax.tick_params(axis='both', which='major', labelsize=16, width=1)

    ax.view_init(elev=21, azim=-32)
    ax.xaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    ax.yaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    ax.zaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))  # 设置x轴平面背景为透明
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))  # 设置y轴平面背景为透明
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))  # 设置z轴平面背景为透明

    ax.tick_params(axis='y', pad=0)

    # ax.set_title(title, fontsize=18, pad=10)


def draw_3d_subplot1(ax, dataset, title="", title2="",subgraph_ratios1=[]):
    somevalue = 55
    selected_indices  = [0,1,2,3,4]
    for i in [0,1,2,3,4]:
        ratio = subgraph_ratios1[i]
        x = list(range(len(metrics)))
        y = [ratio] * len(metrics)
        z = dataset[i]
        alpha = 0.3 + 0.5 * (1 - i/len(metrics))
        # ax.plot(x, y, z, color=colors1[i], linewidth=2, alpha=alpha)

    for metric_idx, metric in enumerate(metrics):
        y_values = subgraph_ratios1
        z_values = [dataset[i][metric_idx] for i in range(len(subgraph_ratios1))]
        x_position = metric_idx
        alpha = 0.2 + 0.5 * (1 - metric_idx/len(metrics))
        ax.plot(
            [x_position] * len(selected_indices),
            [y_values[i] for i in selected_indices],
            [z_values[i] for i in selected_indices],
            color='black',
            linewidth=1,
            alpha=alpha,
            zorder=5
        )
        verts = [list(zip([x_position] * len(y_values), y_values, z_values)) +
                 [(x_position, y_values[-1], somevalue), (x_position, y_values[0], somevalue)]]
        poly = Poly3DCollection(verts, facecolors=colors1[metric_idx], alpha=alpha)
        ax.add_collection3d(poly)
        ax.scatter(
            [x_position] * len(selected_indices),
            [y_values[i] for i in selected_indices],
            [z_values[i] for i in selected_indices],
            color=colors1[metric_idx],
            s=100,
            edgecolor=colors1[metric_idx],
            zorder=10
        )

        for i in selected_indices:
            ax.plot(
            [x_position, x_position],  # 相同的X坐标
            [y_values[i], y_values[i]],  # 相同的Y坐标
            [z_values[i], somevalue],  # 从数据点到最低点
            color=colors1[metric_idx+5],
            linestyle='--',  # 虚线样式
            alpha=alpha +0.3,  # 比主线条更透明
            linewidth=1,
            zorder=metric_idx *5 +1  # 确保在主要元素下方
        )

    ax.set_xlabel(title2, labelpad=20, fontsize=20)
    ax.set_xticks([x - 0.5 for x in range(len(metrics))])
    ax.set_xticklabels(metrics, fontsize=16,rotation=12)

    ax.set_ylabel(title, labelpad=8, fontsize=20)
    ax.set_yticks(subgraph_ratios1)
    yticklabels = [f"3:1", "2:1", "1:1", "1:2", "1:3"]
    ax.set_yticklabels(yticklabels, fontsize=18)

    ax.set_zlim(somevalue, 91)
    ax.tick_params(axis='both', which='major', labelsize=16, width=1.2)

    ax.view_init(elev=21, azim=-32)
    ax.xaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    ax.yaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    ax.zaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})

    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))  # 设置x轴平面背景为透明
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))  # 设置y轴平面背景为透明
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))  # 设置z轴平面背景为透明

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.tick_params(axis='y', pad=0)

    # ax._axis3don = False  # 隐藏3D坐标轴的线
    # ax.set_title(title, fontsize=18, pad=10)


fig = plt.figure(figsize=(18, 4))  # 高度变大，放2行

# 四个子图
ax1 = fig.add_subplot(1, 4, 1, projection='3d')
draw_3d_subplot(ax1, sm, title="K", title2=f"Datasets")

ax2 = fig.add_subplot(1, 4, 2, projection='3d')
draw_3d_subplot1(ax2, gamma_1, title2=f"$\gamma_1=0$",title=f"$\gamma_2:\gamma_3$", subgraph_ratios1=[1, 10, 20, 30, 40])

ax3 = fig.add_subplot(1, 4, 3, projection='3d')
draw_3d_subplot1(ax3, gamma_2, title2=f"$\gamma_2=0$",title=f"$\gamma_1:\gamma_3$",subgraph_ratios1=[1, 10, 20, 30, 40])

ax4 = fig.add_subplot(1, 4, 4, projection='3d')
draw_3d_subplot1(ax4, gamma_3, title2=f"$\gamma_3=0$",title=f"$\gamma_1:\gamma_2$",subgraph_ratios1=[1, 10, 20, 30, 40])
# Set z-labels with proper rotation
for ax in [ ax4]:
    ax.set_zlabel('AUC (%)', labelpad=7, fontsize=20)
    # Manually adjust z-label position if needed
    ax.zaxis.set_rotate_label(False)  # Disable automatic rotation
    ax.zaxis.label.set_rotation(90)   # Set custom rotation

for i, ax in enumerate([ax1, ax2, ax3, ax4]):
    # Add label in the bottom right corner of each subplot
    ax.text2D(1.03, 0.00, "("+ chr(97 + i) +")", transform=ax.transAxes, 
              fontsize=20, fontweight='bold', va='bottom', ha='right')
    


plt.subplots_adjust(wspace=0.125, hspace=-0.015, left=0.05, right=0.95, top=1, bottom=0.045)

# plt.show()
plt.savefig("./projects/GAD/output/hyper_2.png",dpi=600)
plt.show()