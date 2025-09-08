import numpy as np 
import matplotlib.pyplot as plt 
# ==== 数据示例 ==== 
iterations = np.linspace(1, 20, 11) 
# 0,0.1,...,1 
data = { "SM": { 
    "SIM": [0.76, 0.82, 0.80, 0.83, 0.85, 0.82, 0.81, 0.85, 0.83, 0.87, 0.82], 
    "DIV": [0.82, 0.76, 0.68, 0.78, 0.79, 0.88, 0.85, 0.82, 0.82, 0.83, 0.84], # "
    "ARI": [31.8, 32.2, 34.3, 33.2, 35.5, 34.6, 33.5, 33.3, 32.1, 30.0, 30.2] }, 
"SM-BIO": { "SIM": [0.72, 0.83, 0.86, 0.81, 0.84, 0.87, 0.92, 0.88, 0.89, 0.86, 0.9], 
"DIV": [0.69, 0.75, 0.78, 0.94, 0.90, 0.86, 0.85, 0.83, 0.84, 0.85, 0.84], # 
"ARI": [20.0, 20.4, 21.6, 22.1, 23.5, 22.8, 21.5, 20.8, 19.3, 18.7, 16.4] },
 "SM-BIO-SY": { "SIM": [0.8, 0.77, 0.72, 0.84, 0.92, 0.88, 0.95, 0.93, 0.93, 0.92, 0.90 ],
  "DIV": [0.85, 0.81, 0.84, 0.80, 0.83, 0.82, 0.86, 0.86, 0.88, 0.9, 0.87], # 
  "ARI": [23.5, 24.6, 25.8, 26.5, 27.3, 26.1, 25.4, 25.6, 24.7, 23.1, 22.8] }, 
  "SN": { "SIM": [0.73, 0.75, 0.78, 0.79, 0.76, 0.78, 0.74, 0.75,0.73, 0.72, 0.75], 
  "DIV": [1,1,1,1,1,1,1,1,1,1,1], # 
  "ARI": [23.5, 24.6, 25.8, 26.5, 27.3, 216.1, 25.4, 25.6, 24.7, 23.1, 22.8] },
   "CV": { "SIM": [0.97, 0.97, 0.97, 0.92,0.93,0.92,0.94,0.96,0.95,0.92,0.92], 
"DIV": [0.57,0.52,0.58,1,1,1,1,1,1,1,1], #
 "ARI": [23.5, 24.6, 25.8, 26.5, 27.3, 26.1, 25.4, 25.6, 24.7, 23.1, 22.8] } } 
colors = ['r', 'gold', 'c', 'b', 'm'] # 红, 金色, 青色, 蓝色, 品红 markers = ['o', 's', '^', 'p', 'D'] # 圆圈, 方块, 三角形, 五边形, 菱形

markers = ['o', 's', '^', 'p', 'D'] # 圆圈, 方块, 三角形, 五边形, 菱形

handles = []
labels = []

def plot_metric(ax, metric_name): 
    global handles, labels
    for i, dataset in enumerate(data.keys()): 
        line, = ax.plot(iterations, data[dataset][metric_name],
                        marker=markers[i], color=colors[i], label=dataset) 
        if metric_name == "SIM":  # 只收集一次，避免重复
            handles.append(line)
            labels.append(dataset)
    ax.set_ylabel(metric_name, fontsize=14) 
    ax.set_xlabel(r'Epochs', fontsize=16) 
    ax.set_ylim(0.5, 1) 
    ax.grid(True) 
    ax.tick_params(axis='both', labelsize=12)
    ax.set_xticks(np.arange(0, 21, 2))



# === 绘图 ===
metrics = ["SIM", "DIV"] 
fig, axes = plt.subplots(1, 3, figsize=(10, 3), gridspec_kw={'width_ratios':[1,1,0.3]})

# 前两个子图画图
for i, metric in enumerate(metrics):
    plot_metric(axes[i], metric)

# 第三个子图专门放 legend
axes[2].axis('off')
axes[2].legend(handles, labels, loc='center', fontsize=12)

plt.subplots_adjust(wspace=0.3, left=0.15, right=0.95, bottom=0.15)
plt.tight_layout()

plt.show()