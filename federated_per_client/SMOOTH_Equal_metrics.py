import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 将数据存储在字典中，包含 global 和 client 数据
#CiteSeer
data = {
    'acc': {
        7: {'OURS': (np.array([1, 2, 3, 4, 5,6,7]), np.array([0.8020, 0.7950, 0.6165, 0.7752, 0.5982,0.9411, 0.6882])),
            'FedGCN': (np.array([1, 2, 3, 4, 5,6,7]), np.array([0.54, 0.6411, 0.5020, 0.6211, 0.5193, 0.9291, 0.5443])),
            'Local': (np.array([1, 2, 3, 4, 5,6,7]), np.array([0.6738, 0.5271, 0.5182, 0.503, 0.564, 0.7704, 0.6035]))
            },
        9: {'OURS': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([0.8020, 0.7450, 0.6165, 0.7752, 0.6782,0.9311, 0.7102, 0.7183, 0.6462])),
             'FedGCN': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([0.52, 0.6267, 0.5479, 0.7189, 0.6482, 0.9086, 0.5811, 0.6972, 0.5821])),
             'Local': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([0.6738, 0.5271, 0.5182, 0.503, 0.564, 0.7704, 0.6035, 0.6435, 0.6397]))},
        10: {'OURS': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                        np.array([0.7920, 0.7950, 0.6165, 0.7752, 0.5982,0.9311, 0.7832, 0.6715, 0.6884, 0.6755])),
            'FedGCN': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                        np.array([0.55, 0.5819, 0.5216, 0.5093, 0.6168, 0.9185, 0.6145, 0.5815, 0.6, 0.6286])),
             'Local': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                        np.array([0.6738, 0.5271, 0.5182, 0.503, 0.564, 0.7704, 0.5238, 0.6138, 0.5819, 0.5524]))},
    },
}





# 设置全局字体为微雅软黑
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False  # 保证负号正常显示
plt.rcParams['font.weight'] = 'bold'  # 设置全局字体加粗
# 单独设置一些元素的字体大小（可选）
plt.rcParams['axes.titlesize'] = 16  # 设置标题字体大小
plt.rcParams['axes.labelsize'] = 14  # 设置坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = 12  # 设置x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 12  # 设置y轴刻度字体大小
plt.rcParams['legend.fontsize'] = 12  # 设置图例字体大小

# 设置标题加粗
plt.rcParams['axes.titleweight'] = 'bold'  # 设置标题字体加粗

# 平滑曲线函数
def smooth_curve(x, y):
    spl = make_interp_spline(x, y, k=3)  # k=3表示三次样条插值
    x_new = np.linspace(x.min(), x.max(), 500)  # 生成更多的点来平滑曲线
    y_new = spl(x_new)
    return x_new, y_new


# 选择要绘制的指标
data_names = ['acc']

# 创建图形，设置为 3 行 4 列
fig, axs = plt.subplots(1, 3, figsize=(12, 3))

# 为每个指标和每组数据绘制图形
for i, data_name in enumerate(data_names):
    for j, num_points in enumerate([7,9,10]):
        # 获取 global 和 client 数据
        x_ours, y_ours = data[data_name][num_points]['OURS']
        x_global, y_global = data[data_name][num_points]['FedGCN']
        x_client, y_client = data[data_name][num_points]['Local']

        # 计算平滑曲线
        x_smooth_global, y_smooth_global = smooth_curve(x_global, y_global)
        x_smooth_client, y_smooth_client = smooth_curve(x_client, y_client)
        x_smooth_ours, y_smooth_ours = smooth_curve(x_ours, y_ours)


        # 选择不同的颜色
        color_global = '#E5637B'
        color_client = '#5979A2'
        color_ours = '#008687'
        smooth_color_global = '#E5637B'
        smooth_color_client = '#5979A2'
        smooth_color_ours = '#008687'


        ax = axs[j]  # 交换行列的索引
        ax.bar(x_global, y_global, width=0.3, color=color_global, alpha=0.7, label='FedNCN', zorder=2)
        ax.bar(x_client, y_client, width=0.3, color=color_client, alpha=0.6, label='Local', zorder=3)
        ax.bar(x_ours, y_ours, width=0.3, color=color_ours, alpha=0.5, label='OURS', zorder=1)


        ax.plot(x_smooth_global, y_smooth_global, color=smooth_color_global)
        ax.plot(x_smooth_client, y_smooth_client, color=smooth_color_client)
        ax.plot(x_smooth_ours, y_smooth_ours, color=smooth_color_ours)



        ax.set_xticks(np.arange(1, num_points + 1, 1))
        ax.set_xticklabels(np.arange(1, num_points + 1))
        ax.set_ylim(0, 1.05)


        
axs[0].set_xlabel(f'{data_name.upper()} (SM)')
axs[1].set_xlabel(f'{data_name.upper()} (SM-BIO)')

axs[2].set_xlabel(f'{data_name.upper()} (SM-BIO-SY)')

      
fig.legend(
    labels=['FedGCN','Local', 'OURS'],
    loc='upper center',
    ncol=3,
    bbox_to_anchor=(0.5, 1.05),
    frameon=False
)# 调整布局
plt.tight_layout()

# 图例统一放在所有子图上方
# fig.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.05))  # 调整位置
plt.tight_layout(rect=[0, 0, 1, 0.95])  # 给图例留出空间# plt.savefig("./smo/CiteSeer.png", dpi=400)
# plt.savefig("output/smooth.png", dpi=600)
plt.show()