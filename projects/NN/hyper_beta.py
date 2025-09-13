import numpy as np
import matplotlib.pyplot as plt

# ==== 数据示例 ====
iterations = np.linspace(0, 1, 11)  # 0,0.1,...,1

data = {
    "SM": {
        "ACC": [72.5, 72.8, 74.7, 75.2, 76.4, 78.2, 77.5, 76.3, 73.2, 71.0, 69.5],
        "NMI": [22.8, 24.3, 25.5, 25.5, 26.8, 27.3, 26.5, 25.4, 24.2, 24.7, 23.5],
        "ARI": [31.8, 32.2, 34.3, 33.2, 35.5, 34.6, 33.5, 33.3, 32.1, 30.0, 30.2]
    },
    "SM-BIO": {
        "ACC": [67.3, 69.8, 71.8, 72.4, 72.9, 73.2, 73.8, 71.7, 70.4, 70.0, 68.8],
        "NMI": [13.5, 14.2, 15.8, 17.5, 17.3, 16.4, 15.5, 13.5, 14.0, 12.6, 11.5],
        "ARI": [20.0, 20.4, 21.6, 22.1, 23.5, 22.8, 21.5, 20.8, 19.3, 18.7, 16.4]
    },
    "SM-BIO-SY": {
        "ACC": [62.0, 63.0, 68.6, 70.9, 71.7, 72.2, 73.7, 72.5, 70.0, 68.0, 67.8],
        "NMI": [15.0, 15.5, 16.0, 17.0, 19.2, 18.8, 16.0, 15.5, 15.9, 14.0, 12.5],
        "ARI": [23.5, 24.6, 25.8, 26.5, 27.3, 26.1, 25.4, 25.6, 24.7, 23.1, 22.8]
    }
}

colors = ['r', 'gold', 'c']
markers = ['o', 's', '^']

# ==== 绘图函数（按指标绘图） ====
def plot_metric(ax, metric_name):
    for i, dataset in enumerate(data.keys()):
        ax.plot(iterations, data[dataset][metric_name], marker=markers[i], color=colors[i], label=dataset)
    ax.set_ylabel(metric_name+"(%)", fontsize=14)
    ax.set_xlabel(r'$\beta$', fontsize=16)
    if metric_name == "ACC":
        ax.set_ylim(40, 80)
    elif metric_name == "ARI":
        ax.set_ylim(0, 40)
    else:
        ax.set_ylim(0, 30)
    ax.legend()
    ax.grid(True)
    ax.tick_params(axis='both', labelsize=12)

# ==== 绘图 ====
metrics = ["ACC", "ARI", "NMI"]
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for i, metric in enumerate(metrics):
    plot_metric(axes[i], metric)

plt.subplots_adjust(wspace=0.3, left=0.2, right=1, bottom=0.1)

# plt.savefig('./output/hyper_beta.png', dpi=600, transparent=False)

plt.tight_layout()
plt.show()
# 显示图片，然后保存为pdf，而不是save
