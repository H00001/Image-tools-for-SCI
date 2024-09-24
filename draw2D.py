#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 8))  # 根据需要调整宽度和高度

# 数据
NAME = "REUT"

if NAME == "CITE":
    sta = 0.0
    end = 0.8

if NAME == "ACM":
    sta = .3
    end = 1

if NAME == "HHAR":
    sta = 0.3
    end = 1
if NAME == "REUT":
    sta = 0.1
    end = 1
if NAME == "USPS":
    sta = 0.3
    end = 0.9

if NAME == "DBLP":
    sta = 0.0
    end = 0.9

# plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.family'] = 'Helvetica Neue'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'

categories = ['ACC', 'NMI', 'ARI', 'F1']
group_names = ['BASE', '-S', '-F', 'OURS']

#colors = ['#F5834A', '#FEAB43', '#FBD54A', '#ECEE66']
# colors = ['#4A90E2', '#50E3C2', '#9013FE', '#B8E986']
#colors = ['#4A80E2', '#4A9FE2', '#4ABFE2', '#4AD9E2']
# colors = ['#3B7A57', '#4CAF50', '#81C784', '#A5D6A7']
colors = ['#4A90E2', '#5A9FD8', '#6BB0C5', '#7BC1B3']




values_ACM = np.array(
    [
        [0.7808, 0.4619, 0.4938, 0.7683],
        [0.9020, 0.6954, 0.7414, 0.8727],
        [0.8691, 0.6028, 0.6489, 0.8673],
        [0.9240, 0.7123, 0.7829, 0.9216],
    ]
)

values_CITE = np.array(
    [[0.3835, 0.1309, 0.1176, 0.3626],
     [0.6584, 0.4301, 0.4255, 0.6008],
     [0.6678, 0.3772, 0.4473, 0.6041],
     [0.7123, 0.4400, 0.4661, 0.6145]]
)

values_HHAR = np.array(
    [[0.5710, 0.6121, 0.4501, 0.5326],
     [0.8476, 0.7591, 0.7079, 0.8466],
     [0.7300, 0.7131, 0.6314, 0.7169],
     [0.8883, 0.8258, 0.7779, 0.8876],
     ]
)

values_REUT = np.array(
    [[0.4863, 0.1548, 0.1373, 0.3725],
     [0.7867, 0.5605, 0.5899, 0.6580],
     [0.7496, 0.5327, 0.5755, 0.6349],
     [0.8173, 0.6000, 0.6300, 0.6640]
    ]
)

values_USPS = np.array(
    [[0.6311, 0.5510, 0.4573, 0.5969],
     [0.7944, 0.8207, 0.7535, 0.7819],
     [0.7937, 0.7910, 0.7646, 0.7051],
     [0.8096, 0.8275, 0.7646, 0.7925],
     ]
)

values_DBLP = np.array(
    [[0.6311, 0.3410, 0.3873, 0.5969],
     [0.6744, 0.3407, 0.35, 0.6819],
     [0.6737, 0.3210, 0.3646, 0.6951],
     [0.7610, 0.4370, 0.4691, 0.7592]]
)
# values = np.roll(values, shift=-1, axis=1)
# values[:, [0, 3]] = values[:, [3, 0]]

# 绘制条状图
bar_width = 0.2  # 条带宽度
gap_width = 0.01  # 间隙宽度
for i, group_name in enumerate(group_names):
    positions = np.arange(len(categories)) + (bar_width + gap_width) * i
    plt.bar(positions, eval(f"values_{NAME}")[i], bar_width, label=group_name, color=colors[i])

# 添加标题和标签
plt.grid(color='white', linestyle='-', linewidth=1)  # 添加白色网格线

plt.title("")
plt.xlabel(NAME, fontweight='bold', fontsize='18')
plt.ylabel('Score', fontweight='bold', fontsize='18')
plt.ylim(sta, end)

plt.xticks(np.arange(len(categories)) + bar_width * 1.5, categories)  # 设置x轴刻度位置
legend = plt.legend(ncol=4, fontsize="13", frameon=False, loc='upper center')

plt.savefig(f'abolish/{NAME}_abolish_600.png', dpi=600)
plt.savefig(f'abolish/{NAME}_abolish_1200.png', dpi=1200)

plt.savefig(f'abolish/{NAME}_abolish.eps')

# 显示图形
# plt.show()
