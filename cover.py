from get_max import get_value
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


file = "res/acm seed=10.txt"
accs, nmis, aris, f1s = get_value(file)


indices = list(range(0, 201))
plt.ylim(0.65,0.95)
plt.plot(indices, accs[0:], label='ACC')
plt.plot(indices, nmis[0:], label='NMI')
plt.plot(indices, aris[0:], label='ARI')
# plt.plot(indices, f1s[0:], label='F1')

plt.xticks(fontname='Times New Roman', fontsize=10)
plt.yticks(fontname='Times New Roman', fontsize=10)

# Adding labels and title
plt.xlabel('Epochs', fontname='Times New Roman', fontweight='bold',color="")
plt.ylabel('Scores', fontname='Times New Roman', fontweight='bold')
plt.title('ACM', fontname='Times New Roman', fontweight='bold')
font = FontProperties(family='Times New Roman', style='normal', size=12)
plt.legend(prop=font)
plt.grid(True)


# Display the plot
plt.show(dpi=600)

