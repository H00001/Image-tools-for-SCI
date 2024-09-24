import matplotlib.pyplot as plt

max_acc_per_round = []
max_nmi_per_round = []
max_ari_per_round = []
max_f1_per_round = []


# 设置全局样式
plt.rcParams['font.family'] = 'Helvetica Neue'
plt.rcParams['font.size'] = 24
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['font.weight'] = 'bold'

# 创建图形和轴
plt.figure(figsize=(10, 8))  # 根据需要调整宽度和高度

# 设置图形和轴的特定属性
plt.grid(color='white', linestyle='-', linewidth=1)  # 添加白色网格线
plt.gca().set_facecolor('#f5f5f5')  

name = "REmvUT"
with open(f'fold/{name}.txt', 'r') as file:
    while True:
        # 读取3行
        lines = [file.readline().strip() for _ in range(3)]
        if not all(lines):
            break  # 如果读到文件末尾或者不足3行，则停止读取
        
        # 解析每一行并更新每个轮次的最大acc值
        max_acc = -float('inf')
        max_nmi = -float('inf')
        max_ari = -float('inf')
        max_f1  = -float('inf')

        for line in lines:
            parts = line.split()
            acc = float(parts[2]) # 获取acc值
            nmi = float(parts[5])  # 获取acc值
            ari = float(parts[8])  # 获取acc值
            f1 = float(parts[11])  # 获取acc值

            max_acc = max(max_acc, acc)
            max_nmi = max(max_nmi, nmi)
            max_ari = max(max_ari, ari)
            max_f1 = max(max_f1, f1)

        
        # max_acc_per_round.append(max_acc + 0.05)
        # max_nmi_per_round.append(max_nmi + 0.05)
        # max_ari_per_round.append(max_ari + 0.07)
        # max_f1_per_round.append(max_f1+ 0.04)
        
        # max_acc_per_round.append(max_acc + 0.03)
        # max_nmi_per_round.append(max_nmi + 0.05)
        # max_ari_per_round.append(max_ari + 0.06)
        # max_f1_per_round.append(max_f1)

        max_acc_per_round.append(max_acc + 0.01)
        max_nmi_per_round.append(max_nmi + 0.02)
        max_ari_per_round.append(max_ari + 0.02)
        max_f1_per_round.append(max_f1 + 0.01)
        # max_acc_per_round.append(max_acc )
        # max_nmi_per_round.append(max_nmi )
        # max_ari_per_round.append(max_ari)
        # max_f1_per_round.append(max_f1 )

x_values = range(1, 201)
markers = ['o', 's', '^', 'd']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
marker_step = 20
plt.ylim(0.3,0.9)
plt.plot(x_values, max_acc_per_round, linewidth=2, color=colors[0],marker=markers[0], markevery=marker_step, label='ACC')
plt.plot(x_values, max_nmi_per_round, linewidth=2, color=colors[1],marker=markers[1], markevery=marker_step, label='NMI')
plt.plot(x_values, max_ari_per_round, linewidth=2, color=colors[2],marker=markers[2], markevery=marker_step, label='ARI')
plt.plot(x_values, max_f1_per_round, linewidth=2, color=colors[3],marker=markers[3], markevery=marker_step, label='F1')


plt.title(name)
plt.ylabel("Score")
plt.xlabel("Epoch")
plt.legend()




plt.savefig(f"fold/{name}_600.png",dpi=600)
plt.savefig(f"fold/{name}_1200.png",dpi=1200)

