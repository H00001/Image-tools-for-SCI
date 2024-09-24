
import matplotlib.pyplot as plt

import numpy as np
# plt.figure(figsize=(20, 16))
labels = ['Base', '-L', '-C', 'Ours']
labels1 = ['COX2', 'BZR', 'COLLAB' , 'Letter-low']
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
def tp(matrix):
    return np.array(matrix).T

name = "ARI"

data_ACC = [
[50.99 ,40.37, 40.01, 14.74],
[71.78 ,75.75, 54.24, 31.19],
[73.24 ,76.67, 53.88, 30.36],
[78.90 ,79.93, 58.36, 34.25],
]

data_NMI = [[0.37, 2.22, 5.78, 3.21],
    [2.75, 5.95, 19.69, 29.46],
    [2.41, 6.52, 18.14, 28.58],
    [3.82, 9.39, 22.42, 32.81]]

data_ARI = [
[0.76,1.11 ,5.18,10.35],
[4.88,5.45 ,11.48,21.23],
[5.14,5.87 ,12.89,22.05],
[7.74,6.45 ,13.37,24.18],
]

data_F1 = [
[44.00 ,32.37, 34.41, 14.74],
[70.78 ,73.75, 53.24, 29.99],
[72.24 ,72.82, 52.78, 30.08],
[76.99 ,77.67, 56.66, 32.35],
]


data_use = tp(eval(f"data_{name}"))

x = np.arange(len(labels))
width = 0.22
fig, ax = plt.subplots()

hatch_color = '0.4'

rects1 = ax.bar(x - 1.5*width, np.array(data_use[0]), width, label=labels1[0], color=colors[0],edgecolor =hatch_color, hatch='\\')
rects2 = ax.bar(x - 0.5*width, np.array(data_use[1]), width, label=labels1[1], color=colors[1],edgecolor =hatch_color, hatch='//')
rects3 = ax.bar(x + 0.5*width, np.array(data_use[2]), width, label=labels1[2], color=colors[2],edgecolor =hatch_color, hatch='-')
rects4 = ax.bar(x + 1.5*width, np.array(data_use[3]), width, label=labels1[3], color=colors[3],edgecolor =hatch_color, hatch='+')

rects = [rects1, rects2, rects3, rects4]
for i, rect in enumerate(rects):
    for j, bar in enumerate(rect):
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',  # 显示的文本
                    xy=(bar.get_x() + bar.get_width() / 2, height),  # 标注的位置
                    xytext=(0, 1),  # 文本偏移量
                    textcoords="offset points",  # 使用点作为偏移单位
                    ha='center', va='bottom',  # 对齐方式
                    color='#111111')  # 文本颜色
        ax.plot([bar.get_x() + bar.get_width() / 2, bar.get_x() + bar.get_width() / 2],  # x坐标
                [height, height + 0.5],  # y坐标
                color='#111111',  # 线条颜色
                linewidth=0.5)  # 线条宽度
ax.set_xlabel(f'{name}')
ax.set_ylabel('Score')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
fig.tight_layout()
plt.savefig(f'abl_exp/{name}.png',dpi=1200)
plt.savefig(f'abl_exp/{name}.eps')

plt.show()
