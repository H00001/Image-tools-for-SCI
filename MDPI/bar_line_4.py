import matplotlib.pyplot as plt
import numpy as np

labels = ['Base', '-A', '-B', 'Ours']
labels1 = ['COX2', 'BZR', 'COLLAB', 'Letter-low']
# 使用更现代、协调的配色方案
colors = ['#C42708', '#558A86', '#4CE425', '#182738']  # 优雅配色（tableau混合）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 15
plt.rcParams['axes.unicode_minus'] = False

def tp(matrix):
    return np.array(matrix).T

data_ACC = [
    [50.99, 40.37, 40.01, 14.74],
    [71.78, 75.75, 54.24, 36.19],
    [73.24, 77.67, 54.88, 32.36],
    [81.7, 80.13, 58.36, 44.25],
]

data_NMI = [
    [2.37, 2.22, 2.78, 3.21],
    [5.6, 2.95, 4.5, 41.46],
    [6.2, 3.52, 4.4, 40.58],
    [9.9, 5.39, 5.9, 53.81]
]

data_ARI = [
    [1.76, 2.11, 5.18, 10.35],
    [5.94, 5.45, 7.48, 17.23],
    [4.27, 4.87, 9.89, 18.05],
    [6.33, 7.45, 11.37, 26.18],
]

data_F1 = [
    [44.00, 34.37, 33.41, 16.74],
    [68.78, 70.75, 47.24, 39.99],
    [70.24, 69.82, 48.78, 38.08],
    [79.99, 75.20, 53.66, 42.35],
]

data_use_ACC = tp(data_ACC)
data_use_NMI = tp(data_NMI)
data_use_ARI = tp(data_ARI)
data_use_F1 = tp(data_F1)

x = np.arange(len(labels))
width = 0.2

fig, axes = plt.subplots(1, 4, figsize=(28, 5), sharey=False)
new_order = [data_use_NMI, data_use_ACC, data_use_F1, data_use_ARI]
new_titles = ['NMI', 'ACC', 'F1', 'ARI']
new_min_max = [[0, 55], [0, 100], [0, 90], [0, 30]]

for i, (ax, data, title, limits) in enumerate(zip(axes, new_order, new_titles, new_min_max)):
    rects1 = ax.bar(x - 1.5 * width, np.array(data[0]), width, label=labels1[0], 
                    color=colors[0], edgecolor='black', linewidth=0.7, alpha=0.9)
    rects2 = ax.bar(x - 0.5 * width, np.array(data[1]), width, label=labels1[1], 
                    color=colors[1], edgecolor='black', linewidth=0.7, alpha=0.9)
    rects3 = ax.bar(x + 0.5 * width, np.array(data[2]), width, label=labels1[2], 
                    color=colors[2], edgecolor='black', linewidth=0.7, alpha=0.9)
    rects4 = ax.bar(x + 1.5 * width, np.array(data[3]), width, label=labels1[3], 
                    color=colors[3], edgecolor='black', linewidth=0.7, alpha=0.9)

    for rects in [rects1, rects2, rects3, rects4]:
        for bar in rects:
            height = bar.get_height()
            # ax.annotate(f'{height:.1f}',
            #             xy=(bar.get_x() + bar.get_width() / 2, height),
            #             xytext=(0, 4), 
            #             textcoords="offset points",
            #             ha='center', va='bottom',
            #             fontsize=10, color='black')

    ax.set_title(f'{title}', fontsize=17, fontweight='bold')
    if i == 0:
        ax.set_ylabel('Score (%)', fontsize=17)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=15)
    ax.set_ylim(limits[0], limits[1])
    ax.legend(fontsize=13, loc='upper center', ncol=2, frameon=False)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

fig.tight_layout()
plt.show()
# plt.savefig("module_abl.png", dpi=600)