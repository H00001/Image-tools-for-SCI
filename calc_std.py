import os
import numpy as np
from get_max import get_final_metrics

def process_files(folder_path):
    accs = []
    nmis = []
    aris = []
    f1s = []
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".out"):  # Assuming your files have a .txt extension
            file_path = os.path.join(folder_path, filename)

            # Get max metrics for the current file
            max_acc, max_nmi, max_ari, max_f1 = get_final_metrics(file_path)
            #print(f"{filename}\t{max_acc}\t{max_ari}\t{max_nmi}\t{max_f1}")
            accs.append(max_acc)
            aris.append(max_ari)
            nmis.append(max_nmi)
            f1s.append(max_f1)

    return accs,nmis,aris,f1s

# Replace 'your_folder_path' with the actual path to your folder containing the files
li = ['acm','reut','usps','hhar','cite']
for i in li:
    folder_path = f'./data/{i}'
    accs,nmis,aris,f1s = process_files(folder_path)
    print(f"data_{i} = np.array([")

    print(nmis,",")
    print(aris,",")
    print(f1s,",")
    # 
    print(accs,",")
    print("])")


acc_mean_value = np.mean(accs)
acc_variance_value = np.std(accs)
ari_mean_value = np.mean(aris)
ari_variance_value = np.std(aris)
nmi_mean_value = np.mean(nmis)
nmi_variance_value = np.std(nmis)
f1_mean_value = np.mean(f1s)
f1_variance_value = np.std(f1s)

print("acc: %.4f + %.4f" % (acc_mean_value, acc_variance_value))
print("ari: %.4f + %.4f" % (ari_mean_value, ari_variance_value))
print("nmi: %.4f + %.4f" % (nmi_mean_value, nmi_variance_value))
print("f1: %.4f + %.4f" % (f1_mean_value,f1_variance_value))
#
