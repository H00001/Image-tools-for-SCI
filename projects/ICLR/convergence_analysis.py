import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import matplotlib.ticker as ticker
from scipy.interpolate import interp1d


# 总共 10 个 epoch
sum_of_x_points = 20

x = np.linspace(1, 20, 20)
marker_spacing = 3

data_dict = {
    'FedGCN': {
      'acc': [58.1, 60.2, 62.3, 64.3, 52.2, 55.7, 62.0, 57.6, 58.3, 62.2,
              65.4, 68.1, 75.8, 74.2, 73.1, 68.5, 70.4, 68.1, 64.4, 63.4], 
      'nmi': [5.1,  7.2,  12.5, 15.1, 25.4, 18.7, 16.2, 18.9, 19.2, 22.4,
              22.2, 23.3, 16.1, 16.8, 15.5, 20.3, 16.8, 17.9, 19.1, 21.5], 
      'ari': [7.9, 7.32, 15.6, 22.12, 25.4, 29.2, 30.3, 28.6, 23.4, 18.5,
              25.5, 24.1, 27.7, 19.6, 26.3, 25.4, 23.8, 31.28, 25.4, 18.9],
        'color': "#018F3C", 'marker': 'X',
        'acc_std': (1.5, 2.8), 'nmi_std': (1.3, 2.3), 'ari_std': (1.7, 2.5)
    },
     'Local': {
        'acc': [54.86, 58.37, 61.32, 62.75, 63.39, 65.74, 66.72, 67.69, 66.77, 64.92],
        'nmi': [6.8681, 7.0782, 7.8895, 7.9443, 8.1591, 10.6182, 9.1492, 8.8503, 9.0769, 9.8637],
        'ari': [5.12, 7.18, 10.31, 12.26, 16.40, 18.20, 20.34, 22.31,20.28, 21.11],
        'color': "#059BE6", 'marker': '^',
        'acc_std': (0.7, 2.0), 'nmi_std': (1.5, 1.2), 'ari_std': (1.3, 1.1)
    },
     'Ours': {
        'acc': [58.17, 64.20, 68.37, 70.24, 72.43, 76.11, 80.82, 78.11, 79.42, 79.44
                
                ],
        'nmi': [5.12, 8.32, 12.56, 15.12, 25.40, 24.20, 23.34, 26.31, 27.28, 26.11],
        'ari': [7.9, 8.32, 14.56, 23.12, 27.40, 31.20, 34.34, 35.31, 35.28, 36.42],
        'color': "#FA0606", 'marker': 'P',
        'acc_std': (0.5, 1.2), 'nmi_std': (1.1, 1.8), 'ari_std': (1.1, 0.9)
    },
    'Fed-PKA': {
       'acc': [66.17, 67.20, 68.37, 70.24, 63.43, 64.11, 68.82, 75.11, 72.42, 74.44],
        'nmi': [9.12, 11.32, 12.56, 14.12, 16.40, 22.20, 22.34, 23.31, 24.28, 21.11],
        'ari': [17.9, 18.32, 19.56, 22.12, 25.40, 27.20, 24.34, 20.31, 22.28, 24.42],
        'color': "#FF8C00", 'marker': '*',
        'acc_std': (2.0, 2.5), 'nmi_std': (1.4, 3.0), 'ari_std': (1.6, 2.5)
    },
}
def linear_interpolate(data, num_points):
    interpolated_data = []
    for i in range(len(data) - 1):
        interpolated_data.append(data[i])
        # 计算相邻两点的平均值
        avg_point = (data[i] + data[i + 1]) / 2
        interpolated_data.append(avg_point)
    interpolated_data.append(data[-1])  # 保留最后一个点
    return interpolated_data[:num_points]  # 返回前20个点

# Interpolate the data for each method to 20 points
for method in data_dict:
    for metric in ['acc', 'nmi', 'ari']:
        if method != 'FedGCN':
            data_dict[method][metric] = linear_interpolate(data_dict[method][metric], 20)
def compute_bounds(values, std_min, std_max):
    # 如果 values 长度是19，增加一个点使得长度为20
    if len(values) == 19:
        values = values + [values[-1]]  # 把最后一个值重复一次，确保长度为20

    # 生成随 epoch 变化的标准差
    std_range = np.linspace(std_min, std_max, len(values))  # 确保 std_range 的长度和 values 一致
    
    # 平滑曲线
    values_smooth = gaussian_filter1d(values, sigma=1)
    
    # 使用线性插值确保返回20个点
    if len(values_smooth) < 20:
        x = np.linspace(0, len(values_smooth) - 1, len(values_smooth))  # 原数据的 x 轴
        x_new = np.linspace(0, len(values_smooth) - 1, 20)  # 新的 x 轴，确保插值为20个点
        values_smooth = np.interp(x_new, x, values_smooth)  # 线性插值

    return values_smooth - std_range, values_smooth + std_range, values_smooth

# 创建 1x3 子图
fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

titles = ['ACC (%)', 'NMI (%)', 'ARI (%)']
ylims = [(55, 90), (0, 40), (0, 40)]









for i, (ax, metric) in enumerate(zip(axes, ['acc', 'nmi', 'ari'])):
    for name, d in data_dict.items():
        lower, upper, smoothed = compute_bounds(d[metric], *d[f'{metric}_std'])
        ax.plot(
            x, smoothed,
            color=d['color'], linewidth=3,
            marker=d['marker'], markevery=marker_spacing,
            markersize=15, label=name
        )
        ax.fill_between(x, lower, upper, color=d['color'], alpha=0.2)

    # 隐藏边框
    for spine in ax.spines.values():
        spine.set_visible(False)

    # 坐标范围
    ax.set_xlim(1, sum_of_x_points)
    ax.set_ylim(*ylims[i])

    # 刻度
    ax.set_xticks(x-1)
    ax.tick_params(axis='both', labelsize=26)

    # 网格与背景
    ax.grid(color='white', linestyle='--', linewidth=1.5)
    ax.set_facecolor("#dce7f1")

    # 设置坐标轴标签
    ax.set_xlabel("Epoch", fontsize=24)
    ax.text(
    0.04, 0.95, titles[i],  # x=0.02（靠左），y=0.95（靠顶）
    transform=ax.transAxes,  # 使用轴坐标系（0-1范围）
    fontsize=26,
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
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))


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
plt.savefig("./projects/ICLR/output/coverage_study.png", dpi=600)
plt.show()
