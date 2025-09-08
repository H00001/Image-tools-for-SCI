import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 将数据存储在字典中，包含 global 和 client 数据
#CiteSeer

comress_rate = 0.6
data = {
    'acc': {
        7: {'OURS': (np.array([1, 2, 3, 4, 5,6,7]), np.array([0.8020, 0.7950, 0.6165, 0.7052, 0.7282,0.9411, 0.6882])*100),
            'FedGCN': (np.array([1, 2, 3, 4, 5,6,7]), np.array([0.54, 0.6411, 0.5020, 0.6511, 0.6593, 0.9291, 0.5443])*100),
            'Local': (np.array([1, 2, 3, 4, 5,6,7]), np.array([0.6738, 0.5271, 0.5182, 0.503, 0.564, 0.7704, 0.6035])*100)
            },
        9: {'OURS': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([0.8020, 0.7450, 0.6165, 0.7252, 0.7482,0.9411, 0.7011, 0.7083, 0.7262])*100),
             'FedGCN': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([0.52, 0.6267, 0.5479, 0.6689, 0.6382, 0.9291, 0.6445, 0.6672, 0.5821])*100),
             'Local': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([0.6738, 0.5271, 0.5182, 0.503, 0.564, 0.5238, 0.6035, 0.6435, 0.6397])*100)},
        10: {'OURS': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                        np.array([0.7920, 0.7950, 0.6165, 0.6952, 0.7582,0.9311, 0.742, 0.6715, 0.7284, 0.6755])*100),
            'FedGCN': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                        np.array([0.55, 0.5819, 0.5216, 0.6493, 0.6168, 0.9285, 0.6245, 0.5815, 0.6, 0.6286])*100),
             'Local': (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                        np.array([0.6738, 0.5271, 0.5182, 0.503, 0.564, 0.7704, 0.5238, 0.6138, 0.5819, 0.5524])*100)
                        },
    },
}

data1 = {
    'acc': {
        2: {'OURS': (np.array([1, 2, 3]), np.array([0.8020, 0.7950, 0.6])),
            'FedGCN': (np.array([1, 2,3]), np.array([0.54, 0.6411, 0.4])),
            'Local': (np.array([1, 2,3]), np.array([0.55, 0.51,0.2]))
            },
        }
}





# 设置全局字体为微雅软黑
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False  # 保证负号正常显示
plt.rcParams['font.weight'] = 'bold'  # 设置全局字体加粗
# 单独设置一些元素的字体大小（可选）
plt.rcParams['axes.titlesize'] = 18  # 设置标题字体大小
plt.rcParams['axes.labelsize'] = 16  # 设置坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = 16  # 设置x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 16  # 设置y轴刻度字体大小
plt.rcParams['legend.fontsize'] = 16  # 设置图例字体大小

# 设置标题加粗
plt.rcParams['axes.titleweight'] = 'bold'  # 设置标题字体加粗

# 平滑曲线函数
def smooth_curve(x, y, k=3):
    spl = make_interp_spline(x, y, k=k)  # k=3表示三次样条插值
    x_new = np.linspace(x.min(), x.max(), 500)  # 生成更多的点来平滑曲线
    y_new = spl(x_new)
    return x_new, y_new


# 选择要绘制的指标
data_names = ['acc']

# 创建图形，设置为 3 行 4 列
fig, axs = plt.subplots(1, 3, figsize=(10, 3))

# 为每个指标和每组数据绘制图形
for i, data_name in enumerate(data_names):
    for j, num_points in enumerate([7,9,10]):
        # 获取 global 和 client 数据
        x_ours, y_ours = data[data_name][num_points]['OURS']
        x_global, y_global = data[data_name][num_points]['FedGCN']
        x_client, y_client = data[data_name][num_points]['Local']

        # 计算平滑曲线
        x_smooth_global, y_smooth_global = smooth_curve(x_global * comress_rate, y_global)
        x_smooth_client, y_smooth_client = smooth_curve(x_client * comress_rate, y_client)
        x_smooth_ours, y_smooth_ours = smooth_curve(x_ours * comress_rate, y_ours)


        # 选择不同的颜色
        color_global = '#E5637B'
        color_client = '#5979A2'
        color_ours = '#008687'
        smooth_color_global = '#E5637B'
        smooth_color_client = '#5979A2'
        smooth_color_ours = '#008687'


        # if j == 2:
        #     ax = axs[1][0]
        # else:
        ax = axs[j]  # 交换行列的索引

        ax.bar(x_global* comress_rate, y_global, width=0.35, color=color_global, alpha=0.7, label='FedNCN', zorder=2)
        ax.bar(x_client* comress_rate, y_client, width=0.35, color=color_client, alpha=0.6, label='Local', zorder=3)
        ax.bar(x_ours* comress_rate, y_ours, width=0.35, color=color_ours, alpha=0.5, label='OURS', zorder=1)


        ax.plot(x_smooth_global, y_smooth_global, color=smooth_color_global)
        ax.plot(x_smooth_client, y_smooth_client, color=smooth_color_client)
        ax.plot(x_smooth_ours, y_smooth_ours, color=smooth_color_ours)



        ax.set_xticks(np.arange(1, num_points + 1, 1)*comress_rate)
        ax.set_xticklabels(np.arange(1, num_points + 1))

        ax.set_ylim(20,101)

        ax.spines['right'].set_visible(False)  # 移除右侧边框线
        ax.spines['top'].set_visible(False)   # 移除上侧边框线













# x_ours, y_ours = data1['acc'][2]['OURS']
# x_global, y_global = data1['acc'][2]['FedGCN']
# x_client, y_client = data1['acc'][2]['Local']
# x_client = x_client - 0.2
# x_ours = x_ours + 0.2

#         # 计算平滑曲线
# x_smooth_global, y_smooth_global = smooth_curve(x_global, y_global,k=1)
# x_smooth_client, y_smooth_client = smooth_curve(x_client, y_client,k=1)
# x_smooth_ours, y_smooth_ours = smooth_curve(x_ours, y_ours,k=1)


# ax = axs[1][1]

# ax.bar(x_global, y_global, width=0.25, color=color_global, alpha=0.7, label='FedNCN', zorder=2)
# ax.bar(x_client, y_client, width=0.25, color=color_client, alpha=0.6, label='Local', zorder=3)
# ax.bar(x_ours, y_ours, width=0.25, color=color_ours, alpha=0.5, label='OURS', zorder=1)


# ax.plot(x_smooth_global, y_smooth_global, color=smooth_color_global)
# ax.plot(x_smooth_client, y_smooth_client, color=smooth_color_client)
# ax.plot(x_smooth_ours, y_smooth_ours, color=smooth_color_ours)


# ax.set_xticks(np.arange(1, 3 + 1, 1))
# ax.set_xticklabels(np.arange(1, 3 + 1))

# ax.set_ylim(0.2,1.05)

axs[0].set_ylabel("ACC(%)",  labelpad=-1, fontsize=18)

axs[0].set_xlabel(f'Client ID')
axs[1].set_xlabel(f'Client ID')

axs[2].set_xlabel(f'Client ID')
# axs[2].xaxis.set_label_coords(1.05, -0.1)  # 将标签向右移动

axs[0].annotate(
    'SM',  # 标签文本
    xy=(0.10, 0.95),  # 标签位置，(x, y) 相对于坐标轴的位置
    xycoords='axes fraction',  # 坐标系：相对于坐标轴的百分比位置
    fontsize=16,  # 字体大小
    rotation=-0,  # 旋转角度
    ha='center',  # 水平对齐：居中
    va='center',  # 垂直对齐：居中
        bbox=dict(  # 添加半透明背景框（可选）
        facecolor='#dce7f1', 
        alpha=0.7, 
        edgecolor='none',
        boxstyle='round,pad=0.2'
    )
)
axs[1].annotate(
    'SM-BIO',  # 标签文本
    xy=(0.2, 0.95),  # 标签位置，(x, y) 相对于坐标轴的位置
    xycoords='axes fraction',  # 坐标系：相对于坐标轴的百分比位置
    fontsize=16,  # 字体大小
    rotation=-0,  # 旋转角度
    ha='center',  # 水平对齐：居中
    va='center',  # 垂直对齐：居中
        bbox=dict(  # 添加半透明背景框（可选）
        facecolor='#dce7f1', 
        alpha=0.7, 
        edgecolor='none',
        boxstyle='round,pad=0.2'
    )
)
axs[2].annotate(
    'SM-BIO-SY',  # 标签文本
    xy=(0.27, 0.95),  # 标签位置，(x, y) 相对于坐标轴的位置
    xycoords='axes fraction',  # 坐标系：相对于坐标轴的百分比位置
    fontsize=16,  # 字体大小
    rotation=-0,  # 旋转角度
    ha='center',  # 水平对齐：居中
    va='center',  # 垂直对齐：居中
        bbox=dict(  # 添加半透明背景框（可选）
        facecolor='#dce7f1', 
        alpha=0.7, 
        edgecolor='none',
        boxstyle='round,pad=0.2'
    )
)

# axs[1][1].set_xlabel(f'{data_name.upper()} (SN)')

      
fig.legend(
    labels=['FedGCN','Local', 'OURS'],
    loc='upper center',
    ncol=3,
    bbox_to_anchor=(0.5, 1.05),
    frameon=False
)# 调整布局
# plt.tight_layout()




# 图例统一放在所有子图上方
# fig.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.05))  # 调整位置
plt.tight_layout(rect=[0, 0, 1, 0.95])  # 给图例留出空间# plt.savefig("./smo/CiteSeer.png", dpi=400)
plt.subplots_adjust(wspace=0.161)

plt.savefig("./projects/dream1/output/client-wise.png", dpi=600)
plt.show()