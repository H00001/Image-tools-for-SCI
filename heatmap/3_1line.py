import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 准备数据：三个 5×5 矩阵，值在 0.9–1.0 之间
data_list = [np.random.uniform(68, 94, (5, 5)) for _ in range(3)]
sns.set(style='white')  
conditions = ["3 datasets in SD", "4 datasets in SD", "3 datasets in CD"]  # 对应每张热力图的现有条件

fig, axes = plt.subplots(1, 3, figsize=(15, 5), gridspec_kw={'wspace':0.05})

for ax, data, cond in zip(axes, data_list, conditions):
    sns.heatmap(
        data,
        ax=ax,
        cmap=sns.light_palette("#0378C2", as_cmap=True),  # 浅天蓝渐变
        vmin=50, vmax=94,
        annot=True,
        fmt=".2f",
        # annot_kws={"color": "white", "fontsize": 12},
        linewidths=0.5,
        linecolor='white',
        annot_kws={"fontsize": 17, "color": "white"},
        cbar=False,
        xticklabels=False,  # 移除列标签
        yticklabels=False   # 移除行标签 :contentReference[oaicite:0]{index=0}

    )
    ax.set_title(cond, fontsize=24, fontweight="bold", pad=12)

    ax.tick_params(left=False, bottom=False)  # 不显示刻度线 :contentReference[oaicite:1]{index=1}

# plt.show()
plt.tight_layout()
plt.savefig("./output/inference.png", dpi = 600)
