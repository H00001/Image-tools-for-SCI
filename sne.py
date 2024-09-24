import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def t_sne(embeds, labels, sample_num, low):
    """
    Visualize embedding by t-SNE algorithm.
    :param embeds: Embedding of the data.
    :param labels: Labels.
    :param sample_num: The number of samples.
    :param show_fig: If True, show the figure.
    :return: fig: The figure.
    """
    cool_colors = ['#00B074', '#0A7783', '#A4D845' ,'#1D577B' ,"#EED63F", "#353F78"]
    #353F78
    #400048
    cool_cmap = plt.cm.colors.ListedColormap(cool_colors)

    # Sampling
    sample_index = np.random.randint(0, embeds.shape[0], sample_num)
    sample_embeds = embeds[sample_index]
    sample_labels = labels[sample_index]

    # t-SNE
    ts = TSNE(n_components= low, init='pca', random_state=1)
    ts_embeds = ts.fit_transform(sample_embeds)

    # Remove outliers
    mean, std = np.mean(ts_embeds, axis=0), np.std(ts_embeds, axis=0)
    inliers = (np.abs(ts_embeds - mean) < 3 * std).all(axis=1)
    ts_embeds = ts_embeds[inliers]
    sample_labels = sample_labels[inliers]

    # Normalization
    x_min, x_max = np.min(ts_embeds, axis=0), np.max(ts_embeds, axis=0)
    norm_ts_embeds = (ts_embeds - x_min) / (x_max - x_min)

    # Plot
    plt.rcParams["font.family"] = "Times New Roman"
    fig, ax = plt.subplots()
    scatter = ax.scatter(norm_ts_embeds[:, 0], norm_ts_embeds[:, 1], c=sample_labels, cmap=cool_cmap, s=10)
    # legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
    # ax.add_artist(legend1)
    plt.xticks([])
    plt.yticks([])
    #plt.title(title, fontsize=14)
    plt.axis('off')
    return fig

if __name__ == '__main__':
    # list = ["acm","dblp","reut","hhar","cite"]
    # for v in list:
    #     ori = f"origin_{v}"
    #     #ori = f"{v}"
    #     sv = t_sne(np.load(f"./sne/{v}.npy"),np.loadtxt(f"./sne/{v}_label.txt"),10300,f"{ori}")
    #     sv.savefig(f"sne/{ori}.png",dpi=600)
    
    
    # list = {"acm":(3025,2)} 
    # list = {"dblp": (4057,2)}
    # list = {"hhar":(10300,2)}
    # list = {"reut":(10000,2)}
    # # list = {"cite":(3327,2)}

    # ori = f"cite"
    # sv = t_sne(np.load(f"./sne/{ori}_h.npy"),np.loadtxt(f"./origin/{ori}_label.txt"),list[ori][0],list[ori][1])
    # sv.savefig(f"sne/{ori}_h.pdf", format='pdf', bbox_inches='tight', pad_inches=0.1)
    # sv.savefig(f"sne/{ori}_h.eps", format='eps', bbox_inches='tight', pad_inches=0.1)
    # sv.savefig(f"sne/{ori}_h.svg", format='svg', bbox_inches='tight', pad_inches=0.1)
    # sv.savefig(f"sne/{ori}_h.png",dpi=1200)
    

    # create origin image
    list = {"acm":(3025,2),"dblp":(4057,2),"hhar":(10300,3),"reut":(10000,3),"cite":(3227,2)}

    for v in list:
        ori = f"origin_{v}"
        # ori = f"{v}"
        sv = t_sne(np.loadtxt(f"./origin/{v}.txt"),np.loadtxt(f"./origin/{v}_label.txt"),list[v][0],list[v][1])
        # sv.savefig(f"sne/{ori}_o.pdf", format='pdf', bbox_inches='tight', pad_inches=0.1)
        # sv.savefig(f"sne/{ori}_o.eps", format='eps', bbox_inches='tight', pad_inches=0.1)
        # sv.savefig(f"sne/{ori}_o.svg", format='svg', bbox_inches='tight', pad_inches=0.1)

        sv.savefig(f"sne/{ori}_o.png",dpi=1200)