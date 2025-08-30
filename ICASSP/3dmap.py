import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
import seaborn as sns

name = "F1"

# Example data
y_labels = ['a', 'b', 'c', 'd', 'e']
x_labels = ['a', 'b', 'c', 'd', 'e']
values_0_0 = np.array([
    [0.7238, 0.7241, 0.7241, 0.7244, 0.7244],
    [0.6928, 0.7244, 0.7253, 0.7244, 0.7244],
    [0.6486, 0.6943, 0.7244, 0.7256, 0.7241],
    [0.6142, 0.6417, 0.6946, 0.7241, 0.7256],
    [0.6061, 0.6227, 0.6423, 0.6943, 0.7241]
])*100

values_0_1 = np.array([
[0.725, 0.7229, 0.7248, 0.7011, 0.6828],
    [0.7071, 0.7066, 0.7174, 0.699, 0.6827],
    [0.6918, 0.692, 0.6915, 0.6929, 0.69],
    [0.6936, 0.6928, 0.6932, 0.6926, 0.6898],
    [0.6928, 0.6932, 0.6937, 0.6932, 0.693]
])*100

values_0_2 = np.array([
[0.843, 0.8813, 0.8336, 0.8339, 0.8343],
    [0.8405, 0.8437, 0.8806, 0.8339, 0.8339],
    [0.846, 0.8467, 0.8429, 0.8811, 0.8339],
    [0.846, 0.846, 0.8467, 0.8429, 0.8807],
    [0.846, 0.8469, 0.8438, 0.847, 0.8429]
])*100

values_1_0 = np.array([
 [0.7093, 0.7241, 0.7238, 0.7247, 0.7244],
    [0.6916, 0.7196, 0.7247, 0.7244, 0.7244],
    [0.6471, 0.6949, 0.7226, 0.7256, 0.7241],
    [0.5951, 0.6417, 0.6946, 0.7241, 0.7256],
    [0.5855, 0.5924, 0.6423, 0.6943, 0.7241]
])*100

values_1_1 = np.array([
[0.7325, 0.733, 0.7294, 0.7368, 0.7016],
    [0.7253, 0.7255, 0.7245, 0.7248, 0.7011],
    [0.7072, 0.7071, 0.7065, 0.7174, 0.699],
    [0.6918, 0.6918, 0.692, 0.6915, 0.6929],
    [0.6928, 0.6936, 0.6928, 0.6932, 0.6926]
])*100

values_1_2 = np.array([
   [0.8649, 0.8607, 0.834, 0.8339, 0.8343],
    [0.8419, 0.8438, 0.8815, 0.834, 0.8339],
    [0.8408, 0.8406, 0.8437, 0.8808, 0.8339],
    [0.8426, 0.8449, 0.8468, 0.8429, 0.8807],
    [0.843,  0.8448, 0.8466, 0.8468, 0.8429]
])*100

values_2_0 = np.array([
[0.6856, 0.7072, 0.7235, 0.7247, 0.7247],
    [0.6859, 0.7078, 0.7247, 0.7244, 0.7247],
    [0.6321, 0.6949, 0.7193, 0.7256, 0.7244],
    [0.5951, 0.6441, 0.6949, 0.7223, 0.7256],
    [0.5861, 0.5927, 0.6429, 0.6943, 0.7241]
])*100

values_2_1 = np.array([
   [0.7337, 0.7338, 0.7336, 0.7322, 0.7367],
    [0.7306, 0.7326, 0.733, 0.7293, 0.7368],
    [0.7241, 0.7241, 0.725, 0.7225, 0.7248],
    [0.7072, 0.7072, 0.707, 0.7065, 0.7174],
    [0.6918, 0.6918, 0.6918, 0.692, 0.6915]
])*100

values_2_2 = np.array([
      [0.835, 0.8724, 0.8494, 0.8349, 0.8343],
    [0.8438, 0.865, 0.8577, 0.834, 0.8339],
    [0.8412, 0.8417, 0.8439, 0.8815, 0.834],
    [0.8402, 0.8406, 0.8406, 0.8437, 0.8807],
    [0.8428, 0.8423, 0.8447, 0.8468, 0.8429]
])*100

values_3_0 = np.array([
    [0.6249, 0.6874, 0.7081, 0.7232, 0.7247],
    [0.6171, 0.6823, 0.7078, 0.7238, 0.7247],
    [0.6047, 0.6877, 0.7078, 0.725, 0.7244],
    [0.5987, 0.6372, 0.6937, 0.719, 0.7256],
    [0.5891, 0.5933, 0.6441, 0.6946, 0.7223]    
])*100

values_3_1 = np.array([
 [0.7328, 0.7328, 0.7325, 0.7337, 0.7322],
    [0.7332, 0.7337, 0.7338, 0.7336, 0.7322],
    [0.7314, 0.7306, 0.7317, 0.733, 0.7294],
    [0.7248, 0.7241, 0.7253, 0.7254, 0.7225],
    [0.7072, 0.7072, 0.7072, 0.7078, 0.7065]
])*100


values_3_2 = np.array([
    [0.8333, 0.835, 0.8736, 0.8476, 0.8345],
    [0.8313, 0.8363, 0.8723, 0.8489, 0.8349],
    [0.8416, 0.8438, 0.865, 0.8574, 0.834],
    [0.842, 0.8412, 0.8413, 0.8433, 0.8821],
    [0.8397, 0.8402, 0.8408, 0.8407, 0.8437]
])*100

values_4_0 = np.array([
[0.6201, 0.624, 0.6859, 0.7081, 0.7235],
    [0.6192, 0.6237, 0.6856, 0.7075, 0.7235],
    [0.6171, 0.618, 0.6811, 0.7075, 0.7238],
    [0.5981, 0.6041, 0.6865, 0.7081, 0.725],
    [0.5945, 0.5984, 0.6372, 0.694, 0.7193]
])*100

values_4_1 = np.array([
     [0.7329, 0.7336, 0.7329, 0.7338, 0.7336],
    [0.7328, 0.7328, 0.7328, 0.733, 0.7337],
    [0.7325, 0.7332, 0.7325, 0.7338, 0.7336],
    [0.7314, 0.7314, 0.7306, 0.7317, 0.733],
    [0.7258, 0.7248, 0.7241, 0.7253, 0.7254]
])*100

values_4_2 = np.array([
   [0.8318, 0.8342, 0.834, 0.8739, 0.8477],
    [0.8312, 0.8334, 0.8347, 0.8739, 0.8478],
    [0.827, 0.8313, 0.8352, 0.8724, 0.8496],
    [0.8424, 0.8416, 0.8438, 0.8649, 0.8578],
    [0.8419, 0.842, 0.8412, 0.8413, 0.8433]
])*100

values_5_0 = np.array([
    [81.2, 80.12, 80.03, 78.42, 75.03],
    [80.1, 81.26, 80.13, 80.34, 78.01],
    [79.1, 81.35, 81.26, 80.67, 80.86],
    [78.6, 79.46, 80.18, 80.2, 80.41],
    [75.2, 74.43, 79.22, 80.24, 81.26],
])

values_5_1 = np.array([
    [81.2, 80.12, 80.03, 78.42, 75.03],
    [80.1, 81.26, 80.13, 80.34, 78.01],
    [79.1, 81.35, 81.26, 80.67, 80.86],
    [78.6, 79.46, 80.18, 80.2, 80.41],
    [75.2, 74.43, 79.22, 80.24, 81.26],
])









# Create the color map
num_colors = 99
cmap = sns.color_palette("summer", as_cmap=True)
cmap = plt.cm.viridis


# Create x and y grid
x = np.arange(len(x_labels))
y = np.arange(len(y_labels))
X, Y = np.meshgrid(x, y)

# Create a 5x3 grid of subplots
fig = plt.figure(figsize=(8, 15))  # Adjust the figure size as necessary
fig.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0.05, wspace=0.05)

# Loop over the positions in the grid and create the plots
for i in range(5):
    for j in range(3):
        base = [[58,80],[60,75],[70,90]]
        z_values = eval(f"values_{i}_{j}").T
        norm = colors.BoundaryNorm(boundaries=np.linspace(np.min(z_values), np.max(z_values), 100), ncolors=cmap.N)

        ax = fig.add_subplot(5, 3, i * 3 + j + 1, projection='3d')
        # Plot the 3D surface
        surf = ax.plot_surface(X, Y, z_values, facecolors=cmap(norm(z_values)), shade=False, edgecolor='k', linewidth=0.5, antialiased=True)
        # ax.plot_surface(X, Y, np.zeros_like(z_values), facecolors=cmap(norm(z_values)), shade=False)

        surf = ax.plot_surface(X, Y,  np.zeros_like(z_values) + base[j][0], facecolors=cmap(norm(z_values)), shade=False, edgecolor='k', linewidth=0.5, antialiased=True, rstride=1, cstride=1)

        # Set axis labels and titles
        ax.set_xticks(x)
        ax.set_xticklabels(x_labels, fontsize=18)
        ax.set_yticks(y)
        ax.set_yticklabels(y_labels, fontsize=18)
        ax.tick_params(axis='x', which='major', pad=-2)  # 控制x轴刻度标签与轴的距离
        ax.tick_params(axis='y', which='major', pad=-2)  # 控制x轴刻度标签与轴的距离
        ax.tick_params(axis='z', which='major', pad=-2)  # 控制x轴刻度标签与轴的距离

        if j == 0:
            ax.set_zlabel(f"{name} (%)", rotation=90, fontsize=18)
        ax.set_ylabel(r'$\lambda$', fontsize=14)
        ax.set_xlabel(r'$\mu$', fontsize=14)

        # Adjust view angle
        ax.view_init(elev=17, azim=-132)

        # Beautify the plot
        ax.set_facecolor('white')
        fig.patch.set_facecolor('white')
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.set_zlim( base[j][0],  base[j][1])

        ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.tick_params(axis='z', labelsize=16)  # 设置z轴刻度标签的字体大小为16

        if j == 2:
            ax.text2D(0.12, 0.01, f'$\eta={chr(97 + i)}$', rotation=-90, fontsize=16, 
              ha='right', va='top', bbox=dict(
                  facecolor='white',
                  alpha=0.7,
                  edgecolor='#222222',
                  boxstyle='round,pad=0.2'
              ))
        line = ['CITE', 'ENZYMES', 'HHAR']
        if i == 0:
            ax.text2D(0.0, 0.08, line[j], rotation=0, fontsize=16, 
              ha='center', va='top')
        # z_ticks = np.linspace(np.min(z_values), np.max(z_values), 15)  # 生成10个等距的刻度

        # ax.set_zticks(z_ticks)  # 设置z轴的刻度
        # ax.tick_params(axis='z', labelsize=16)  # 设置z轴刻度标签的字体大小为14
        import matplotlib.ticker as ticker

        ax.zaxis.set_major_locator(ticker.MultipleLocator(5))

# 设置坐标轴背景透明
        ax.patch.set_alpha(0)
fig.patch.set_alpha(0)

plt.subplots_adjust(wspace=0.1, hspace=-0.1, left=0.070, right=0.95, top=1, bottom=0.05)
plt.tight_layout()

plt.savefig('./fig8_last_v2.png', dpi=600)

plt.show()
