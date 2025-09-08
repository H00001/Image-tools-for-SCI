from matplotlib.ticker import MultipleLocator
from get_max import get_value, get_value1
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Create a 2x3 grid of subplots
fig, axs = plt.subplots(2, 3, figsize=(12, 6))  # 2 rows, 3 columns
plt.subplots_adjust(wspace=0.3, hspace=0.4)  # Adjust spacing between subplots

# Define datasets to plot
datasets = [
    {"NAME": "ACM", "file": "res/acm seed=10.txt", "ylim": (0, 1)},
    {"NAME": "CITE", "file": "res/cite seed=1.txt", "ylim": (0, 0.8)},
    {"NAME": "ENZYMES", "file": "res/ENZYMES seed=8.txt", "ylim": (0, 0.9)},
    {"NAME": "REUT", "file": "res/reut seed=4.txt", "ylim": (0, 0.9)},
    {"NAME": "HHAR", "file": "res/hhar seed=2.txt", "ylim": (0, 0.95)},
    # The last subplot (2,3) will be empty except for the legend
]

indices = list(range(0, 201))

# Plot data for each dataset
for i, dataset in enumerate(datasets):
    row = i // 3
    col = i % 3
    ax = axs[row, col]
    
    if dataset["NAME"] == 'ACM':
        accs, nmis, aris, f1s = get_value(dataset["file"])
    elif dataset["NAME"] == 'CITE' or dataset["NAME"] == 'ENZYMES' or dataset["NAME"] == 'REUT':
        accs, nmis, aris, f1s = get_value1(dataset["file"])
    else:
        accs, nmis, aris, f1s = get_value(dataset["file"])
    
    ax.plot(indices, accs[0:], label='ACC', color='#ffa600', linewidth=2)
    ax.plot(indices, nmis[0:], label='NMI', color='#0088c7', linewidth=2)
    ax.plot(indices, aris[0:], label='ARI', color='#9680db', linewidth=2)
    
    ax.set_ylim(dataset["ylim"])
    ax.set_xticks(range(0, 201, 50))
    ax.set_title(dataset["NAME"], fontname='Times New Roman', fontsize=28, weight='bold')
    
    # Customize ticks and grid for each subplot
    ax.tick_params(axis='both', which='major', labelsize=24)
    for tick in ax.get_xticklabels():
        tick.set_fontname('Times New Roman')
        tick.set_fontweight('bold')
    for tick in ax.get_yticklabels():
        tick.set_fontname('Times New Roman')
        tick.set_fontweight('bold')
    
    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    ax.yaxis.set_minor_locator(MultipleLocator(0.05))
    
    ax.grid(which='major', linestyle='-', linewidth=1)
    ax.grid(which='minor', linestyle='-', linewidth=0.5)
    
    ax.set_xlabel('Epochs', fontname='Times New Roman', fontweight='bold', size=24)
    if i ==0 or i ==3 :
        ax.set_ylabel('Scores', fontname='Times New Roman', fontweight='bold', size=24)

# Create legend in the bottom-right subplot (2,3)
font = FontProperties(family='Times New Roman', style='normal', size=24, weight='bold')
axs[1, 2].axis('off')  # Turn off axes for the last subplot
lines = [
    plt.Line2D([0], [0], color='#ffa600', linewidth=3),
    plt.Line2D([0], [0], color='#0088c7', linewidth=3),
    plt.Line2D([0], [0], color='#9680db', linewidth=3)
]
axs[1, 2].legend(lines, ['ACC', 'NMI', 'ARI'], 
                loc='center', prop=font, framealpha=1)

plt.tight_layout()
plt.savefig('multi_plot_with_legend.png', dpi=600)
# plt.show()