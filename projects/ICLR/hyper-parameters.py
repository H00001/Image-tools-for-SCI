import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Define data arrays
SM = np.array([[70., 78.4, 80.3, 76.2, 73.4],
               [26.6, 27.5, 29.4, 28, 27.6],
               [32.2, 33.4, 35.5, 34, 33.4],
               [67.2, 71.7, 73.6, 71.5, 63.4]]) / 100

SM_BIO = np.array([[66.4, 68.5, 71.7, 73.2, 70.3],
                   [32.3, 33.1, 35.5, 34.2, 36.4],
                   [34.3, 35.3, 37.2, 36, 34],
                   [57.1, 60.9, 61.4, 60.9, 55]]) / 100

SN = np.array([[67.3, 70.8, 71.4, 69.5, 66.6],
                [34.7, 32.5, 35.1, 33.8, 30.7],
                [32.5, 36.2, 37.3, 36.6, 35.5],
                [60.2, 59.6, 61.0, 58.7, 59.2]])/ 100

CV = np.array([[35.12, 37.05, 40, 37.87,32.16],
                [33.35, 36.42, 38, 35.52, 30.18],
                [22.40, 24.45, 25, 24.61, 21.92],
                [32.27, 33.91, 36, 34.66, 28.37]])/ 100


SM= SM[[1, 2, 3,0], :]
SM_BIO = SM_BIO[[1, 2, 3,0], :]
SN = SN[[1, 2, 3,0], :]
CV = CV[[ 2, 3,1,0], :]
# Set font
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# Create 1x4 grid for subplots
fig, axs = plt.subplots(1, 4, figsize=(14, 3.0),subplot_kw={'projection': '3d'})

# Function to create 3D bar plot
def create_3d_bar(ax, data, labels_x, labels_y, title):
    xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)
    dx = dy = 0.85
    dz = data.flatten()
    colors = ['#FAEE85','#7FCB82','#7BB2D6','#918AC2']
    
    for y, color in zip(np.unique(ypos), colors):
        ax.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], 
                 color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
    
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_xticklabels(labels_x, fontsize=13, rotation=20)
    ax.set_yticks(np.arange(data.shape[0])+0.8)
    ax.set_yticklabels(labels_y, fontsize=13, rotation=-15)
    
    ax.set_xlabel("Ratio", fontsize=13)
    ax.set_ylabel("Metrics", fontsize=13)
    ax.set_zlabel("Values", fontsize=13, rotation=0)

    ax.set_zlim(0, np.max(dz) * 1.1)
    ax.set_zticks(np.linspace(0, np.max(dz), 5))
    ax.set_zticklabels([f'{x:.1f}' for x in np.linspace(0, np.max(dz), 5)], fontsize=14)

    ax.tick_params(axis='y', pad=-2) # 调整 y 轴刻度标签与轴的距离 
    ax.tick_params(axis='x', pad=-1) # 调整 y 轴刻度标签与轴的距离
    ax_pos = ax.get_position()  # Get subplot position in figure coordinates

    if title == "SM":
        fig.text(ax_pos.x0 + ax_pos.width / 2-0.06, ax_pos.y0 - 0.04, title, 
             ha='center', va='top', fontsize=14)
    elif title == "SM-BIO":
        fig.text(ax_pos.x0 + ax_pos.width / 2-0.02, ax_pos.y0 - 0.04, title, 
             ha='center', va='top', fontsize=14)
    elif title == "CV":
        fig.text(ax_pos.x0 + ax_pos.width / 2+0.06, ax_pos.y0 - 0.04, title, 
             ha='center', va='top', fontsize=14)
    else:
        fig.text(ax_pos.x0 + ax_pos.width / 2+0.01, ax_pos.y0 - 0.04, title, 
             ha='center', va='top', fontsize=14)
    ax.view_init(elev=24, azim=-53) #ax2.view_init(elev=26, azim=-45)

    # 23,-58
    # ax.set_title(title, fontsize=14, pad=-140)

# Define labels
labels_x = ['10:1', '5:1', '1:1', '1:5', '1:10']
labels_y = [ 'NMI', 'ARI', 'F1','ACC']

# Create 3D plots
create_3d_bar(axs[0], SM, labels_x, labels_y, "SM")
create_3d_bar(axs[1], SM_BIO, labels_x, labels_y, "SM-BIO")

# Example other subplots (change data as needed)
create_3d_bar(axs[2], SN, labels_x, labels_y, "SN")
create_3d_bar(axs[3], CV, labels_x, [  'ARI', 'NMI','F1','ACC'], "CV")

# Adjust layout
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.1, top=1, wspace=0.15)
plt.tight_layout()

# Save and show plot
script_path = sys.argv[0]
current_dir = os.path.dirname(__file__)
script_name = os.path.basename(sys.argv[0])
plt.savefig(f"{current_dir}/output/{script_name}.png", dpi=600)
plt.show()
