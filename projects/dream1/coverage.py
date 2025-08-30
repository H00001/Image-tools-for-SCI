import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import matplotlib.ticker as ticker

# 总共 10 个 epoch
sum_of_x_points = 10
# 横坐标：1, 2, ..., 10
x = np.arange(1, sum_of_x_points + 1)

marker_spacing = 3

data_dict = data_dict = {
    'FedGCN': {
        'acc': [58.17, 60.20, 64.37, 52.24, 63.43,
                64.11, 68.82, 75.11, 72.42, 74.44],
        'nmi': [5.12, 7.32, 12.56, 15.12, 25.40,
                22.20, 23.34, 16.31, 16.28, 19.11],
        'ari': [7.9, 7.32, 15.56, 22.12, 25.40,
                29.20, 30.34, 26.31, 31.28, 27.42],
        'color': "#018F3C", 'marker': 'X',
        'acc_std': (1.5, 2.8), 'nmi_std': (1.3, 2.3), 'ari_std': (1.7, 2.5)
    },
    'Local': {
        'acc': [56.86, 60.37, 65.32, 64.75, 65.39,
                65.74, 67.72, 69.69, 62.77, 62.92],
        'nmi': [5.8681, 5.0782, 7.8895, 7.9443, 8.1591,
                10.6182, 9.1492, 7.8503, 8.0769, 9.8637],
        'ari': [5.12, 7.18, 10.31, 15.26, 25.40,
                22.20, 23.34, 16.31, 16.28, 19.11],
        'color': "#059BE6", 'marker': 'o',
        'acc_std': (0.7, 2.0), 'nmi_std': (1.5, 1.2), 'ari_std': (1.3, 1.1)
    },
    'Ours': {
        'acc': [57.00, 57.43, 58.82, 63.47, 67.73,
                70.66, 75.16, 75.97, 75.76, 76.96],
        'nmi': [10.05, 10.30, 11.53, 13.82, 16.38,
                18.29, 23.01, 25.49, 28.73, 30.48],
        'ari': [11.92, 12.33, 13.88, 16.72, 19.64,
                22.25, 28.46, 33.34, 35.84, 37.15],
        'color': "#FA0606", 'marker': 'P',
        'acc_std': (0.5, 1.2), 'nmi_std': (1.1, 1.8), 'ari_std': (1.1, 0.9)
    }
}

def compute_bounds(values, std_min, std_max):
    # 生成随 epoch 变化的标准差
    std_range = np.linspace(std_min, std_max, len(values))
    # 平滑曲线
    values_smooth = gaussian_filter1d(values, sigma=1)
    return values_smooth - std_range, values_smooth + std_range, values_smooth

# 创建 1x3 子图
fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

titles = ['ACC (%)', 'NMI (%)', 'ARI (%)']
ylims = [(55, 80), (0, 40), (0, 40)]

for i, (ax, metric) in enumerate(zip(axes, ['acc', 'nmi', 'ari'])):
    for name, d in data_dict.items():
        lower, upper, smoothed = compute_bounds(d[metric], *d[f'{metric}_std'])
        ax.plot(
            x, smoothed,
            color=d['color'], linewidth=4,
            marker=d['marker'], markevery=marker_spacing,
            markersize=16, label=name
        )
        ax.fill_between(x, lower, upper, color=d['color'], alpha=0.2)

    # 隐藏边框
    for spine in ax.spines.values():
        spine.set_visible(False)

    # 坐标范围
    ax.set_xlim(1, sum_of_x_points)
    ax.set_ylim(*ylims[i])

    # 刻度
    ax.set_xticks(x)
    ax.tick_params(axis='both', labelsize=30)

    # 网格与背景
    ax.grid(color='white', linestyle='--', linewidth=1.5)
    ax.set_facecolor("#dce7f1")

    # 设置坐标轴标签
    ax.set_xlabel("Epoch", fontsize=28)
    ax.text(
    0.04, 0.95, titles[i],  # x=0.02（靠左），y=0.95（靠顶）
    transform=ax.transAxes,  # 使用轴坐标系（0-1范围）
    fontsize=28,
    fontweight='bold',
    verticalalignment='top',  # 文本顶部对齐
    bbox=dict(  # 添加半透明背景框（可选）
        facecolor='white', 
        alpha=0.7, 
        edgecolor='none',
        boxstyle='round,pad=0.2'
    )
)
    # ax.set_ylabel(titles[i], fontsize=28)

    # 统一 y 轴主刻度改为 5
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

# 整体图例放在上方中央
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(
    handles=handles, labels=labels,
    loc='upper center', fontsize=26,
    ncol=len(data_dict),
    bbox_to_anchor=(0.5, 1.07),
    frameon=False
)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("./projects/dream1/output/coverage_study.png", dpi=1200)
# plt.show()
