import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from matplotlib.lines import Line2D
from matplotlib.collections import PathCollection

# Generate random data for demonstration
np.random.seed(0)
x = np.linspace(0, 60, 60)
ACC_GLCC = [58.17, 48.49, 60.20, 54.01, 64.37, 63.44, 64.68, 65.99, 66.00, 52.24,
           58.12, 63.43, 61.72, 64.11, 62.69, 68.82, 63.77, 70.89, 72.92, 66.88,
           75.11, 74.23, 72.42, 68.37, 74.26, 76.29, 75.44, 76.37, 74.44, 73.37] 


NIM_GLCC = [0.1807, 0.7648, 0.7179, 0.6240, 0.7857, 0.0150, 0.2528, 0.1034, 0.1746, 0.7855, 
            0.0147, 0.2893, 0.8669, 0.8372, 0.4364, 0.8822, 0.4169, 0.8780, 0.6394, 0.0494, 
            0.3730, 0.3139, 0.9922, 0.4050, 0.9557, 0.2556, 0.4047, 0.4743, 0.4500, 0.5420] 
AAC_DGLC = [56.86, 57.42, 60.37, 64.11, 65.32, 64.71, 64.75, 64.28, 65.39, 64.37,
           65.74, 66.43, 67.72, 68.11, 69.69, 67.82, 68.77, 69.89, 72.92, 74.88,
           75.11, 76.23, 76.42, 77.37, 77.26, 77.29, 77.44, 77.37, 78.44, 78.37] 

NMI_DGLC = [0.5632, 1.8386, 2.5321, 1.9579, 1.7485, 2.5559, 1.7957, 1.8173, 2.7470, 2.3428, 
            2.0917, 1.7619, 2.5777, 2.8522, 4.1608, 4.9478, 4.2127, 4.1789, 4.9053, 4.8988, 
            4.2698, 4.7948, 4.3274, 4.1512, 4.7966, 4.3818, 4.6326, 4.8607, 5.8002, 4.5727]

ACC_OURS = [58.17, 58.49, 59.20, 60.01, 62.37, 63.44, 64.68, 65.99, 66.00, 68.24,
           70.12, 72.43, 73.72, 74.11, 75.69, 76.82, 77.77, 78.89, 79.92, 80.88,
           81.11, 82.23, 83.42, 83.37, 83.26, 83.29, 83.44, 83.37, 83.44, 83.37]

ACC_OURS = [58.17, 58.49, 59.20, 60.01, 62.37, 63.44, 64.68, 65.99, 66.00, 68.24,
           70.12, 72.43, 73.72, 74.11, 75.69, 76.82, 77.77, 78.89, 79.92, 80.88,
           81.11, 82.23, 83.42, 83.37, 83.26, 83.29, 83.44, 83.37, 83.44, 83.37]

NMI_OURS = [1.12,2.89,3.32,3.77,3.56,3.94,3.12,3.30,3.40,3.45,3.47,3.66,4.01,
            4.18,4.42,4.79,5.12,5.26,5.21,5.56,5.92,6.15,6.21,6.20,6.22,6.34,
            6.45,6.21,6.19,6.24]
name = "acc"
if name=="acc":
    y1_GLCC = ACC_GLCC
    y2_UDGC = AAC_DGLC
    y3_OURS = ACC_OURS
    y1_std_min, y1_std_max =  1.5, 4.8
    y2_std_min, y2_std_max = 0.7, 2.0
    y3_std_min, y3_std_max = 0.5, 1.8
    plt.ylim(50,90)
    plt.xlim(0, 60)

else:
    y1_GLCC = NIM_GLCC
    y2_UDGC = NMI_DGLC
    y3_OURS = NMI_OURS
    plt.ylim(00,20)
    plt.xlim(0, 60)

    y1_std_min, y1_std_max = 0.0, 0.1
    y2_std_min, y2_std_max = 0.0, 0.3
    y3_std_min, y3_std_max = 0.1, 0.4



def interpolate_values(values):
    interpolated_values = []
    for i in range(len(values) - 1):
        interpolated_values.append(values[i])
        interpolated_values.append((values[i] + values[i + 1]) / 2)
    interpolated_values.append(values[-1])
    interpolated_values.append(values[-1])
    return interpolated_values

y1_GLCC = interpolate_values(y1_GLCC)
y2_UDGC = interpolate_values(y2_UDGC)
y3_OURS = interpolate_values(y3_OURS)

y1_GLCC = gaussian_filter1d(y1_GLCC, 1)
y2_UDGC = gaussian_filter1d(y2_UDGC, 1)
y3_OURS = gaussian_filter1d(y3_OURS, 1)

# Calculate mean and standard deviation for each line
mean1, std1 = np.mean(y1_GLCC), np.std(y1_GLCC)
mean2, std2 = np.mean(y2_UDGC), np.std(y2_UDGC)
mean3, std3 = np.mean(y3_OURS), np.std(y3_OURS)

def bd(l, sta, end):
    std_devs = np.linspace(sta, end, 60)
    lower_bounds = l - std_devs
    upper_bounds = l + std_devs
    return lower_bounds, upper_bounds

y1_GLCC_lowm, y1_GLCC_upp = bd(y1_GLCC, y1_std_min, y1_std_max)
y2_UDGC_lowm, y2_UDGC_upp = bd(y2_UDGC, y2_std_min, y2_std_max)
y3_OURS_lowm, y3_OURS_upp = bd(y3_OURS, y3_std_min, y3_std_max)

# Reduce the number of points to add markers
marker_spacing = 5  # Add a marker every 5 points

# Plotting the lines with shaded areas representing mean ± standard deviation
plt.figure(figsize=(12,8), facecolor='#f1f1f1')  # Set figure background to gray

plt.tick_params(axis='both', which='major', labelsize=28)

# Plotting Line 1 with shaded region
line1, = plt.plot(x, y1_GLCC, color='blue', lw=3)
plt.fill_between(x, y1_GLCC_lowm, y1_GLCC_upp, color='blue', alpha=0.2)

# Adding triangle markers for every 5th data point in y1_GLCC
markers1 = plt.scatter(x[::marker_spacing], y1_GLCC[::marker_spacing], color='blue', marker='X', s=100, zorder=5)

# Plotting Line 2 with shaded region
line2, = plt.plot(x, y2_UDGC, color='green', lw=3)
plt.fill_between(x, y2_UDGC_lowm, y2_UDGC_upp, color='green', alpha=0.2)

# Adding circle markers for every 5th data point in y2_UDGC
markers2 = plt.scatter(x[::marker_spacing], y2_UDGC[::marker_spacing], color='green', marker='o', s=100, zorder=5)

# Plotting Line 3 with shaded region
line3, = plt.plot(x, y3_OURS, color='red', lw=3)
plt.fill_between(x, y3_OURS_lowm, y3_OURS_upp, color='red', alpha=0.2)

# Adding square markers for every 5th data point in y3_OURS
markers3 = plt.scatter(x[::marker_spacing], y3_OURS[::marker_spacing], color='red', marker='P', s=100, zorder=5)

# Customize font
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 24


plt.xlabel('Epoch', fontproperties='Microsoft YaHei', fontsize=24)
plt.ylabel('ACC (%)', fontproperties='Microsoft YaHei', fontsize=24)

# Set grid to white
plt.grid(True, color='white')  # Set grid color to white

# Create a custom legend for lines and markers together
legend_elements = [
    Line2D([0], [0], color='blue', lw=3, label='GLCC', marker='X', markerfacecolor='blue', markersize=10),
    Line2D([0], [0], color='green', lw=3, label='DGLC', marker='o', markerfacecolor='green', markersize=10),
    Line2D([0], [0], color='red', lw=3, label='OURS', marker='P', markerfacecolor='red', markersize=10)
]
plt.gca().set_facecolor('#f1f1f1')  # Set axes background to light gray

plt.legend(handles=legend_elements, loc='upper left', fontsize=24)

plt.show()
