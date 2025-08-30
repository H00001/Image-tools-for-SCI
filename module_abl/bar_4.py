import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.font_manager import FontProperties

# matplotlib.use('Agg')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 解决中文乱码

labels = ['SM', 'SN', 'CV', 'SM-BIO', 'SM-BIO-SY']

a = [58, 32, 8.59, 53, 58]
b = [54, 30, 8.76, 52, 56]
c = [61, 54, 15.6, 54, 52]
d = [75.0, 61.9, 30.6, 69,68]
e = [78, 69.2, 38.4, 73, 73.5]
# marks = ["o", "X", "+", "*", "O"]

x = np.arange(len(labels))  # 标签位置

num_bars = 5
width = 0.15  # 每个 bar 的宽度
x = np.arange(len(a))  # 每组数据的位置
# gap_width = 0  # 间隙宽度
offsets = np.linspace(-width * 2, width *2.1, num_bars)


# fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(12, 5))
# ax.set_ylim(0, 91)
# yy = [65, 68, 70, 72, 75, 78, 80]
# plt.yticks(yy)

rects1 = ax.bar(x + offsets[0], a, width, label='FedSage',
                hatch="///", color='white', edgecolor="#1f77b4", linewidth=1.2, zorder=3)

rects2 = ax.bar(x + offsets[1], b, width, label='FCGL',
                hatch="oo", color='white', edgecolor="#d62728", linewidth=1.2, zorder=3)

rects3 = ax.bar(x + offsets[2], c, width, label='Fedstar',
                hatch="++", color='white', edgecolor="#2ca02c", linewidth=1.2, zorder=3)

rects4 = ax.bar(x + offsets[3], d, width, label='FedGCN',
                hatch="\\\\", color='white', edgecolor="#9467bd", linewidth=1.2, zorder=3)

rects5 = ax.bar(x + offsets[4], e, width, label='OURS',
                hatch="xx", color='white', edgecolor="#ff7f0e", linewidth=1.2, zorder=3)




# 为y轴、标题和x轴等添加一些文本。
# ax.set_xlabel('Clustering metrics', fontsize=14)
# ax.set_ylabel('Performance (%)', fontsize=14)
ax.set_facecolor('#ffffff')  # 设置背景颜色为浅灰色

ax.set_xlabel('Federated Client Dataset Settings', fontsize=30)
plt.ylabel('ACC(%)', fontsize=30 , weight='bold')
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='white', zorder=0)

ax.set_xticks(x)
ax.set_xticklabels(labels , fontsize=32, fontweight='bold')
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
    bbox_to_anchor=(0.5, 1.13)  # 0.5 是横向居中，1.05 是往上移动（默认是 1.0）
)
# 设置网格线的刻度
ax.set_xticks(np.arange(-0.5, len(labels), 1), minor=True)
ax.set_yticks(np.arange(0, 93, 20), minor=False)

# 去掉边框线
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# plt.show()
plt.tight_layout()
plt.savefig("./output/supervisor.jpg", dpi=600)
# plt.show()