import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

data_cv = {
    'acc': {
        3: {'OURS': (np.array([1, 2, 3]), np.array([0.355, 0.383, 0.399])),
            'FedGCN': (np.array([1, 2, 3]), np.array([0.331, 0.372, 0.344])),
            'Local': (np.array([1, 2, 3]), np.array([0.268, 0.285, 0.363]))
            },
    },
    'nmi': {
        3: {'OURS': (np.array([1, 2, 3]), np.array([0.353, 0.373, 0.392])),
            'FedGCN': (np.array([1, 2, 3]), np.array([0.266, 0.305, 0.27])),
            'Local': (np.array([1, 2, 3]), np.array([0.286, 0.259, 0.258]))},
            },
    'ari': {
        3: {'OURS': (np.array([1, 2, 3]), np.array([0.248, 0.27, 0.20])),
            'FedGCN': (np.array([1, 2, 3]), np.array([0.19, 0.25, 0.154])),
            'Local': (np.array([1, 2, 3]), np.array([0.16, 0.15, 0.12]))},
    },
    'f1': {
        3: {'OURS': (np.array([1, 2, 3]), np.array([0.31, 0.35, 0.40])),
            'FedGCN': (np.array([1, 2, 3]), np.array([0.29, 0.30, 0.33])),
            'Local': (np.array([1, 2, 3]), np.array([0.18, 0.164, 0.20]))},
        }
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
    spl = make_interp_spline(x, y, k=5)  # k=3表示三次样条插值
    x_new = np.linspace(x.min(), x.max(), 500)  # 生成更多的点来平滑曲线
    y_new = spl(x_new)
    return x_new, y_new

data=data_cv

x_base = np.array([1, 2, 3])

bar_width = 0.25
offset_gap = 0.28


# 选择要绘制的指标
data_names = ['acc','nmi','ari','f1']

# 创建图形，设置为 3 行 4 列
fig, axs = plt.subplots(1, 4, figsize=(8, 3))

# 为每个指标和每组数据绘制图形
for i, data_name in enumerate(data_names):
    for j, num_points in enumerate([3]):
        # 获取 global 和 client 数据
        x_ours, y_ours = data[data_name][num_points]['OURS']

        x_global, y_global = data[data_name][num_points]['FedGCN']
        x_client, y_client = data[data_name][num_points]['Local']

        x_ours   = x_base - offset_gap
        x_global = x_base
        x_client = x_base + offset_gap

        # 计算平滑曲线
        # x_smooth_global, y_smooth_global = smooth_curve(x_global, y_global)
        # x_smooth_client, y_smooth_client = smooth_curve(x_client, y_client)
        # x_smooth_ours, y_smooth_ours = smooth_curve(x_ours, y_ours)


        # 选择不同的颜色
        color_global = '#E5637B'
        color_client = '#5979A2'
        color_ours = '#008687'
        smooth_color_global = '#E5637B'
        smooth_color_client = '#5979A2'
        smooth_color_ours = '#008687'


        # 绘制 global 和 client 数据的柱状图和曲线
        ax = axs[i]  # 交换行列的索引
        ax.bar(x_ours, y_ours, width=0.3, color=color_ours, alpha=0.7, label='OURS', zorder=1)
        ax.bar(x_global, y_global, width=0.3, color=color_global, alpha=0.7, label='FedNCN', zorder=2)
        ax.bar(x_client, y_client, width=0.3, color=color_client, alpha=0.7, label='Local', zorder=3)

        # ax.plot(x_smooth_global, y_smooth_global, color=smooth_color_global)
        # ax.plot(x_smooth_client, y_smooth_client, color=smooth_color_client)
        # ax.plot(x_smooth_ours, y_smooth_ours, color=smooth_color_ours)



        ax.set_xticks(np.arange(1, num_points + 1, 1))
        ax.set_xticklabels(np.arange(1, num_points + 1))

        
axs[0].set_xlabel(f'ACC')
axs[1].set_xlabel(f'NMI')

axs[2].set_xlabel(f'ARI')
axs[3].set_xlabel(f'F1')


      
fig.legend(
    labels=['OURS', 'FedGCN', 'Local'],
    loc='upper center',
    ncol=3,
    bbox_to_anchor=(0.5, 1.05),
    frameon=False
)# 调整布局
plt.tight_layout()

# 图例统一放在所有子图上方
# fig.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.05))  # 调整位置
plt.tight_layout(rect=[0, 0, 1, 0.95])  # 给图例留出空间# plt.savefig("./smo/CiteSeer.png", dpi=400)
# plt.savefig("./output/smo1.png", dpi=600)
plt.show()