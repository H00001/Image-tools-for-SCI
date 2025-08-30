import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

# 设置全局字体为微软雅黑并加粗
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['font.weight'] = 'bold'

# 五个数据集的标签
labels = ['ACC', 'NMI', 'ARI', 'F1']
num_vars = len(labels)

# 五个模型在五个数据集上的 Accuracy 数据
model_A = [0.31, 0.26 , 0.14, 0.30]
model_B = [0.30, 0.27 , 0.15, 0.29]
model_C = [0.38, 0.35 , 0.18, 0.36]
model_D = [0.36, 0.37 , 0.19, 0.34]
model_E = [0.32, 0.33 , 0.20, 0.31]
model_F = [0.41, 0.43 , 0.23, 0.40]

# data = [model_A, model_B, model_C, model_E]
data = [model_A, model_B, model_C, model_D, model_E, model_F]
model_names = ['Average Pooling','Max Pooling','DiffPooling', 'Multi-scale Pooling', 'Top-K Pooling', 'Ours']
# model_names = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']

# 计算角度并闭合雷达图
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]
for i in range(len(data)):
    data[i] += data[i][:1]

# 设置颜色
# colors = ['#ff8682', '#eaf07a', '#a4d4ed', '#d194da']
# colors = ['#8ccdbf', '#cde0a5', '#f9db95', '#ef8476', '#a4d4ed','#c5a8ce']
colors = ['#f57c6e', '#f2b56f', '#fae69e', '#84c3b7', '#88d8db','#f2a7da']

# 创建图像
fig, ax = plt.subplots(figsize=(4.5,6), subplot_kw=dict(polar=True))

# 绘制每个模型的线和填充区域
for i, d in enumerate(data):
    ax.plot(angles, d, color=colors[i], linewidth=3, label=model_names[i], zorder=1)
    ax.fill(angles, d, color=colors[i], alpha=0.2, zorder=1)

# 隐藏角度刻度线
# ax.set_xticks([])
ax.set_xticklabels([])

# 设置每72°画一条角度刻度线
ax.set_thetagrids(angles=np.degrees(angles[:-1]), labels=labels, fontsize=12, fontweight='bold')
# # 手动添加标签，使其远离圆形主体
# for i, angle in enumerate(angles[:-1]):
#     ax.text(angle, 1.1, labels[i], horizontalalignment='right', verticalalignment='center',
#             fontsize=12, fontweight='bold', color='black', zorder=1)

# 设置 y 轴刻度字体和范围
ax.tick_params(axis='y')
for label in ax.get_yticklabels():
    label.set_fontweight('bold')
ax.set_ylim(0, 0.4)
ax.set_rgrids([i / 10 for i in range(0, 10, 3)], fontsize=12)  # 设置只显示偶数刻度

# 添加标题并调整位置
plt.title('Comparison of ACC on different pooling', fontsize=12, fontweight='bold', y=1.12 ,x=0.52)

# 设置图例为上下两个部分
# 第一个图例（右上角）：前两个模型
# legend1 = ax.legend(
#     handles=[ax.lines[i] for i in [0, 1, 2]],
#     labels=model_names[0:2],
#     loc='upper right',
#     bbox_to_anchor=(0.5, 0.0),
#     fontsize=10,
#     frameon=False
# )

# # 第二个图例（右下角）：后两个模型
# legend2 = ax.legend(
#     handles=[ax.lines[i] for i in [3,4,5]],
#     labels=model_names[3:6],
#     loc='upper left',
#     bbox_to_anchor=(0.5, 0.0),
#     fontsize=10,
#     frameon=False
# )
# 构造前两个模型的图例（第一行）
legend1 = plt.legend(
    handles=[ax.lines[i] for i in [0, 1,2]],
    labels=model_names[0:3],
    loc='lower center',
    bbox_to_anchor=(0.5, -0.2),
    ncol=3,
    fontsize=9,
    frameon=False
)

# 构造后四个模型的图例（第二行）
legend2 = plt.legend(
    handles=[ax.lines[i] for i in [3, 4, 5]],
    labels=model_names[3:6],
    loc='lower center',
    bbox_to_anchor=(0.48, -0.28),
    ncol=3,
    fontsize=9,
    frameon=False
)

# 添加两个图例到图中
ax.add_artist(legend1)
ax.add_artist(legend2)


# legend3 = ax.legend(
#     handles=[ax.lines[i] for i in [0]],
#     labels=model_names[0:1],
#     loc='upper right',
#     bbox_to_anchor=(1.4, 1),
#     fontsize=10,
#     frameon=False
# )

# legend4 = ax.legend(
#     handles=[ax.lines[i] for i in [5]],
#     labels=model_names[5:6],
#     loc='upper right',
#     bbox_to_anchor=(0.05, 1),
#     fontsize=10,
#     frameon=False
# )

# 将两个图例添加到图中
# ax.add_artist(legend)
# ax.add_artist(legend2)
# ax.add_artist(legend3)
# ax.add_artist(legend4)

ax.set_rmax(0.5)  # 设置最大半径为 0.3
ax.set_rgrids([0.0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)  # 显示你希望的刻度

# 自动调整布局
plt.tight_layout(pad=1)
plt.savefig("pooling-abl.png", dpi=600)
plt.show()
