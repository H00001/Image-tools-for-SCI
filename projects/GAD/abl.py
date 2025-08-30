#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
# 全局设置
plt.rcParams['font.family'] = 'Microsoft Yahei'
plt.rcParams['font.size'] = 28
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'
# 数据集配置
datasets = {
    "Cora": {"values": np.array([
        [0.5846, 0.4483],
        [0.7472, 0.6407],
        [0.7624, 0.6817],
        [0.8262, 0.7481],
    ]), "sta": 0.2, "end": 0.9 },

     "Amazon": {"values": np.array([
        [0.5551, 0.5217],
        [0.7154, 0.6613],
        [0.7405, 0.7288],
        [0.8135, 0.7882]
    ]), "sta": 0.2, "end": 0.9}
,
    
    "Weibo": {"values": np.array([
        [0.6002, 0.5217],
        [0.7045, 0.6888],
        [0.8254, 0.7513],
        [0.8802, 0.8458]
    ]), "sta": 0.3, "end": 1.0},
    
    "Reddit": {"values": np.array([
        [0.5032, 0.4215],
        [0.5431, 0.4569],
        [0.5791, 0.5166],
        [0.6356, 0.5976],
    ]), "sta": 0.2, "end": 0.7},
    
    "Disney": {"values": np.array([
        [ 0.5473, 0.4725],
        [0.6627, 0.5349],
        [0.6312, 0.5280],
        [0.6800, 0.5640]
    ]), "sta": 0.2, "end": 0.7},
    
    "Books": {"values": np.array([
        [0.5135, 0.4542],
        [0.5611, 0.5130],
        [0.6212, 0.5235],
        [0.6433, 0.5547],
    ]), "sta": 0.2, "end": 0.7}
    
    }
    


# 通用绘图函数
def plot_bars(ax, dataset_name, data_dict):
    ax.spines['right'].set_visible(False)  # 隐藏右侧框线
    ax.spines['top'].set_visible(False)    # 隐藏顶部框线
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))  # 强制1位小数
# Set the locator to place ticks every 0.1 units
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))

# Optional: Set minor ticks for finer grid (e.g., every 0.05)
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

    # 可选：加粗左、下框线
    ax.spines['left'].set_linewidth(2)     # 左侧框线宽度
    ax.spines['bottom'].set_linewidth(2)   # 底部框线宽度
    categories = ['AUC',  'F1']
    group_names = ['Base', '-RGAI', '-IAD', 'OURS',]
    colors = ['#4A90E2', '#5A9FD8', '#6BB0C5', '#7BC1B3']
    bar_width = 0.1
    gap_width = 0.01

    for i, group_name in enumerate(group_names):
        positions = np.arange(len(categories)) * 0.6 + (bar_width + gap_width) * i
        ax.bar(positions, data_dict["values"][i], bar_width, label=group_name, color=colors[i])

    ax.grid(color='white', linestyle='-', linewidth=1)
    ax.set_title("")
    ax.set_xlabel(dataset_name, fontweight='bold', fontsize=28)
    # ax.set_ylabel('Score', fontweight='bold', fontsize=28)
    ax.tick_params(axis='y', labelsize=28)  # 刻度字体大小

    ax.set_ylim(data_dict["sta"], data_dict["end"])
    ax.set_xticks(np.arange(len(categories)) * 0.6 + (4 - 1) / 2 * (bar_width + gap_width))
    ax.set_xticklabels(categories)

    handles, labels = axes[0, 0].get_legend_handles_labels()


    # ax.legend(handles, labels, 
    #        ncol=4, 
    #        fontsize=20, 
    #        frameon=False, 
    #        loc='upper center',
    #        bbox_to_anchor=(0.5, -0.05),  # 调整y值控制图例与图的距离
    #        handletextpad=0.2)

# 创建画布和子图（2行3列）
fig, axes = plt.subplots(2, 3, figsize=(16, 7))  # 调整总画布大小

# 按顺序绘制数据集
plot_bars(axes[0, 0], "Cora", datasets["Cora"])
plot_bars(axes[0, 1], "Amazon", datasets["Amazon"])

plot_bars(axes[0, 2], "Weibo", datasets["Weibo"])
plot_bars(axes[1, 0], "Reddit", datasets["Reddit"])
plot_bars(axes[1, 1], "Disney", datasets["Disney"])
plot_bars(axes[1, 2], "Books", datasets["Books"])

# 添加全局图例（放在底部）
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, 
           ncol=4, 
           fontsize=32, 
           frameon=False, 
           loc='upper center',
           bbox_to_anchor=(0.5, 1.0),  # 调整y值控制图例与图的距离
           handletextpad=0.4)
plt.tight_layout(rect=[-0.02, -0.04, 1., 0.95])  # 顶部预留 10% 空间
plt.subplots_adjust( hspace=0.49)

# plt.tight_layout()  # 自动调整子图间距
plt.savefig("./projects/GAD/output/abl.png",dpi=600)
plt.show()
