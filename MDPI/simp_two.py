import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# Generate random data for demonstration
np.random.seed(0)
x = np.linspace(0, 60, 60)

# Data
data = {
    'ACC_GLCC': [58.17, 48.49, 60.20, 54.01, 64.37, 63.44, 64.68, 65.99, 66.00, 52.24, 58.12, 63.43, 61.72, 64.11, 62.69, 68.82, 63.77, 70.89, 72.92, 66.88, 75.11, 74.23, 72.42, 68.37, 74.26, 76.29, 75.44, 76.37, 74.44, 73.37],
    'NMI_GLCC': [0.1807, 0.7648, 0.7179, 0.6240, 0.7857, 0.0150, 0.2528, 0.1034, 0.1746, 0.7855, 0.0147, 0.2893, 0.8669, 0.8372, 0.4364, 0.8822, 0.4169, 0.8780, 0.6394, 0.0494, 0.3730, 0.3139, 0.9922, 0.4050, 0.9557, 0.2556, 0.4047, 0.4743, 0.4500, 0.5420],
    'AAC_DGLC': [56.86, 57.42, 60.37, 64.11, 65.32, 64.71, 64.75, 64.28, 65.39, 64.37, 65.74, 66.43, 67.72, 68.11, 69.69, 67.82, 68.77, 69.89, 72.92, 74.88, 75.11, 76.23, 76.42, 77.37, 77.26, 77.29, 77.44, 77.37, 78.44, 78.37],
    'ACC_UDGC': [54.47, 55.63, 56.15, 57.43, 57.98, 59.03, 59.84, 60.46, 61.69, 62.55, 63.22, 63.79, 64.48, 65.14, 65.86, 67.35, 68.19, 69.06, 69.48, 69.92, 70.72, 71.08, 72.35, 73.38, 74.49, 74.6, 74.6, 74.6, 74.6, 74.6],
    'NMI_DGLC': [0.5632, 1.8386, 2.5321, 1.9579, 1.7485, 2.5559, 1.7957, 1.8173, 2.7470, 2.3428, 2.0917, 1.7619, 2.5777, 2.8522, 4.1608, 4.9478, 4.2127, 4.1789, 4.9053, 4.8988, 4.2698, 4.7948, 4.3274, 4.1512, 4.7966, 4.3818, 4.6326, 4.8607, 4.8002, 4.5727],
    'ACC_OURS': [58.17, 58.49, 59.20, 60.01, 62.37, 63.44, 64.68, 65.99, 66.00, 68.24,
                 70.12, 72.43, 73.72, 74.11, 75.69, 76.82, 77.77, 78.89, 79.92, 80.88,
                 81.11, 80.23, 81.22, 81.1, 81.2, 80.29, 80.4, 80.5, 80.6, 81.01],
    'NMI_OURS': [1.12, 2.89, 3.32, 3.77, 3.56, 3.94, 3.12, 3.30, 3.40, 3.45, 3.47, 3.66, 4.01,
                 4.18, 4.42, 4.79, 5.12, 5.26, 5.21, 5.56, 5.92, 6.15, 6.21, 6.20, 6.22, 6.34,
                 6.35, 6.31, 6.30, 6.28]
}

# Standard deviation ranges
std_ranges = {
    'acc': {'GLCC': (1.5, 4.8), 'DGLC': (0.7, 2.0), 'OURS': (0.5, 1.2), 'UDGC': (0.1, 1.8)},
    'nmi': {'GLCC': (0.0, 0.1), 'DGLC': (0.0, 0.3), 'OURS': (0.1, 0.4)}
}

# Interpolation function
def interpolate_values(values):
    return np.interp(np.linspace(0, len(values), len(values)*2+1), np.arange(len(values)), values)

# Apply interpolation and Gaussian filter to data
for key, values in data.items():
    data[key] = gaussian_filter1d(interpolate_values(values), 1)

# Boundary function
def bd(values, std_min, std_max):
    std_devs = np.linspace(std_min, std_max, len(values))
    return values - std_devs, values + std_devs

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plotting function
def plot_data(ax, x, y_label, y_data, std_ranges, marker_spacing):
    ax.set_ylim(0, max([max(d) for d in y_data.values()]) * 1.1)
    ax.set_xlim(0, 60)
    ax.set_facecolor("#e9e9e9")
    ax.grid(color='white', linestyle='--', linewidth=1)
    ax.set_xlabel('Epoch', fontsize=18)
    ax.set_ylabel(y_label, fontsize=18)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.tick_params(axis='both', which='minor', labelsize=14)

    legend_elements = []
    for key, color in zip(y_data.keys(), ['blue', 'green', 'red', 'yellow']):
        if 'ACC' in key:
            std_range = std_ranges['acc'][key.split('_')[1]]
        else:
            std_range = std_ranges['nmi'][key.split('_')[1]]
        lower_bound, upper_bound = bd(y_data[key], *std_range)
        ax.plot(x, y_data[key], color=color, lw=3)
        ax.fill_between(x, lower_bound, upper_bound, color=color, alpha=0.2)
        ax.scatter(x[::marker_spacing], y_data[key][::marker_spacing], color=color, marker='X' if 'GLCC' in key else 'o' if 'DGLC' in key else 'P' if 'OURS' in key else '+', s=100)
        legend_elements.append(Line2D([0], [0], color=color, lw=3, label=key.split('_')[1], marker='X' if 'GLCC' in key else 'o' if 'DGLC' in key else 'P' if 'OURS' in key else '+', markerfacecolor=color, markersize=10))
    ax.legend(handles=legend_elements, loc='upper left', fontsize=20)

# Plot ACC and NMI data
plot_data(axes[0], x, 'ACC (%)', {k: v for k,     v in data.items() if 'ACC' in k}, std_ranges, marker_spacing=5)
plot_data(axes[1], x, 'NMI', {k: v for k, v in data.items() if 'NMI' in k}, std_ranges, marker_spacing=5)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
