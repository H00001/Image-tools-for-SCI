import matplotlib.pyplot as plt
import numpy as np

labels = ['SP', 'GK', 'RW', 'WL', "HRW"]
ACC = [42.1, 41.9, 42.5, 42.9, 77]
NMI = [50.2, 51.7, 51.1, 50.5, 62]
ARI = [24.2, 23.6, 23.4, 24.4, 34]
F1 = [42.1, 41.7, 42.5, 43.5, 55]

x = np.arange(len(labels))

colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B3']

fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)  # 2列1行，y轴共享

# 左图: ACC 和 NMI
axs[0].plot(x, ACC, marker='o', linestyle='-', color=colors[0], linewidth=3, markersize=10, alpha=0.8, label='ACC')
axs[0].plot(x, NMI, marker='o', linestyle='-', color=colors[1], linewidth=3, markersize=10, alpha=0.8, label='NMI')
axs[0].plot(x, ARI, marker='o', linestyle='-', color=colors[2], linewidth=3, markersize=10, alpha=0.8, label='ARI')
axs[0].plot(x, F1, marker='o', linestyle='-', color=colors[3], linewidth=3, markersize=10, alpha=0.8, label='F1')

axs[0].set_xticks(x)
axs[0].set_xticklabels(labels, fontsize=22, rotation=0)
axs[0].set_ylabel('SM', fontsize=26)
# axs[0].set_xlabel('SM', fontsize=26)
axs[0].set_ylim(10, 100)
axs[0].grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.4)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].spines['left'].set_color('#888888')
axs[0].spines['bottom'].set_color('#888888')
axs[0].legend(fontsize=20, ncol=2)

# 右图: ARI 和 F1
axs[1].plot(x, ACC, marker='o', linestyle='-', color=colors[0], linewidth=3, markersize=10, alpha=0.8, label='ACC')
axs[1].plot(x, NMI, marker='o', linestyle='-', color=colors[1], linewidth=3, markersize=10, alpha=0.8, label='NMI')
axs[1].plot(x, ARI, marker='o', linestyle='-', color=colors[2], linewidth=3, markersize=10, alpha=0.8, label='ARI')
axs[1].plot(x, F1, marker='o', linestyle='-', color=colors[3], linewidth=3, markersize=10, alpha=0.8, label='F1')

axs[1].set_xticks(x)
axs[1].set_xticklabels(labels, fontsize=22, rotation=0)
axs[1].set_ylabel('SM-BIO', fontsize=26)
axs[1].set_ylim(10, 100)
axs[1].grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.4)
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_color('#888888')
axs[1].spines['bottom'].set_color('#888888')
axs[1].legend(fontsize=20, ncol=2)


axs[0].tick_params(axis='y', labelsize=22)
axs[1].tick_params(axis='y', labelsize=32)
plt.tight_layout()
# plt.show()
plt.savefig("output/GK.png", dpi=600)
