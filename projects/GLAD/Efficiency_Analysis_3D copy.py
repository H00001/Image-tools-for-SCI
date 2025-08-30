import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 12
# subgraph_ratios = [1, 5, 10, 15, 20, 30, 40, 50]
# selected_indices = [0, 2, 4, 5, 6, 7]
metrics = ["DHFR","IMDB", "BZR", "COX2"]

import sys
import os

# 获取执行时使用的文件名（可能是相对/绝对路径）
script_path = sys.argv[0]
current_dir = os.path.dirname(__file__)


sm1 = np.array([
    [473, 44.9, 77.5, 130, 67],
    [580, 47.8, 104, 215, 86],
    [94.8, 9,  122, 85, 63],
    [106, 10,  48,127, 62]
]).T
sm2 = np.array([
    [22.05,20.12,16.22, 16.87,   17.16],
    [19.42,21.35,16.32,   16.52, 17.18],
    [18.45,22.40,17.18,  16.61,  18.92],
    [19.91,20.27,17.20,  16.66,  16.37]
]).T


colors1 = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd',
           '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd']

def draw_3d_subplot1(ax, dataset, title, subgraph_ratios1, min, max):
    somevalue = min
    selected_indices = [0, 1, 2, 3, 4]
    for i in selected_indices:
        ratio = subgraph_ratios1[i]
        x = list(range(len(metrics)))
        y = [ratio] * len(metrics)
        z = dataset[i]
        alpha = 0.3 + 0.4 * (1 - i / len(metrics))
        # ax.plot(x, y, z, color=colors1[i], linewidth=2, alpha=alpha)

    for metric_idx, metric in enumerate(metrics):
        y_values = subgraph_ratios1
        z_values = [dataset[i][metric_idx] for i in range(len(subgraph_ratios1))]
        x_position = metric_idx
        alpha = 0.2 + 0.5 * (1 - metric_idx / len(metrics))

        ax.plot(
            [x_position] * len(selected_indices),
            [y_values[i] for i in selected_indices],
            [z_values[i] for i in selected_indices],
            color='black',
            linewidth=2,
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
            alpha=alpha +0.1,  # 比主线条更透明
            linewidth=2,
            zorder=metric_idx *5 +1  # 确保在主要元素下方
        )

    ax.set_xticks([x - 0.5 for x in range(len(metrics))])
    ax.set_xticklabels(metrics, fontsize=14)
    ax.set_ylabel(title, labelpad=18, fontsize=18)
    ax.set_xlabel("Datasets", labelpad=15, fontsize=18, rotation=20)

    ax.set_yticks(subgraph_ratios1)
    yticklabels = ["MUSE","SDGG", "HC-GL",  "CARE", "OURS"]
    ax.set_yticklabels(yticklabels, fontsize=18, rotation=45)
    ax.set_zlim(somevalue, max)
    ax.tick_params(axis='both', which='major', labelsize=17, width=11)
    ax.tick_params(axis='y',pad=-7)

    ax.view_init(elev=18, azim=-30)
    # ax.xaxis._axinfo["grid"].upd5ate({"linewidth": 1, "color": "#dddddd"})
    # ax.yaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    # ax.zaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    ax.set_facecolor("#ffffff")

    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))  # RGBA，最后一个是透明度
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))


fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
draw_3d_subplot1(ax1, sm1, title=f"Methods", subgraph_ratios1=[1, 10, 20, 30, 40], min=0, max=600)
ax2 = fig.add_subplot(1,2 , 2, projection='3d')
draw_3d_subplot1(ax2, sm2, title=f"Methods", subgraph_ratios1=[1, 10, 20, 30, 40], min=10, max=25)
# ax3 = fig.add_subplot(1, 4, 3, projection='3d')
# draw_3d_subplot1(ax3, sm3, title=f"$\gamma$", subgraph_ratios1=[1, 10, 20, 30, 40], min=10, max=40)
# ax4 = fig.add_subplot(1, 4, 4, projection='3d')
# draw_3d_subplot1(ax4, sm4, title=f"$\gamma$", subgraph_ratios1=[1, 10, 20, 30, 40], min=40, max=75)


# ax3.text(0, 82.7,18.5, 'ARI (%)',rotation=-20,  fontsize=16, ha='right', va='top',    bbox=dict(  # 添加半透明背景框（可选）
    #     facecolor='white', 
    #     alpha=0.7, 
    #     edgecolor='#222222',
    #     boxstyle='round,pad=0.2'
    # ))

# ax4.text(0, 82.7,52.5, 'F1 (%)',rotation=-20,  fontsize=16, ha='right', va='top',    bbox=dict(  # 添加半透明背景框（可选）
#         facecolor='white', 
#         alpha=0.7, 
#         edgecolor='#222222',
#         boxstyle='round,pad=0.2'
#     ))
# from mpl_toolkits.mplot3d.art3d import text_2d_to_3d
# from matplotlib.patches import FancyBboxPatch
# text = ax2.text(0.5, 0.5, 0.5, "NMI (%)", fontsize=20, ha='right', va='top')

# 转换 2D bbox 到 3D
# bbox = FancyBboxPatch((0, 0), 0.2, 0.1, boxstyle="round,pad=0.2", 
                    #   facecolor='white', alpha=0.7, edgecolor='#222222')
# ax2.add_patch(bbox)
# text_2d_to_3d(bbox, z=0.5)  # 转换到 3D 空间


ax1.text2D(0.95, 0.75, 'Runtime (ms)', transform=ax1.transAxes, fontsize=18, ha='right', va='top',  bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='#222222',
        boxstyle='round,pad=0.2'
    ))
ax2.text2D(0.95, 0.75, 'Memory (MB)', transform=ax2.transAxes, fontsize=18, ha='right', va='top',bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='#222222',
        boxstyle='round,pad=0.2'
    ))
# ax4.text2D(0.3, 0.8, 'F1 (%)',  transform=ax4.transAxes, fontsize=18, ha='right', va='top')

# ax1.text(
#     0.04, 0.95, 'ACC (%)',  # x=0.02（靠左），y=0.95（靠顶）
#     transform=ax1.transAxes,  # 使用轴坐标系（0-1范围）
#     fontsize=28,
#     fontweight='bold',
#     verticalalignment='top',  # 文本顶部对齐
#     bbox=dict(  # 添加半透明背景框（可选）
#         facecolor='white', 
#         alpha=0.7, 
#         edgecolor='none',
#         boxstyle='round,pad=0.2'
#     )
# )
# 子图角标 (a), (b), ...
# for i, ax in enumerate([ax1, ax2, ax3, ax4]):
#     ax.text2D(0.99, 0.00, "("+ chr(97 + i) +")", transform=ax.transAxes,
#               fontsize=20, fontweight='bold', va='bottom', ha='right')
fig.set_facecolor('white')  # 设置整个图形的背景颜色

# 提取纯文件名
script_name = os.path.basename(sys.argv[0])

plt.subplots_adjust(wspace=0.00, hspace=0.025, left=0.05, right=0.95, top=1, bottom=0.245)
plt.savefig(f"{current_dir}/output/{script_name}.png", dpi=600)
plt.show()
