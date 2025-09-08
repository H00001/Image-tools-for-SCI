import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import matplotlib.ticker as ticker

# 总共 10 个 epoch
sum_of_x_points = 10
# 横坐标：1, 2, ..., 10
x = np.arange(1, sum_of_x_points + 1)

marker_spacing = 3

data_dict = {
    'Local': {
        'acc': [48.85, 49.60, 50.30, 51.20, 51.90, 50.70, 50.00, 50.00, 49.30, 49.30],
        'nmi': [0.07, 2.10, 4.80, 7.30, 10.83, 10.83, 8.10, 8.10, 7.00, 7.00],
        'ari': [0.00, 1.10, 2.80, 4.40, 5.60, 5.60, 4.00, 4.00, 3.00, 3.00],
        'color': "#059BE6", 'marker': 'o',
        'acc_std': (1.5, 2.8), 'nmi_std': (1.3, 2.3), 'ari_std': (1.7, 2.5)
    },
    'FedGCN': {
        'acc': [50.49, 51.30, 52.00, 53.00, 54.10, 54.80, 55.50, 54.70, 53.60, 50.20],
        'nmi': [0.47, 2.50, 5.20, 8.40, 11.30, 12.60, 11.70, 11.70, 10.30, 10.30],
        'ari': [0.43, 1.80, 3.90, 6.20, 8.70, 10.50, 12.30, 12.30, 10.80, 10.80],
        'color': "#018F3C", 'marker': 'X',
        'acc_std': (0.7, 2.0), 'nmi_std': (1.5, 1.2), 'ari_std': (1.3, 1.1)
    },
    'Ours': {
        'acc': [48.02, 53.80, 53.80, 54.80, 54.80, 54.80, 60.00, 62.21, 62.21, 62.21],
        'nmi': [0.08, 2.40, 4.90, 8.20, 12.10, 15.60, 18.50, 20.59, 20.59, 20.59],
        'ari': [0.75, 1.90, 3.80, 6.10, 10.30, 14.00, 17.00, 18.73, 18.73, 18.73],
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
ylims = [(45, 65), (0, 25), (0, 25)]

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
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))

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
plt.savefig("./projects/ASPIRE/output/coverage_study.png", dpi=1200)
# plt.show()
