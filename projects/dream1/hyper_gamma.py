import matplotlib.pyplot as plt
import numpy as np

labels = ['1%', '5%', '10%', '15%', "20%"]
ACC = [[72.2, 74.1, 77.2, 76.5, 75.4],
       [71.6,73.5,73.4,72.8,71.7]]
NMI = [[25.4, 26, 27, 26.6, 26.3],
       [18.4,19.5,22.3,21.7,20.0]]
ARI = [[32.2, 33.1, 35.4, 36.1, 35.8],
       [21.5,21.9,24.6,23.8,22.9]]
F1 = [[68.5, 69.7, 70.2, 69.3, 68.4],
      [60.6,62.7,63.5,61.4,61.1]]

x = np.arange(len(labels))  # 标签位置
width = 0.16  # 柱状图宽度
colors = ['#4A90E2', '#5A9FD8', '#6BB0C5', '#7BC1B3']

fig, axs = plt.subplots(1, 2, figsize=(8, 2.5), sharey=True)

# ================= 左图 =================
# 绘制分组柱状图
axs[0].bar(x - 1.7*width, NMI[0], width, color=colors[1], alpha=0.8, label='NMI')
axs[0].bar(x - 0.55*width, ARI[0], width, color=colors[2], alpha=0.8, label='ARI')
axs[0].bar(x + 0.55*width, ACC[0], width, color=colors[0], alpha=0.8, label='ACC')
axs[0].bar(x + 1.7*width, F1[0], width, color=colors[3], alpha=0.8, label='F1')

# 设置标签和样式
axs[0].set_xticks(x)
axs[0].set_xticklabels(labels, fontsize=18)
axs[0].set_ylabel('SM', fontsize=22)
axs[0].set_ylim(0, 80)  # 调整Y轴范围
axs[0].grid(True, axis='y', linestyle='--', alpha=0.4)
# axs[0].legend(fontsize=14, loc='upper left')

# ================= 右图 =================
# 绘制相同的分组柱状图
axs[1].bar(x - 1.7*width, NMI[1], width, color=colors[1], alpha=0.8, label='NMI')
axs[1].bar(x - 0.55*width, ARI[1], width, color=colors[2], alpha=0.8, label='ARI')
axs[1].bar(x + 0.55*width, ACC[1], width, color=colors[0], alpha=0.8, label='ACC')
axs[1].bar(x + 1.7*width, F1[1], width, color=colors[3], alpha=0.8, label='F1')

# 设置标签和样式
axs[1].set_xticks(x)
axs[1].set_xticklabels(labels, fontsize=18)
axs[1].set_ylabel('SM-BIO', fontsize=22)
axs[1].set_ylim(0, 80)
axs[1].grid(True, axis='y', linestyle='--', alpha=0.4)
# axs[1].legend(fontsize=14, loc='upper left', ncol=4)

# ================= 全局样式调整 =================
for ax in axs:
    ax.tick_params(axis='both', labelsize=16)
    # 移除顶部和右侧边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # 加粗底部和左侧边框
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)


handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, 
           loc='upper center', 
           ncol=4, 
           fontsize=16,
           frameon=False,
           bbox_to_anchor=(0.5, 1.07))
plt.tight_layout()
plt.subplots_adjust(wspace=0.1)  # 调整子图间距
plt.show()
# plt.savefig("./output/hyper_gamma.png", dpi=600, bbox_inches='tight')z