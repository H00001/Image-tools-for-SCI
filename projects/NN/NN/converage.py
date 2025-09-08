import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from matplotlib.lines import Line2D
import matplotlib.ticker as ticker


# ==== 基本参数 ====
x = np.linspace(0, 20, 20)
marker_spacing = 5
sum_of_x_points = 20

# ==== 模型结果 ====
data_dict = {
    'FedGCN': {
        'acc': [58.17, 50.49, 60.20, 54.01, 64.37, 63.44, 52.24, 58.12, 63.43, 61.72,
                64.11, 62.69, 68.82, 63.77, 75.11, 69.23, 72.42, 68.37, 74.44, 73.37],
        'nmi': [5.12, 6.89, 7.32, 9.77, 12.56, 14.94, 15.12, 17.30, 25.40, 23.45,
                22.20, 24.22, 23.34, 18.35, 16.31, 17.30, 16.28, 14.12, 19.11, 15.99],
        'ari': [7.9, 6.89, 7.32, 9.77, 15.56, 16.94, 22.12, 23.30, 25.40, 28.45,
                29.20, 28.22, 30.34, 31.35, 26.31, 30.30, 31.28, 27.71, 27.42, 25.55],
        'loss':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'color': '#1f77b4', 'marker': 'X', 'acc_std': (1.5, 4.8), 'nmi_std': (1.3, 2.3),'ari_std': (1.7,2.5), 'loss_std': (0,0)
    },
    'Local': {
        'acc': [56.86, 57.42, 60.37, 64.11, 65.32, 64.71, 64.75, 64.28, 65.39, 64.37,
                65.74, 66.43, 67.72, 68.11, 69.69, 67.82, 62.77, 63.89, 62.92, 61.88],
        'nmi': [5.8681, 5.9100, 5.0782, 5.0967, 7.8895, 6.9755, 7.9443, 4.9777, 8.1591, 11.7345,
                10.6182, 12.1383, 9.1492, 7.6171, 7.8503, 6.6187, 8.0769, 9.5718, 9.8637, 9.1600],
        'ari': [5.12, 6.77, 7.18, 8.77, 10.31, 14.88, 15.26, 17.30, 25.40, 23.45,
                22.20, 24.22, 23.34, 18.35, 16.31, 17.30, 16.28, 14.12, 19.11, 15.99],
        'loss':[62.0,54.1,44,62.5,55.8,34.7,29.2,57.5,63.2,62.6,50,44,37,35,45,52,61,30,45,49],

        'color': '#2ca02c', 'marker': 'o', 'acc_std': (0.7, 2.0), 'nmi_std': (0.5, 0.2),'ari_std': (0.7, 0.5),'loss_std': (8,12)
    },
    'OURS': {
        'acc': [56.12, 58.90, 60.00, 62.11, 63.49, 65.11, 68.18, 70.60, 72.12, 74.17,
                76.55, 77.72, 78.68, 78.39, 78.35, 79.08, 79.71, 79.84, 79.99, 78.92],
        'nmi': [5.5632, 7.8386, 11.5321, 15.9579, 19.7485, 22.5559, 23.7957, 24.8173, 24.7470, 24.3428,
                24.0917, 24.7619, 25.5777, 25.8522, 27.1608, 27.9478, 27.2127, 29.1789, 28.9053, 28.8988],
        'ari': [7.12, 9.89, 9.32, 10.77, 13.56, 17.94, 19.12, 22.30, 23.40,
                22.20, 26.22, 28.22, 30.34, 33.35, 34.31, 34.30, 35.28, 35.71, 35.42, 35.55],
        'loss':[80.7,74.2,91.5,66.4,72.8,34.3, 51.2,69.7,40.9,30.8,28.5,43.1,18.9,22.5,17.3,8.6,13.5,5.7,12.7,10],

        'color': '#d62728', 'marker': 'P', 'acc_std': (0.5, 1.2), 'nmi_std': (1.1, 1.8), 'ari_std': (1.1, 2.3),'loss_std': (6,8)
    }
}

# ==== 计算上下界 ====
def compute_bounds(values, std_min, std_max):
    std_range = np.linspace(std_min, std_max, len(values))
    values = gaussian_filter1d(values, 1)
    return values - std_range, values + std_range, values

# ==== 绘图 ====
fig, axes = plt.subplots(1, 4, figsize=(20, 5))
titles = ['ACC (%)', 'NMI (%)', 'ARI (%)', 'Loss']
ylims = [(50, 86), (5, 31),(5, 41),(0,100)]

i = 0
for ax, metric in zip(axes, ['acc', 'nmi', 'ari', 'loss']):
    if metric == 'loss':
        for name, d in data_dict.items():
            if name == "OURS"  or name== "Local":
                lower, upper, smoothed = compute_bounds(d[metric], *d[f'{metric}_std'])
                ax.plot(x, smoothed, color=d['color'], lw=3, marker=d['marker'], markevery=marker_spacing,
                markersize=10, label=name)
                ax.fill_between(x, lower, upper, color=d['color'], alpha=0.2)

    else:
        for name, d in data_dict.items():
            lower, upper, smoothed = compute_bounds(d[metric], *d[f'{metric}_std'])
            ax.plot(x, smoothed, color=d['color'], lw=3, marker=d['marker'], markevery=marker_spacing,
            markersize=10, label=name)
            ax.fill_between(x, lower, upper, color=d['color'], alpha=0.2)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlim(0, sum_of_x_points)
    ax.set_ylim(*ylims[i])
#     ax.set_xlabel('Epoch', fontsize=26)
    ax.set_xlabel(titles[i], fontsize=38)
    ax.tick_params(axis='both', labelsize=36)
    ax.grid(color='white', linestyle='--', linewidth=1)
    ax.set_facecolor("#e9e9e9")
    
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))  # 每5个单位一个刻度
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))  # 每5个单位一个刻度

    if metric == 'loss':
        ax.yaxis.set_major_locator(ticker.MultipleLocator(25)) 

#     ax.legend(fontsize=20, loc='upper left')
    i+=1



plt.subplots_adjust(top=0.75)  # 适当调大

handles, labels = axes[0].get_legend_handles_labels()

fig.legend(handles=handles,
           labels=labels,
           loc='upper center',
           fontsize=34,
           ncol=len(data_dict),
           bbox_to_anchor=(0.5, 1.0459),
           frameon=False
           
           )
plt.tight_layout(rect=[0, 0.0225, 1, 0.90])  # 留出上方空间

plt.subplots_adjust(wspace=0.3)

plt.savefig('./output/converage.png', dpi=600, transparent=False)

plt.show()
# plt.savefig("output/cover.png")
