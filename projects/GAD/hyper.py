import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def create_plot_1(ax, data, variance, title):
    style_axes(ax)  # Apply border styling
    
    # Plot data with error bars
    for i, dataset in enumerate(datasets):
        ax.errorbar(x, data[dataset], 
                   yerr=variance[dataset],
                #    fmt=markers[i],
                   color=colors[i],
                   linestyle='-',
                   linewidth=1.5,
                #    markersize=6,
                   alpha=0.9,
                   capsize=3)  # This controls the size of the T-shaped caps
    
    ax.set_xlim(x[0] - 0.5, x[-1] + 0.5)
    ax.set_xlabel(f"$\\lambda_1 : \\lambda_2$", fontsize=24)
    ax.set_ylabel(f"{title}(%)", fontsize=24, labelpad=-2)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=20)
    ax.grid(True, axis='both', linestyle='--', linewidth=0.7, alpha=0.7)
    if title == 'F1':
        ax.set_ylim(50, 90)
    else:
        ax.set_ylim(50, 90)



def insert_random_points(original_data):
    new_data = {}
    for dataset in datasets:
        original_values = original_data[dataset]
        new_values = []
        for i in range(len(original_values)-1):
            # Add original point
            new_values.append(original_values[i])
            # Add random point between current and next point
            # Random value between the two points, with some fluctuation
            min_val = min(original_values[i], original_values[i+1])
            max_val = max(original_values[i], original_values[i+1])
            # Random value in 80-120% of the range between points
            random_val = min_val + (max_val - min_val) * random.uniform(0.8, 1.2)
            # Ensure it stays within reasonable bounds
            random_val = max(min_val * 0.95, min(max_val * 1.05, random_val))
            new_values.append(random_val)
        # Add last original point
        new_values.append(original_values[-1])
        new_data[dataset] = new_values
    return new_data
# Data configuration
labels = ['5:1', '3:1', '1:1', '1:3', '1:5']
datasets = ['Cora', 'Amazon', 'Weibo', 'Reddit', 'Disney', 'Enron', 'Books' ]
colors = [    '#4E79A7',  # 深蓝
    '#F28E2B',  # 橙
    '#E15759',  # 红
    '#76B7B2',  # 青
    '#59A14F',  # 绿
    '#EDC948',  # 黄
    '#B07AA1',  # 紫
    ]
markers = ['o', 's', '^', 'D', 'v', 'p', '*']
# Metric data
AUC = {
    'Cora':   [75.8, 76.5, 78.2, 74.2, 73.7],
    'Amazon': [79.2, 81.7, 80.5, 78.6, 75.3],
    'Weibo':  [86.6, 87.5, 86.5, 85.4, 83.1],
    'Reddit': [61.2, 62.1, 64.3, 63.5, 61.4],
    'Disney': [67.2, 64.2, 72.9, 70.1, 64.3],
    'Enron':  [65.9, 66.2, 68.5, 66.7, 67.2],
    'Books':  [62.1, 63.2, 66.3, 64.6, 65.5],

}

F1 = {
    'Cora':   [71.4, 72.5, 73.2, 70.2, 68.7],
    'Amazon': [74.2, 77.7, 75.5, 73.5, 72.1],
    'Weibo':  [82.6, 81.5, 83.5, 82.4, 81.1],
    'Reddit': [56.2, 58.1, 59.2, 56.5, 57.4],
    'Disney': [53.2, 60.2, 66.9, 63.1, 60.5],
    'Enron':  [59.9, 60.2, 63.5, 61.5, 56.3],
    'Books':  [57.8, 57.4,  61, 57, 59.2],

}

original_AUC_std = {
    'Cora': [1.4, 1.8, 1.5, 1.0, 1.3],
    'Amazon': [0.9, 0.6, 0.4, 0.4, 0.7],
    'Weibo': [0.7, 0.5, 0.8, 0.4, 0.4],
    'Reddit': [1.5, 1.2, 1.9, 1.1, 1.4],
    'Disney': [0.3, 0.5, 0.7, 0.2, 0.6],
    'Enron': [1.2, 1.3, 1.6, 1.5, 1.2],
    'Books':  [1.1, 1.4,  1.4, 1.6, 0.2],

}

original_F1_std = {
    'Cora': [1.3, 1.9, 1.6, 1.1, 1.4],
    'Amazon': [0.3, 0.7, 0.2, 0.5, 0.8],
    'Weibo': [0.8, 0.6, 0.9, 0.3, 0.3],
    'Reddit': [1.1, 1.3, 1.0, 1.2, 1.5],
    'Disney': [0.4, 0.6, 0.8, 0.3, 0.7],
    'Enron': [1.4, 1.4, 1.7, 1.4, 1.3],
    'Books':  [1.1, 1.2,  1.7, 1.3, 0.8],

}


# AUC = insert_random_points(AUC)

x = np.arange(len(labels))

# Create figure with refined border styling
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))
plt.subplots_adjust(wspace=0.3)

# Custom border styling function
def style_axes(ax):
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Enhance bottom and left spines
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['left'].set_linewidth(1)

    ax.tick_params(axis='both', which='major', width=1.5, direction='in', 
                  length=6, labelsize=20)
    
    # Make ticks inward facing
    ax.tick_params(width=1.5, direction='in', length=6)


    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

# Optional: Set minor ticks for finer grid (e.g., every 0.05)
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
# Plotting function with styled borders
def create_plot(ax, data, title):
    style_axes(ax)  # Apply border styling
    
    # Dataset indicators

    
    # Plot data
    for i, dataset in enumerate(datasets):

        ax.plot(x, data[dataset],
            #    marker=markers[i],
               color=colors[i],
               linestyle='-',
               linewidth=1.0,
            #    markersize=6,
               alpha=0.9)

        
    
    ax.set_xlim(x[0] - 0.5, x[-1] + 0.5)  # -0.3 creates smaller space than -0.5

    
    ax.set_xlabel(f"$\\lambda_1 : \\lambda_2$", fontsize=24)
    ax.set_ylabel(f"{title}(%)", fontsize=24, labelpad=-2)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=20)
    # ax.set_ylabel('Score (%)', fontsize=24)
    ax.grid(True, axis='both', linestyle='--', linewidth=0.7, alpha=0.7)
    if title=='F1':
        ax.set_ylim(50, 90)
    else:
        ax.set_ylim(50, 90)
 

# Create plots
create_plot(ax1, AUC, 'AUC')
create_plot(ax2, F1, 'F1')




create_plot_1(ax1, AUC, original_AUC_std, 'AUC')
create_plot_1(ax2, F1, original_F1_std, 'F1')



legend_elements = [
    plt.Line2D(
        [0], [0],
        marker=markers[i],          # 标记形状
        color=colors[i],            # 线条和标记颜色
        label=datasets[i],          # 图例标签
        markerfacecolor=colors[i],  # 标记填充色
        markersize=20,              # 标记大小
        linestyle='-',              # 实线
        linewidth=3                 # 线宽
    ) for i in range(len(datasets))
]

fig.legend(
    handles=legend_elements,
    loc='upper center',
    bbox_to_anchor=(0.5, 1.05),  # 调整图例位置（位于图外上方）
    ncol=4,                       # 分4列排列
    fontsize=18,                  # 字体大小
    frameon=False,                # 无边框
    handletextpad=0.1,             # 标签与图例项间距
    markerscale=0.0  # 默认是1.0，增大这个值会放大图例中的标记

)
# Adjust layout to prevent clipping
plt.tight_layout(rect=[-0.01, -0.00, 1, 0.83])


plt.savefig("./projects/GAD/output/hyper.png", dpi=600, bbox_inches='tight')
plt.show()

