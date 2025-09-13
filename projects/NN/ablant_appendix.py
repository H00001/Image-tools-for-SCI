import matplotlib.pyplot as plt
import numpy as np

# Data and labels
labels = ['a', 'b', 'c', 'd']
SM = np.array([[77.2, 76.4, 74.1, 78],[27.1, 26.5,23.5,28],[33.6, 32.5,28.6,35],[67.4, 64.9, 63.2, 68.5]]) / 100
# SM  = np.array([np.roll(row, -1) for row in SM])
SM = SM[[1, 2, 3, 0], :]




SM_BIO_SY = np.array([[70.2,71.3,69.5,74.4],[15.6, 17.3,14.4,18.3],[20.2, 21.5,16.4,23.5],[63.2, 61.4, 58.7, 64.1]]) / 100
# SM_BIO_SY  = np.array([np.roll(row, -1) for row in SM_BIO_SY])
SM_BIO_SY = SM_BIO_SY[[1, 2, 3, 0], :]


SN = np.array([[65.4,66.2,64.7,69.8],[27.5,28.6,30.8,33.2 ],[33.2, 35.2,36.1,37.4],[55.4,53.1,54.3,57.0]]) / 100
# SN  = np.array([np.roll(row, -1) for row in SN]).T
SN = SN[[1, 2, 3, 0], :]

CV = np.array([[35.5,37.2,37,39.4],[35,36,37,38],[20.5, 22.4,22,23.7],[30,31,32,35.5]]) / 100
# CV  = np.array([np.roll(row, -1) for row in CV]).T
CV = CV[[2, 3, 1, 0], :]

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
    ax.set_xticklabels(labels, fontsize=16, rotation=0)
    ax.tick_params(axis='y', which='major', pad=-2)  # Reduce pad to bring the labels closer
    ax.tick_params(axis='x', which='major', pad=-2)  # Reduce pad to bring the labels closer

    # ax.set_xticklabels(labels, fontsize=16, rotation=15, )

    ax.set_yticks(np.arange(data.shape[0]) + 0.8)
    if xlabel == 'CV':
        ax.set_yticklabels(['ARI', 'NMI', "F1", 'ACC'], fontsize=14, rotation=-40)
    else:
        ax.set_yticklabels(['NMI', 'ARI', "F1", 'ACC'], fontsize=14, rotation=-40)
    
    yticks = ax.get_yticks()
    for label, y in zip(ax.get_yticklabels(), yticks):
        label.set_position((0.9, y, 0))

    ax.set_xlabel("Strategies", fontsize=15, labelpad=6, rotation=35)
    ax.set_title(xlabel, fontsize=13, loc='center', pad=0, y=-0.15)
    ax.set_ylabel('Metrics', fontsize=16, labelpad=8)
    ax.set_zlabel('Score', fontsize=18, labelpad=8)
    ax.set_zlim(0., zlim)
    ax.set_zticks(zticks)
    ax.set_zticklabels([f'{x:.1f}' for x in zticklabels], fontsize=16)
    ax.view_init(elev=14, azim=-52)


# Create figure
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
fig = plt.figure(figsize=(16, 4))

# Subplot 1 and 3 (SM data)
ax1 = fig.add_subplot(141, projection='3d')
plot_3d(ax1, SM, 'SM-SY', 0.82, [0, 0.2, 0.4, 0.6, 0.8], [0, 0.2, 0.4, 0.6, 0.8])

ax3 = fig.add_subplot(142, projection='3d')
plot_3d(ax3, SM_BIO_SY, 'SM-BIO-SY', 0.82, [0, 0.2, 0.4, 0.6, 0.8], [0, 0.2, 0.4, 0.6, 0.8])

# Subplot 2 and 4 (SM_BIO data)
ax2 = fig.add_subplot(143, projection='3d')
plot_3d(ax2, SN, 'SN', 0.71, [0.1, 0.3, 0.5, 0.7], [0.1, 0.3, 0.5, 0.7])

ax4 = fig.add_subplot(144, projection='3d')
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
plt.savefig('./output/addition_ablant.png', dpi=600, transparent=False)
plt.show()
