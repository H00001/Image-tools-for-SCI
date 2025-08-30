import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data setup
x_labels = ['100', '10', '1', '0.1', '0.01']
y_labels = ['0.01', '0.1', '1', '10', '100']

ACC_values = np.array([
    [82.7, 80.12, 80.03, 78.42, 75.03],  
    [80.1, 82.26, 80.13, 80.34, 78.01],  
    [79.1, 81.35, 82.26, 80.67, 80.86],  
    [78.6, 79.46, 80.18, 82.2, 80.41],  
    [75.2, 74.43, 79.22, 80.24, 82.26],  
])
ACC_values = np.rot90(ACC_values)

ARI_values = np.array([
    [6.98, 6.42, 6.42, 6.42, 5.97],  
    [7.01, 7.75, 6.53, 6.30, 5.51],  
    [7.24, 7.88, 8.27, 6.7, 5.62],  
    [7.98, 7.06, 8.26, 8.14, 6.89],  
    [8.05, 8.13, 8.02, 7.46, 8.21],  
])
ARI_values = np.rot90(ARI_values)

NMI_values = np.array([
    [3.95, 3.78, 3.23, 3.4, 3.2],  
    [3.97, 3.99, 3.45, 3.24, 3.5],  
    [4.12, 3.74, 4.18, 3.40, 3.1],  
    [4.05, 3.85, 3.88, 4.17, 3.4],  
    [4.14, 3.96, 3.72, 3.54, 3.57],  
])
NMI_values = np.rot90(NMI_values)

F1_values = np.array([
    [81.26, 76.12, 75.66, 74.867, 73.11],  
    [76.15, 82.29, 77.3, 74.14, 76.01],  
    [74.18, 77.35, 83.28, 77.25, 74.76],  
    [74.13, 76.81, 76.69, 82.29, 76.3],  
    [73.25, 76.43, 74.38, 76.24, 82.29],  
])
F1_values = np.rot90(F1_values)

# Colormap setup
cmap = sns.color_palette("Blues", as_cmap=True)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Data and titles
values = [ACC_values, ARI_values, NMI_values, F1_values]
titles = ['ACC', 'ARI', 'NMI', 'F1']

# Adjust the spacing between subplots
fig.subplots_adjust(left=0.05, right=0.95, top=1, bottom=0.05, hspace=0.3, wspace=0.2)

# Plot each metric's data
for ax, value, title in zip(axes.ravel(), values, titles):
    im = ax.imshow(value, cmap=cmap, aspect='auto')
    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_xticklabels(x_labels, fontsize=14)
    ax.set_yticks(np.arange(len(y_labels)))
    ax.set_yticklabels(y_labels, fontsize=14)
    ax.set_xlabel(r'$\lambda$', fontsize=16)
    ax.set_ylabel(r'$\mu$', fontsize=16)
    ax.set_title(title, fontsize=18)

    # Add colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.set_label(f"{title} (%)", rotation=270, fontsize=14)

# Show the plot
plt.show()
