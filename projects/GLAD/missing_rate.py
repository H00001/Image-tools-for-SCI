import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from matplotlib.lines import Line2D
import matplotlib.ticker as ticker

# 定义不同的标记
markers = ['o', 's', 'D', '^', '*', 'P', 'X', 'p']

# 基本参数
x = np.linspace(50, 80, 10)
marker_spacing = 2
sum_of_x_points = 80
names = ['ENZYMES', 'AIDS', 'DHFR', 'BZR', 'COX2', 'DD', 'MMP', 'IMDB']
morandi_colors = [
    "#A7C4BC", "#8BBABB", "#6B7B8E", "#D3D0C8", 
    "#E2DCD0", "#B7B7B7", "#8F8F8F", "#5F5F5F"
]

# 模型结果
ours_dict = {
    'PROTEINS': [71.17, 69.49, 68.20, 64.01, 63.37, 63.44, 61.24, 58.12, 58.43, 52.72],
    'DHFR': [66.86, 64.42, 60.37, 59.11, 59.32, 57.71, 54.75, 53.28, 53.39, 52.37],
    'BZR': [72.86, 71.42, 70.37, 70.11, 63.32, 62.71, 66.75, 61.28, 59.39, 60.37],
    'COX2': [65.1, 64.4, 63.2, 62.7, 65.7, 66.3, 66.6, 64.3, 62.1, 60.8],
    'ENZYMES': [60.4, 57.77, 55.18, 56.77, 54.31, 53.88, 51.26, 50.30, 50.40, 50.45],
    'IMDB': [63.12, 62.77, 62.18, 62.77, 61.91, 56.88, 55.26, 57.30, 60.40, 55.45]
}

others_dict = {
    'PROTEINS': [54.17, 50.18, 68.20, 64.01, 63.37, 63.44, 61.24, 58.12, 58.43, 52.72],
    'DHFR': [52.86, 54.42, 50.37, 46.11, 44.32, 42.71, 39.75, 40.28, 40.39, 40.37],
    'BZR': [61.86, 58.42, 55.37, 54.11, 54.32, 53.71, 53.75, 45.28, 40.39, 32.37],
    'COX2': [61.1, 63.4, 62.2, 60.7, 61.7, 55.3, 56.6, 55.3, 43.1, 42.8],
    'ENZYMES': [56.4, 54.77, 52.18, 50.77, 53.31, 45.88, 44.26, 32.30, 30.40, 30.45],
    'IMDB': [54.12, 54.77, 52.18, 51.77, 50.91, 44.88, 44.26, 42.30, 42.40, 41.45]
}

std0 = [[2, 5], [1, 2], [2, 3]]
std1 = [[3, 2], [3, 4], [2, 1]]

std0 = [[3, 5], [3.5, 3], [2.6, 3]]
std1 = [[1, 2], [2.5, 4], [1, 2]]

# 计算上下界
def compute_bounds(values, std_min, std_max):
    std_range = np.linspace(std_min, std_max, len(values))
    values = gaussian_filter1d(values, 1)
    return values - std_range, values + std_range, values

# 绘图
fig, axes = plt.subplots(1, 2, figsize=(15, 6))



for i, db in enumerate(['ENZYMES', 'IMDB', 'DHFR']):
    lower, upper, smoothed = compute_bounds(ours_dict[db], std0[i][0], std0[i][1])
    axes[0].plot(x, smoothed, color=morandi_colors[i], lw=3, marker=markers[i], markevery=marker_spacing,
                 markersize=10, label=f'O({db})')
    axes[0].fill_between(x, lower, upper, color=morandi_colors[i], alpha=0.2)

    lower, upper, smoothed = compute_bounds(others_dict[db], std0[i][0], std0[i][1])
    axes[0].plot(x, smoothed, color=morandi_colors[i+3], lw=3, marker=markers[i+3], markevery=marker_spacing,
                 markersize=10, label=f'S({db})', linestyle='--')
    axes[0].fill_between(x, lower, upper, color=morandi_colors[i+3], alpha=0.2)

    axes[0].set_xlim(49, sum_of_x_points+1)
    # axes[0].set_xticks(np.arange(50, sum_of_x_points))
    axes[0].set_ylim(30, 80)
    axes[0].set_ylabel('AUC (%)', fontsize=28)
    axes[0].tick_params(axis='both', labelsize=28)
    axes[0].grid(color='#d2d2d2', linestyle='--', linewidth=1)
    axes[0].set_facecolor("#ffffff")
    axes[0].yaxis.set_major_locator(ticker.MultipleLocator(10))

for i, db in enumerate(['COX2', 'IMDB', 'BZR']):
    lower, upper, smoothed = compute_bounds(ours_dict[db], std1[i][0], std1[i][1])
    axes[1].plot(x, smoothed, color=morandi_colors[i], lw=3, marker=markers[4+i], markevery=marker_spacing,
                 markersize=10, label=f'O({db})')
    axes[1].fill_between(x, lower, upper, color=morandi_colors[i], alpha=0.2)

    lower, upper, smoothed = compute_bounds(others_dict[db], std1[i][0], std1[i][1])
    axes[1].plot(x, smoothed, color=morandi_colors[i+3], lw=3, marker=markers[i+3], markevery=marker_spacing,
                 markersize=10, label=f'S({db})', linestyle='--')
    axes[1].fill_between(x, lower, upper, color=morandi_colors[i+3], alpha=0.2)

    axes[1].set_xlim(49, sum_of_x_points+1)
    # axes[1].set_xticks(np.arange(50, sum_of_x_points))
    axes[1].set_ylim(30, 90)
    axes[1].tick_params(axis='both', labelsize=28)
    axes[1].grid(color='#d1d1d1', linestyle='--', linewidth=1)
    axes[1].set_facecolor("#ffffff")
    axes[1].yaxis.set_major_locator(ticker.MultipleLocator(10))

plt.subplots_adjust(top=0.75)

handles, labels = axes[0].get_legend_handles_labels()
axes[0].legend(loc='upper center', fontsize=17, ncol=3, handletextpad=0.2)
axes[1].legend(loc='upper center', fontsize=17, ncol=3, handletextpad=0.2)

axes[0].set_xlabel("Missing Rate (%)", fontsize=25)
axes[1].set_xlabel("Missing Rate (%)", fontsize=25)

axes[0].xaxis.set_tick_params(pad=10)
axes[1].xaxis.set_tick_params(pad=10)


axes[0].xaxis.set_major_locator(ticker.MultipleLocator(5))

axes[1].xaxis.set_major_locator(ticker.MultipleLocator(5))

plt.subplots_adjust(left=0, bottom=0.1, right=0.9, top=1, wspace=-0.0, hspace=0)

plt.tight_layout(rect=[0, 0.0225, 1, 0.90])

plt.savefig("./projects/GLAD/output/missing_rate.png")
plt.show()
