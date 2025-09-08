import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.font_manager import FontProperties

# matplotlib.use('Agg')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 解决中文乱码

labels = ['ITR', 'AMGC', 'AIAE', 'ASD-VAE', 'OURS']
la1 = ['PROTEINS', 'ENZYMES', 'DHFR','BZR', 'COX2']
a = [58.4, 54.4, 61.2, 58.0, 52.9]
b = [32.3, 30.5, 54.6, 61.9, 49.2]
c = [58.6, 54.8, 55.6, 30.6, 38.4]
d = [53.0, 52.1, 54.7, 69.0,53.5]
e = [72.3, 60.4, 64.0, 71.0, 64.2]
transposed = list(zip(a, b, c, d, e))

# Print the transposed result
a = list(a)
b = list(b)
c = list(c)
d = list(d)
e = list(e)

# marks = ["o", "X", "+", "*", "O"]

x = np.arange(len(labels))  # 标签位置

num_bars = 5
width = 0.12  # 每个 bar 的宽度
x = np.arange(len(a))  # 每组数据的位置
# gap_width = 0  # 间隙宽度
offsets = np.linspace(-width * 2, width *2.1, num_bars)


# fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(12, 5))
# ax.set_ylim(0, 91)
# yy = [65, 68, 70, 72, 75, 78, 80]
# plt.yticks(yy)

offsets = np.linspace(-width * 2, width * 2.6, num_bars)  # Keep this line as it is

# Adjust the x positions of the bars to introduce gaps between groups
group_gap = 0.25  # You can adjust this value to control the gap between groups
x = np.arange(len(a))  # Initial positions of the bars
rects1 = ax.bar(x + offsets[0], a, width, label=labels[0], color='#000001', edgecolor="#000001", linewidth=1.2, zorder=3)
rects2 = ax.bar(x + offsets[1], b, width, label=labels[1], color='#541b7a', edgecolor="#541b7a", linewidth=1.2, zorder=3)
rects3 = ax.bar(x + offsets[2], c, width, label=labels[2], color='#a63a7a', edgecolor="#a63a7a", linewidth=1.2, zorder=3)
rects4 = ax.bar(x + offsets[3], d, width, label=labels[3], color='#e6684a', edgecolor="#e6684a", linewidth=1.2, zorder=3)
rects5 = ax.bar(x + offsets[4], e, width, label=labels[4], color='#feb202', edgecolor="#feb202", linewidth=1.2, zorder=3)

# Add numbers on top of each bar
for rect in rects1 + rects2 + rects3 + rects4 + rects5:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 1, f'{height:.1f}', ha='center', va='bottom', fontsize=17, rotation=90, fontweight='bold')




# 为y轴、标题和x轴等添加一些文本。
# ax.set_xlabel('Clustering metrics', fontsize=14)
# ax.set_ylabel('Performance (%)', fontsize=14)
ax.set_facecolor('#ffffff')  # 设置背景颜色为浅灰色

# ax.set_xlabel('Node-level Imputation Method + Detector', fontsize=30)
plt.ylabel('AUC(%)', fontsize=28 , weight='bold')
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='white', zorder=0)

ax.set_xticks(x + 0.05)
ax.set_xticklabels(la1 , fontsize=24, fontweight='bold')
# ax.tick_params(axis='both',which='both', labelsize=18)

# 设置刻度字体加粗
ax.tick_params(axis='both', which='both', labelsize=28, length=0)  # 隐藏刻度线
for tick in ax.get_xticklabels() + ax.get_yticklabels():
    tick.set_fontweight('bold')

ax.legend(
    loc='upper center',
    ncol=5,
    columnspacing=1.0,
    prop={'weight': 'bold', 'size': 20},
    frameon=False,
    bbox_to_anchor=(0.5, 1.19)  # 0.5 是横向居中，1.05 是往上移动（默认是 1.0）
)
# 设置网格线的刻度
ax.set_xticks(np.arange(-0.5, len(labels), 1), minor=True)
ax.set_yticks(np.arange(0, 93, 20), minor=False)

# 去掉边框线
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# plt.show()
plt.tight_layout()
plt.savefig("./projects/GLAD/output/compare_4.png", dpi=600)
plt.show()