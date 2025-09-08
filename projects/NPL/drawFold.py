import matplotlib.pyplot as plt
import numpy as np


datasets = ['HHAR', 'REUT']
dataset_titles = ['HHAR', 'REUT']
metrics = ['ACC', 'NMI']
# Data for the two datasets
labels = ['K=1', 'K=3', 'K=5', 'K=10']
markers = ['o', 'P', '*', '^']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
linewidth = 2
markersize = 0
alpha = 0.8


HHAR_OURS_ACC = [87.4, 89.2, 88.5, 87.5]
HHAR_SDCN_ACC = [80,82,85,79]
HHAR_DAEGC_ACC = [77,78,71,63]
HHAR_AGCC_ACC = [87.2,87.0,88.0,87.2]


HHAR_OURS_NMI = [83.2, 84.3, 83.2, 82.5]
HHAR_SDCN_NMI = [79,79.5,80,79.2]
HHAR_DAEGC_NMI = [69,69,62,60.3]
HHAR_AGCC_NMI = [81,81.5,81.2,82]



REUT_OURS_ACC =   [81.9, 83.3, 82.6, 82.3]  # ACC

REUT_SDCN_ACC = [78.6,77.8,77.9,78.8]
REUT_DAEGC_ACC = [38,66,69,71]
REUT_AGCC_ACC = [79.4,79.6,79.5,79.5]


REUT_OURS_NMI =     [61.2, 64.0, 63.2, 61.7]
REUT_SDCN_NMI = [52,50,50.1,51]
REUT_DAEGC_NMI = [5,32,41,42]
REUT_AGCC_NMI = [57,57.2,54.4,53.1]

# Set positions for the bars
x = np.arange(len(labels))

# Create the figure and axes with 2 columns
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 12), sharey=False)
for j, dataset in enumerate(datasets):
    for i, metric in enumerate(metrics):
        axes[i,j].set_facecolor('#f6f4ff')  # 单个子图背景

        # 获取数据

        axes[i, j].grid(True, axis='y', linestyle='-', linewidth=1, color='white')  # 白色实线横向网格
        axes[i, j].grid(True, axis='x', linestyle='-', linewidth=1, color='white')  # 白色实线竖向网格

    # 根据数据集名称和度量名称动态获取数据

        # 绘制曲线
        axes[i, j].plot(x, globals()[f"{dataset}_OURS_{metric}"], marker=markers[0], color=colors[0], linestyle='-', linewidth=linewidth, markersize=markersize, alpha=alpha, label="OURS")
        axes[i, j].plot(x, globals()[f"{dataset}_SDCN_{metric}"], marker=markers[1], color=colors[1], linestyle='-', linewidth=linewidth, markersize=markersize, alpha=alpha, label="SDCN")
        axes[i, j].plot(x, globals()[f"{dataset}_DAEGC_{metric}"], marker=markers[2], color=colors[2], linestyle='-', linewidth=linewidth, markersize=markersize, alpha=alpha, label="DAGEC")
        axes[i, j].plot(x, globals()[f"{dataset}_AGCC_{metric}"], marker=markers[3], color=colors[3], linestyle='-', linewidth=linewidth, markersize=markersize, alpha=alpha, label="AGCC")

        # 设置标题和标签
        if i==0:
            axes[i, j].set_title(dataset_titles[j], fontsize=22)
        axes[i, j].set_xticks(x)
        axes[i, j].set_xticklabels(labels, fontsize=22)
        if j==0:
            axes[i, j].set_ylabel('ACC (%)' if i==0 else 'NMI (%)', fontsize=22)
        axes[i, j].tick_params(axis='y', labelsize=22)

        # axes[i, j].legend(fontsize=18, title="Metrics", title_fontsize=22)
        axes[i, j].legend(loc='lower center', fontsize=13, ncol=4)


        if i==0:
            if j==0:
                axes[i, j].set_ylim(60, 90)
            else:
                axes[i, j].set_ylim(30,85)

        else:
            if j==0:
                axes[i, j].set_ylim(55, 85)
            else:
                axes[i, j].set_ylim(0, 70)

        axes[i, j].grid(True, axis='y', linestyle='--', linewidth=0.7)


plt.tight_layout(rect=[0, 0.05, 1, 1])


plt.subplots_adjust(hspace=0.185)

# Show the plots
plt.savefig("./NPL/k-hyper-1.png", dpi=600)
# plt.show()

