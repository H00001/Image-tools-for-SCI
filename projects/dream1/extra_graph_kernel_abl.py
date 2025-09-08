import matplotlib.pyplot as plt
import numpy as np

# Data and labels
labels = ['SP', 'GK', 'RW', 'WL', "HRW"]
SM_SY = np.array([[61.6, 25.1, 22.5, 57.9],[68.4, 23.5,28.6,61.3],[64.2, 18.5,26,60.3],[70.1, 20.7, 26.5, 63.2],[75.5,27.4,32.1,69.4]]) / 100
SM_SY  = np.array([np.roll(row, -1) for row in SM_SY]).T


SM_BIO_SY = np.array([[63.2, 19.5, 21.4, 57.9],[64.4, 18.5,15,56.3],[68.2, 13.5,16.4,57.3],[68.1, 17.7, 17.5, 60.2],[72.3,22.4,24.5,64.9]]) / 100
SM_BIO_SY  = np.array([np.roll(row, -1) for row in SM_BIO_SY]).T


SN_SY = np.array([[23.5,8.7,9.6,15.5],[21.5,7.7,7.6,17.5],[23.2, 5,8,20.6],[18.5,6.7,7.6,12.5],[26.5,12.7,6.6,16.5]]) / 100
SN_SY  = np.array([np.roll(row, -1) for row in SN_SY]).T


CV = np.array([[31,19,32,28],[26,17,34,28],[28,17,30,27],[30,18,27,26],[34,20,35,31]]) / 100
CV  = np.array([np.roll(row, -1) for row in CV]).T

# Common settings
colors = ['#FAEE85','#7FCB82','#7BB2D6','#918AC2']
dx = dy = 0.85

# Plotting function
def plot_3d(ax, data, xlabel, zlim, zticks, zticklabels, xlabel_rotation=-20):
    xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)
    dz = data.flatten()

    for y, color in zip(np.unique(ypos), colors):
        ax.bar3d(xpos[ypos == y], ypos[ypos == y], zpos[ypos == y], dx, dy, dz[ypos == y], color=color, zsort='average', shade=False, edgecolor='black', linewidth=1)
    
    ax.set_xticks(np.arange(data.shape[1]) + 0.5)
    ax.set_xticklabels(labels, fontsize=14, rotation=25)
    ax.tick_params(axis='y', which='major', pad=-1)  # Reduce pad to bring the labels closer
    ax.tick_params(axis='x', which='major', pad=-1)  # Reduce pad to bring the labels closer

    # ax.set_xticklabels(labels, fontsize=16, rotation=15, )

    ax.set_yticks(np.arange(data.shape[0]) + 0.8)
    if xlabel == 'CV':
        ax.set_yticklabels(['ARI', 'NMI', "F1", 'ACC'], fontsize=14, rotation=-40)
    else:
        ax.set_yticklabels(['NMI', 'ARI', "F1", 'ACC'], fontsize=14, rotation=-40)
    
    yticks = ax.get_yticks()
    for label, y in zip(ax.get_yticklabels(), yticks):
        label.set_position((0.9, y, 0))

    ax.set_xlabel("Graph Kernels", fontsize=15, labelpad=11, rotation=35)
    ax.set_title(xlabel, fontsize=15, loc='center', pad=0, y=-0.15)
    ax.set_ylabel('Metrics', fontsize=16, labelpad=8)
    ax.set_zlabel('Score', fontsize=18, labelpad=8)
    ax.set_zlim(0., zlim)
    ax.set_zticks(zticks)
    ax.set_zticklabels([f'{x:.1f}' for x in zticklabels], fontsize=16)
    ax.view_init(elev=14, azim=-52)


# Create figure
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
fig = plt.figure(figsize=(12, 8))

# Subplot 1 and 3 (SM data)
ax1 = fig.add_subplot(221, projection='3d')
plot_3d(ax1, SM_SY, 'SM-SY', 0.82, [0, 0.2, 0.4, 0.6, 0.8], [0, 0.2, 0.4, 0.6, 0.8])

ax3 = fig.add_subplot(222, projection='3d')
plot_3d(ax3, SM_BIO_SY, 'SM-BIO-SY', 0.82, [0, 0.2, 0.4, 0.6, 0.8], [0, 0.2, 0.4, 0.6, 0.8])

# Subplot 2 and 4 (SM_BIO data)
ax2 = fig.add_subplot(223, projection='3d')
plot_3d(ax2, SN_SY, 'SN-SY', 0.31, [0.0, 0.1, 0.2, 0.3], [0.0, 0.1, 0.2, 0.3])

ax4 = fig.add_subplot(224, projection='3d')
plot_3d(ax4, CV, 'CV', 0.41, [0.0,0.1, 0.2, 0.3, 0.4], [0.0,0.1, 0.2, 0.3, 0.4])

# Layout settings
fig.patch.set_alpha(0)
ax1.patch.set_alpha(0)
ax2.patch.set_alpha(0)
ax3.patch.set_alpha(0)
ax4.patch.set_alpha(0)
ax1.set_facecolor('white')
fig.patch.set_facecolor('white')

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=1, wspace=0.2, hspace=0.2)
plt.tight_layout()

# Save and show the plot
plt.savefig('./projects/dream1/output/GK_2x2_combined.png', dpi=600, transparent=False)
plt.show()
