import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

plt.rcParams.update({
    'font.size': 18,
    'axes.labelsize': 18,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'figure.titlesize': 18
})

methods = ['IFedGC', 'FedNCN', 'FedIIH', 'FedPub', 'FedTAD']
missing_rates = np.array([0.2, 0.3, 0.4, 0.5, 0.6])
X = np.arange(len(methods))

acc_data = np.array([
    # 客户端数 = 5
    [
        # CiteSeer
        [
            [55.4, 53.3, 50.8, 50.5, 46.3],  # 我们的方法
            [51.8, 50.2, 49.0, 46.5, 43.1],  # FedNCN
            [50.7, 49.3, 47.5, 47.0, 42.6],  # FedIIH
            [49.8, 48.0, 48.3, 45.7, 41.9],  # FedPub
            [52.5, 50.1, 50.4, 47.3, 44.0]  # FedTAD
        ],
        # PubMed
        [
            [63.1, 59.7, 59.5, 57.9, 55.2],  # 我们的方法
            [59.4, 57.1, 57.8, 54.9, 52.0],  # FedNCN
            [58.3, 56.5, 54.7, 55.1, 51.3],  # FedIIH
            [57.2, 55.6, 56.0, 53.8, 50.5],  # FedPub
            [59.9, 57.0, 58.1, 55.3, 51.6]  # FedTAD
        ],
        # Computer
        [
            [56.3, 55.8, 51.5, 49.0, 46.4],  # 我们的方法
            [53.2, 52.0, 50.9, 47.8, 45.3],  # FedNCN
            [52.5, 51.1, 48.6, 46.9, 44.0],  # FedIIH
            [51.7, 49.9, 50.2, 47.5, 43.8],  # FedPub
            [54.0, 52.3, 49.7, 48.0, 44.7]  # FedTAD
        ],
        # Photo
        [
            [67.4, 66.1, 62.9, 60.6, 58.0],  # 我们的方法
            [64.2, 63.0, 60.8, 58.3, 55.9],  # FedNCN
            [62.8, 61.2, 59.0, 56.6, 54.4],  # FedIIH
            [61.7, 59.5, 60.1, 57.3, 53.8],  # FedPub
            [65.1, 63.5, 61.0, 58.2, 55.7]  # FedTAD
        ],
        # Cora
        [
            [58.5, 56.0, 55.7, 51.1, 48.5],  # 我们的方法
            [55.3, 53.7, 52.0, 49.5, 46.8],  # FedNCN
            [54.1, 52.9, 50.6, 48.3, 45.7],  # FedIIH
            [53.2, 51.0, 51.5, 48.0, 44.9],  # FedPub
            [56.0, 54.3, 52.5, 49.7, 47.2]  # FedTAD
        ]
    ],

    # 客户端数 = 10
    [
        # CiteSeer
        [
            [54.0, 53.7, 49.6, 47.1, 44.5],  # 我们的方法
            [50.8, 49.6, 48.4, 46.2, 43.9],  # FedNCN
            [49.7, 48.5, 46.8, 45.3, 42.8],  # FedIIH
            [48.6, 46.9, 47.1, 44.7, 41.9],  # FedPub
            [51.3, 49.8, 47.4, 45.0, 42.6]  # FedTAD
        ],
        # PubMed
        [
            [68.0, 66.1, 61.3, 55.8, 53.1],  # 我们的方法
            [63.5, 62.0, 59.2, 56.1, 53.0],  # FedNCN
            [61.7, 60.2, 57.6, 54.3, 51.7],  # FedIIH
            [60.2, 58.3, 57.5, 53.7, 50.5],  # FedPub
            [64.1, 62.7, 59.9, 56.5, 53.8]  # FedTAD
        ],
        # Computer
        [
            [65.0, 61.4, 60.1, 57.5, 54.8],  # 我们的方法
            [61.8, 59.7, 57.6, 54.9, 52.1],  # FedNCN
            [60.5, 58.3, 56.7, 53.8, 50.9],  # FedIIH
            [59.1, 57.4, 57.2, 52.9, 49.7],  # FedPub
            [62.5, 60.9, 58.3, 55.4, 52.5]  # FedTAD
        ],
        # Photo
        [
            [69.2, 67.6, 61.5, 58.9, 56.2],  # 我们的方法
            [65.5, 63.7, 61.0, 58.0, 55.5],  # FedNCN
            [63.9, 62.0, 59.5, 56.2, 53.4],  # FedIIH
            [62.3, 60.4, 60.1, 55.7, 52.8],  # FedPub
            [66.1, 64.2, 61.7, 58.6, 55.8]  # FedTAD
        ],
        # Cora
        [
            [60.1, 59.2, 52.0, 49.3, 46.5],  # 我们的方法
            [56.7, 55.4, 53.0, 50.7, 48.3],  # FedNCN
            [55.4, 54.1, 51.6, 49.2, 46.0],  # FedIIH
            [54.2, 52.5, 52.8, 49.0, 45.3],  # FedPub
            [57.6, 56.3, 53.4, 50.9, 47.8]  # FedTAD
        ]
    ],

    # 客户端数 = 20
    [
        # CiteSeer
        [
            [55.8, 52.8, 48.1, 45.6, 42.9],  # 我们的方法
            [52.4, 50.5, 48.3, 45.1, 42.0],  # FedNCN
            [51.2, 49.4, 46.9, 44.2, 41.4],  # FedIIH
            [50.0, 48.1, 48.4, 43.9, 40.7],  # FedPub
            [50.1, 48.2, 48.7, 46.0, 43.1]  # FedTAD
        ],
        # PubMed
        [
            [69.7, 66.1, 62.7, 59.1, 57.4],  # 我们的方法
            [66.2, 63.8, 61.3, 58.0, 55.2],  # FedNCN
            [64.5, 62.0, 59.1, 56.7, 53.8],  # FedIIH
            [63.1, 60.4, 60.7, 55.9, 52.5],  # FedPub
            [65.3, 64.7, 62.0, 58.9, 56.0]  # FedTAD
        ],
        # Computer
        [
            [73.6, 69.2, 66.4, 61.7, 57.9],  # 我们的方法
            [69.7, 66.8, 64.0, 60.5, 57.2],  # FedNCN
            [68.1, 65.3, 63.0, 59.8, 56.4],  # FedIIH
            [66.5, 63.6, 61.2, 58.0, 54.8],  # FedPub
            [69.9, 67.9, 65.0, 61.4, 58.1]  # FedTAD
        ],
        # Photo
        [
            [72.9, 69.2, 65.6, 60.8, 58.9],  # 我们的方法
            [69.3, 66.4, 64.2, 60.1, 57.6],  # FedNCN
            [67.9, 65.1, 62.3, 59.0, 56.2],  # FedIIH
            [66.1, 63.3, 60.7, 57.3, 54.5],  # FedPub
            [69.5, 67.6, 64.8, 61.0, 58.0]  # FedTAD
        ],
        # Cora
        [
            [60.8, 57.7, 55.1, 50.1, 48.0],
            [54.3, 51.5, 49.2, 45.0, 42.6],
            [52.7, 50.1, 47.8, 44.2, 41.5],
            [55.6, 52.4, 50.2, 46.9, 44.0],
            [51.9, 49.5, 48.3, 44.0, 42.2]
        ]
    ]
])

colors = ['#f18c25', '#db614f', '#715ea9', '#6a9ace', '#1e803d']
pane_color = (1.0, 0.996, 0.959, 1.0)

client_settings = [5, 10, 20]
datasets = ['CiteSeer', 'PubMed', 'Computer', 'Photo', 'Cora']

fig = plt.figure(figsize=(25, 15))

for row in range(3):         # 客户端数
    for col in range(5):     # 数据集
        ax = fig.add_subplot(3, 5, row * 5 + col + 1, projection='3d')
        ax.xaxis.set_pane_color(pane_color)
        ax.yaxis.set_pane_color(pane_color)
        ax.zaxis.set_pane_color(pane_color)
        ax.grid(False)
        ax.xaxis.pane.set_edgecolor((1, 1, 1, 0))
        ax.yaxis.pane.set_edgecolor((1, 1, 1, 0))
        ax.zaxis.pane.set_edgecolor((1, 1, 1, 0))

        # 计算该子图所有值的最小值作为 z_project
        z_min = acc_data[row, col].min()
        z_project = z_min - 3  # 可调偏移值

        for i in range(len(methods)):
            y = missing_rates
            z = acc_data[row, col, i]
            x_center = X[i]
            x1, x2 = x_center - 0.2, x_center + 0.2

            X_top = np.array([[x1]*len(y), [x2]*len(y)])
            Y_top = np.array([y, y])
            Z_top = np.array([z, z])
            Z_bottom = np.full_like(Z_top, z_project)

            ax.plot_surface(Y_top, X_top, Z_top, color=colors[i], alpha=0.6, edgecolor='none', shade=False)
            ax.plot_surface(Y_top, X_top, Z_bottom, color=colors[i], alpha=0.3, edgecolor='none', shade=False)

            # 墙体
            alpha_wall = 0.1
            y0, z0 = y[0], z[0]
            y1, z1 = y[-1], z[-1]

            ax.plot_surface(np.array([[y0, y0], [y0, y0]]),
                            np.array([[x1, x2], [x1, x2]]),
                            np.array([[z0, z0], [z_project, z_project]]),
                            color=colors[i], alpha=alpha_wall, edgecolor='none', shade=False)
            ax.plot_surface(np.array([[y1, y1], [y1, y1]]),
                            np.array([[x1, x2], [x1, x2]]),
                            np.array([[z1, z1], [z_project, z_project]]),
                            color=colors[i], alpha=alpha_wall, edgecolor='none', shade=False)
            ax.plot_surface(np.array([y, y]),
                            np.array([[x1]*len(y), [x1]*len(y)]),
                            np.array([z, [z_project]*len(z)]),
                            color=colors[i], alpha=alpha_wall, edgecolor='none', shade=False)
            ax.plot_surface(np.array([y, y]),
                            np.array([[x2]*len(y), [x2]*len(y)]),
                            np.array([z, [z_project]*len(z)]),
                            color=colors[i], alpha=alpha_wall, edgecolor='none', shade=False)

        ax.set_xlabel('Missing Rate', labelpad=10)
        ax.set_ylabel('Method', labelpad=12)
        ax.set_xticks(missing_rates)
        ax.set_yticks(X)
        ax.set_yticklabels([f"M{i+1}" for i in range(len(methods))])
        ax.set_ylim(-0.5, len(methods)-0.5)
        ax.view_init(elev=15, azim=-25)
        ax.set_title(f"{datasets[col]} | Clients={client_settings[row]}")

# 图例
legend_elements = [Patch(facecolor=colors[i], label=f"M{i+1}: {methods[i]}") for i in range(len(methods))]
fig.legend(handles=legend_elements,
           loc='upper center',
           bbox_to_anchor=(0.5, 0.98),
           ncol=5, fontsize=20, frameon=False)

plt.tight_layout(rect=[0, 0, 1, 0.92])
# plt.savefig('bar.png', dpi=600)
plt.show()