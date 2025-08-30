import torch
import matplotlib.pyplot as plt

import numpy as np
# 加载数据


# _type = "preds_client_"
# _type = "client_z_"
_type = "emb_client_"
z = torch.load(rf"E:\donwload\Image-tools-for-SCI-main\emb\{_type}3.pt", map_location=torch.device('cpu'))
L = np.loadtxt(rf"E:\donwload\Image-tools-for-SCI-main\emb\3.txt")

# 确保 z 形状正确
print("Tensor shape:", z.shape)
print(z)

if len(z.shape) != 2 or z.shape[1] != 3:
    print("z 的形状必须是 (n, 3)，但得到的是: {}".format(z.shape))
    z = z[:, :-1]

# 转换为 NumPy
x, y, z = z[:, 0].detach().numpy(), z[:, 1].detach().numpy(), z[:, 2].detach().numpy()

# 创建 3D 图
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(x, y, z, c=L, marker='o', alpha=1)

# 添加标签
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Scatter Plot of Tensor')

# 强制显示图像
plt.show(block=True)
# plt.savefig("0.svg")
