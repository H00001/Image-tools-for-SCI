import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.transforms as mtransforms

plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 18
subgraph_ratios = [1, 5, 10, 15, 20, 30, 40, 50]
selected_indices = [0, 2, 4, 5, 6, 7]
metrics = ["SM","MY", "MB", "MBY"]

sm1 = np.array([
    [60.84, 69.09, 72.23, 77.04, 60.39],
    [64.00, 67.50, 75.47, 70.10, 58.20],
    [62.13, 63.39, 74.44, 71.12, 63.27],
    [60.92, 62.75, 73.83, 70.16, 64.18]
]).T
sm2 = np.array([
    [23.23, 27.87, 31.48, 28.12, 23.45],
    [23.16, 24.43, 31.72, 26.35, 23.09],
    [20.55, 24.62, 27.23, 22.40, 20.91],
    [20.02, 21.38, 24.57, 23.27, 20.66]
]).T
sm3 = np.array([
    [25.32, 35.64, 37.17, 28.45, 24.03],
    [24.88, 28.77, 35.69, 29.39, 23.74],
    [23.41, 26.05, 31.50, 24.92, 22.38],
    [22.10, 24.66, 28.42, 23.20, 20.81]
]).T
sm4 = np.array([
    [61.35, 67.28, 71.21, 73.10, 60.12],
    [62.40, 63.87, 70.00, 66.43, 60.76],
    [63.19, 64.44, 67.39, 64.77, 61.33],
    [60.97, 63.10, 65.83, 63.85, 60.22]
]).T

# colors1 = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd',
        #    '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd']
colors1 = [ '#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd',
          '#1f77b4', '#2ca02c', '#ff7f0e',  '#9467bd']

def draw_3d_subplot1(ax, dataset, title, subgraph_ratios1, min, max):
    somevalue = min
    selected_indices = [0, 1, 2, 3, 4]
    for i in selected_indices:
        ratio = subgraph_ratios1[i]
        x = list(range(len(metrics)))
        y = [ratio] * len(metrics)
        z = dataset[i]
        alpha = 1# 0.2 + 0.5 * (1 - i / len(metrics))
        # ax.plot(x, y, z, color=colors1[i], linewidth=2, alpha=alpha)

    for metric_idx, metric in enumerate(metrics):
        y_values = subgraph_ratios1
        z_values = [dataset[i][metric_idx] for i in range(len(subgraph_ratios1))]
        x_position = metric_idx
        alpha = 0.3 + 0.4* (1 - metric_idx / len(metrics))

        ax.plot(
            [x_position] * len(selected_indices),
            [y_values[i] for i in selected_indices],
            [z_values[i] for i in selected_indices],
            color=colors1[metric_idx],
            linewidth=2,
            alpha=alpha,
            zorder=metric_idx *5 -1
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
            s=60,
            edgecolor='#333333',
            zorder=metric_idx *5
        )

        for i in selected_indices:
            ax.plot(
            [x_position, x_position],  # 相同的X坐标
            [y_values[i], y_values[i]],  # 相同的Y坐标
            [z_values[i], somevalue],  # 从数据点到最低点
            color=colors1[metric_idx+4],
            linestyle='--',  # 虚线样式
            alpha=alpha +0.1,  # 比主线条更透明
            linewidth=2,
            zorder=metric_idx *5 +1  # 确保在主要元素下方
        )
    #     ax.plot(
    #     [0,0],  # X坐标相同（垂直方向）
    #     [0,0],  # Y坐标相同（保持垂直）
    #     [10, z_values[i]],  # Z坐标从0到当前点（垂直线）
    #     color=colors1[metric_idx],
    #     linestyle='--',  # 虚线样式（可选）
    #     alpha=0.5,  # 透明度（可选）
    #     linewidth=1,  # 线宽（可选）
    #     zorder=5
    # )
        
    #     ax.plot(
    #     [1,0],  # X坐标相同（垂直方向）
    #     [0,0],  # Y坐标相同（保持垂直）
    #     [10, z_values[i]],  # Z坐标从0到当前点（垂直线）
    #     color=colors1[metric_idx],
    #     linestyle='--',  # 虚线样式（可选）
    #     alpha=0.5,  # 透明度（可选）
    #     linewidth=1,  # 线宽（可选）
    #     zorder=5
    # )

# # 找出最高和次高的点
#         points = list(zip(
#     [y_values[i] for i in selected_indices],
#     [z_values[i] for i in selected_indices]
# ))

# # 按z值排序（假设z值代表高度）
#         sorted_points = sorted(points, key=lambda x: x[1], reverse=True)

#         if len(sorted_points) >= 1:
#     # 标注最高点
#             top_point = sorted_points[0]
#             ax.text(
#         x_position, 
#         top_point[0], 
#         top_point[1], 
#         f'{top_point[1]:.2f}', 
#         color='black',
#         ha='center',
#         va='top',
#         fontsize=10,
#         zorder=11
#     )

#         if len(sorted_points) >= 2:
#     # 标注次高点
#             second_point = sorted_points[1]
#             ax.text(
#         x_position, 
#         second_point[0], 
#         second_point[1], 
#         f'{second_point[1]:.2f}', 
#         color='black',
#         ha='center',
#         va='top',
#         fontsize=10,
#         zorder=11
#     )

    ax.set_xticks([x - 0.5 for x in range(len(metrics))])
    ax.set_xticklabels(metrics, fontsize=20)
    ax.annotate(
    'Settings',  # 标签文本
    xy=(0.05, 0.17),  # 标签位置，(x, y) 相对于坐标轴的位置
    xycoords='axes fraction',  # 坐标系：相对于坐标轴的百分比位置
    fontsize=18,  # 字体大小
    rotation=-51,  # 旋转角度
    ha='center',  # 水平对齐：居中
    va='center',  # 垂直对齐：居中
)
    ax.set_ylabel(title, labelpad=5, fontsize=20)
    # ax.set_xlabel("Settings", labelpad=15, fontsize=20, rotation=20)
    # label = ax.xaxis.label
    # label.set_transform(mtransforms.Affine2D().translate(-2.5, 0) + ax.transAxes)  # 向左平移0.1

    ax.set_yticks(subgraph_ratios1)
    yticklabels = ["1", "5", "10", "15", "20"]
    ax.set_yticklabels(yticklabels, fontsize=24, rotation=0,  )
    ax.set_zlim(somevalue, max)
    ax.tick_params(axis='both', which='major', labelsize=17, width=1.2)
    ax.tick_params(axis='y',pad=-2)

    ax.view_init(elev=16, azim=-19)
    # ax.xaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    # ax.yaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    # ax.zaxis._axinfo["grid"].update({"linewidth": 1, "color": "#dddddd"})
    ax.set_facecolor("#ffffff")

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_alpha(0)
    ax.yaxis.pane.set_alpha(0)
    ax.zaxis.pane.set_alpha(0)
    ax.set_facecolor("none")



fig = plt.figure(figsize=(20, 5))
ax1 = fig.add_subplot(1, 4, 1, projection='3d')
draw_3d_subplot1(ax1, sm1, title=f"$\gamma$", subgraph_ratios1=[1, 10, 20, 30, 40], min=49, max=82)
ax2 = fig.add_subplot(1, 4, 2, projection='3d')
draw_3d_subplot1(ax2, sm2, title=f"$\gamma$", subgraph_ratios1=[1, 10, 20, 30, 40], min=15, max=32)
ax3 = fig.add_subplot(1, 4, 3, projection='3d')
draw_3d_subplot1(ax3, sm3, title=f"$\gamma$", subgraph_ratios1=[1, 10, 20, 30, 40], min=15, max=42)
ax4 = fig.add_subplot(1, 4, 4, projection='3d')
draw_3d_subplot1(ax4, sm4, title=f"$\gamma$", subgraph_ratios1=[1, 10, 20, 30, 40], min=49, max=76)


ax1.text2D(0.075, 0.040,'ACC (%)',rotation=0,  fontsize=16, ha='right', va='top',    bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='#222222',
        boxstyle='round,pad=0.2'
    ))
# 内嵌 Z 轴标签
ax2.text2D(0.075, 0.040, 'NMI (%)',rotation=0,  fontsize=16, ha='right', va='top',    bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='#222222',
        boxstyle='round,pad=0.2'
    ))

ax3.text2D(0.075, 0.040, 'ARI (%)',rotation=0,  fontsize=16, ha='right', va='top',    bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='#222222',
        boxstyle='round,pad=0.2'
    ))

ax4.text2D(0.075, 0.040,'F1 (%)',rotation=-0,  fontsize=16, ha='right', va='top',    bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='#222222',
        boxstyle='round,pad=0.2'
    ))

ax4.xaxis.label.set_position((-5, 0))  # 你可以调整-0.05值来实现更多的平移

# from mpl_toolkits.mplot3d.art3d import text_2d_to_3d
# from matplotlib.patches import FancyBboxPatch
# text = ax2.text(0.5, 0.5, 0.5, "NMI (%)", fontsize=20, ha='right', va='top')

# 转换 2D bbox 到 3D
# bbox = FancyBboxPatch((0, 0), 0.2, 0.1, boxstyle="round,pad=0.2", 
                    #   facecolor='white', alpha=0.7, edgecolor='#222222')
# ax2.add_patch(bbox)
# text_2d_to_3d(bbox, z=0.5)  # 转换到 3D 空间


# ax3.text2D(0.3, 0.8, 'ARI (%)', transform=ax3.transAxes, fontsize=18, ha='right', va='top')
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

plt.subplots_adjust(wspace=-0.012, hspace=0.025, left=0.05, right=0.95, top=1, bottom=0.245)
plt.savefig("./projects/dream1/output/hyper3d.png", dpi=600)
plt.show()
