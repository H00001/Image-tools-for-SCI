
import matplotlib.pyplot as plt

import numpy as np
# plt.figure(figsize=(20, 16))
labels = ['Base', '-L', '-C', 'Ours']
labels1 = ['COX2', 'BZR', "IMDB-BINARY", 'COLLAB' , 'Letter-low', "Synthie"]
colors = ['#a6c8ff', '#ffb84d', '#b3e6b3', '#ff9999', '#d1b3e0', '#c2b0a7']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 40
plt.rcParams['axes.unicode_minus'] = False


def tp(matrix):
    return np.array(matrix).T

name = "ACC"

data_ACC = [
[30.99 ,40.37, 30.01, 18.2, 14.74,23.9],
[71.78 ,75.75, 64.24, 58.5, 31.19,48.9],
[73.24 ,76.67, 63.66, 59.6, 35.36,50.4],
[81.20 ,82.4, 69.2, 63.3 ,40.8,  54.4],
]

data_NMI = [[0.37, 2.22,1.7, 10.78, 3.21,23.3],
    [2.75, 6.95, 8.4, 17.7, 37.46,51.4],
    [2.41, 5.52, 6.6,20.9, 39.58,50.1],
    [3.82, 10.7, 11.1,23.7, 42.5,58.8]]

data_ARI = [
[0.76,1.22, 5.18, 5.27, 9.35,14.27],
[4.88,17.5 ,11.48,10.65,16.23,18.65],
[5.14,18.4 ,12.89,12.37,18.05,16.37],
[8.4,22.2 ,13.4,  14.1, 22.6,22.21],
]

data_F1 = [
[44.00 ,32.37 ,34.41,27.1, 14.74,30.3],
[72.78 ,73.75, 53.24,42.5, 29.99,51.5],
[70.24 ,71.82 ,52.78,53.4, 30.08,42.6],
[77.00 ,76.8 ,56.66,55.6, 39.6,52.3],
]


data_use = tp(eval(f"data_{name}"))

x = np.arange(len(labels))
width = 0.15
fig, ax = plt.subplots(figsize=(16, 10))  # Adjust the width and height as needed


hatch_color = '0.4'

rects1 = ax.bar(x - 2.5*width, np.array(data_use[0]), width, label=labels1[0], color=colors[0],edgecolor =hatch_color, hatch='\\')
rects2 = ax.bar(x - 1.5*width, np.array(data_use[1]), width, label=labels1[1], color=colors[1],edgecolor =hatch_color, hatch='//')
rects3 = ax.bar(x - 0.5*width, np.array(data_use[2]), width, label=labels1[2], color=colors[2],edgecolor =hatch_color, hatch='-')
rects4 = ax.bar(x + 0.5*width, np.array(data_use[3]), width, label=labels1[3], color=colors[3],edgecolor =hatch_color, hatch='+')
rects5 = ax.bar(x + 1.5*width, np.array(data_use[4]), width, label=labels1[4], color=colors[4],edgecolor =hatch_color, hatch='*')
rects6 = ax.bar(x + 2.5*width, np.array(data_use[5]), width, label=labels1[5], color=colors[5],edgecolor =hatch_color, hatch='O')

rects = [rects1, rects2, rects3, rects4,rects5, rects6]
for i, rect in enumerate(rects):
    for j, bar in enumerate(rect):
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',  # 显示的文本
            xy=(bar.get_x() + bar.get_width() / 2, height),  # 标注的位置
            xytext=(0, 1),  # 文本偏移量
            textcoords="offset points",  # 使用点作为偏移单位
            ha='center', va='bottom',  # 对齐方式
            color='#111111',  # 文本颜色
            fontsize=19)  # 设置字体大小
        ax.plot([bar.get_x() + bar.get_width() / 2, bar.get_x() + bar.get_width() / 2],  # x坐标
                [height, height + 0.5],  # y坐标
                color='#111111',  # 线条颜色
                linewidth=0.5)  # 线条宽度
# ax.set_xlabel(f'{name}')9
ax.set_ylabel('Score (%)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.3)  # You can adjust alpha for transparency

# Optionally, set the background color of the plot area
ax.set_facecolor('whitesmoke')  # Lighter background color for the plot area
ax.legend(fontsize=25, frameon=False)  # Set the font size to 12 points
fig.tight_layout()
name = name.lower()
plt.savefig(f'./ICASSP/abl_exp/abl_{name}.png',dpi=600)
# plt.savefig(f'abl_exp/{name}.eps')

# plt.show()
