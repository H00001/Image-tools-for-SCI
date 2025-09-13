import matplotlib.pyplot as plt
import numpy as np

# 数据定义：每个子图对应不同数据集的Pace_Reward和Proposal_Reward比例
data = [
    # 左上子图
    {
        'x': [60, 70, 80, 90, 100],
        'pace_reward': [0.37, 0.36, 0.35, 0.35, 0.34],
        'proposal_reward': [0.40, 0.39, 0.38, 0.40, 0.39]
    },
    # 右上子图
    {
        'x': [60, 70, 80, 90, 100],
        'pace_reward': [0.42, 0.39, 0.38, 0.38, 0.37],
        'proposal_reward': [0.36, 0.35, 0.35, 0.37, 0.36]
    },
    # 左下子图
    {
        'x': [60, 70, 80, 90, 100],
        'pace_reward': [0.41, 0.40, 0.40, 0.38, 0.37],
        'proposal_reward': [0.38, 0.37, 0.37, 0.40, 0.40]
    },
    # 右下子图
    {
        'x': [60, 70, 80, 90, 100],
        'pace_reward': [0.41, 0.398, 0.398, 0.38, 0.38],
        'proposal_reward': [0.40, 0.386, 0.386, 0.41, 0.41]
    }
]

# 创建4个子图布局
fig, axs = plt.subplots(2, 2, figsize=(12, 7))

# 遍历每个子图并绘制数据
for i, ax in enumerate(axs.flat):
    d = data[i]
    
    # 绘制柱状图
    bar_width = 2.5  # 柱宽调整以匹配原图
    x_positions = np.array(d['x']) - bar_width/2
    
    ax.bar(x_positions, d['pace_reward'], width=bar_width, color='#FF7F50', label='Pace_Reward')
    ax.bar(x_positions + bar_width, d['proposal_reward'], width=bar_width, color='#4682B4', label='Proposal_Reward')
    
    # 设置坐标轴标签、标题和刻度
    ax.set_xlabel('Number of Interactions', fontsize=14)
    ax.set_ylabel('Reward proportion (%)', fontsize=14)
    ax.set_xticks(d['x'])
    ax.set_ylim(0, 0.5)
    ax.tick_params(axis='both', which='major', labelsize=14)

    
    # 显示图例
    ax.legend(loc='upper right', ncol=2)

plt.tight_layout()
plt.show()
