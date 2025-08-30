import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def adjust_brightness(color, factor):
    import matplotlib.colors
    return tuple([min(1, c * factor) for c in matplotlib.colors.to_rgb(color)])


datasets = {
    "ACM": np.array([
        [0.8833, 0.9309, 0.8860, 0.9170, 0.8539],
        [0.8793, 0.9313, 0.8853, 0.9168, 0.8537],
        [0.6923, 0.8051, 0.6968, 0.7700, 0.6144],
        [0.6522, 0.7477, 0.6640, 0.7104, 0.5489],
    ]),
    "CITE": np.array([
        [0.7121, 0.7166, 0.6751, 0.6438, 0.6261],
        [0.6278, 0.6329, 0.6216, 0.6261, 0.5983],
        [0.4737, 0.4799, 0.4436, 0.3923, 0.3512],
        [0.4422, 0.4471, 0.4347, 0.4018, 0.3567],
    ]),
    "REUT": np.array([
        [0.8016, 0.8312, 0.7821, 0.7226, 0.6239],
        [0.7663, 0.7907, 0.7484, 0.6708, 0.5719],
        [0.6008, 0.6628, 0.5499, 0.4437, 0.2496],
        [0.5990, 0.6318, 0.5380, 0.4049, 0.3464],
    ]),
    "ENZYMES": np.array([
        [0.7883, 0.8069, 0.7874, 0.7585, 0.7488],
        [0.5463, 0.5590, 0.5458, 0.5103, 0.5041],
        [0.4222, 0.4761, 0.4207, 0.2845, 0.2648],
        [0.3332, 0.3620, 0.3317, 0.2546, 0.2316],
    ]),
    "HHAR": np.array([
        [0.7192, 0.8800, 0.8346, 0.6944, 0.4881],
        [0.6883, 0.8837, 0.8285, 0.6588, 0.4487],
        [0.6101, 0.7792, 0.7354, 0.6102, 0.3675],
        [0.7046, 0.8367, 0.8079, 0.6995, 0.4489],
    ]),
}

colors = ['#ff7793', '#d0d2ff', '#fffbcb', '#f8baf7']
metric_labels = ['ACC', 'F1', 'ARI', 'NMI']
lambda_labels = ['0.01', '0.1', '1', '10', '100']

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 32

fig = plt.figure(figsize=(20, 12))

for idx, name in enumerate(["ACM", "CITE", "REUT", "ENZYMES", "HHAR", "Legend"]):
    if idx == 5:
        ax = fig.add_subplot(2, 3, idx + 1)
        ax.axis('off')
        for i, (color, label) in enumerate(zip(colors, metric_labels)):
            rect_x = 0.3  # ← 向右移动整个图例块
            rect_y = 0.6 - i * 0.15
            ax.add_patch(plt.Rectangle((rect_x, rect_y), 0.1, 0.1, facecolor=color, edgecolor='black'))
            ax.text(rect_x + 0.15, rect_y + 0.05, label, fontsize=32, weight='bold', va='center')
        continue

    ax = fig.add_subplot(2, 3, idx + 1, projection='3d')
    data = datasets[name]

    xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)
    dx = 0.85
    dy = 0.85
    dz = data.flatten()

    for y, color in zip(np.unique(ypos), colors):
        alpha = 0.7 + 0.1 * y
        ax.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y],
                 dx, dy, dz[ypos == y],
                 color=color, edgecolor='black', zsort='average', alpha=alpha)

    xticks_positions = [0.3, 1.5, 2.5, 3.5, 4.7]  # 控制0.01和0.1间距
    yticks_positions = [0.3, 1.5, 2.5, 3.7]
    ax.set_xticks(xticks_positions)
    ax.set_xticklabels(lambda_labels, fontsize=32, weight='bold',  rotation = 25)  # 控制字体粗细
    ax.set_yticks(yticks_positions)
    ax.set_yticklabels([''] * len(metric_labels))
    ax.set_zlim(0, 1)
    ax.set_zticks([0.0, 0.25, 0.50, 0.75, 1.0])
    ax.set_zticklabels(['0.0', '0.25', '0.50', '0.75', '1.00'], fontsize=30, weight='bold', rotation=0)
    ax.tick_params(axis='z', labelsize=35, pad=15)
    
    ax.tick_params(axis='x', pad=2)
    ax.tick_params(axis='y', pad=15)
    ax.set_xlabel(f'$\lambda$', fontsize=32, labelpad=20)
    fig.patch.set_alpha(0)

# 设置坐标轴背景透明
    ax.patch.set_alpha(0)


    ax.set_ylabel(name, fontsize=30, labelpad=3, rotation=25, weight='bold')
    if name == "ENZYMES":
        ax.yaxis.set_label_coords(-0.1, 0.25)  # 向下移动 ENZYMES 标签（适当调这个值）
    else:
        ax.yaxis.set_label_coords(-0.1, 0.35)


    if name in ["REUT", "HHAR"]:
        ax.set_zlabel('Score', fontsize=32, labelpad=35, weight='bold')
    else:
        ax.set_zlabel('', fontsize=32, labelpad=35, weight='bold')

    ax.view_init(elev=22, azim=132)
    ax.grid(False)

plt.subplots_adjust(wspace=-0.1, hspace=-0.08, left=0.00, right=0.95, top=0.95, bottom=0.05)
plt.savefig("Modified_Scores_Hidden_LambdaCloser.png", dpi=1200)
plt.show()
