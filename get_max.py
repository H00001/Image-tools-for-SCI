def get_value(file_path):
    accs, nmis, aris, f1s = [],[],[],[]
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Split the line and extract values
            values = line.split(',')
            accs.append(float(values[0].split()[1].strip()))
            nmis.append(float(values[1].split()[1].strip()))
            aris.append(float(values[2].split()[1].strip()))
            f1s.append(float(values[3].split()[1].strip()))
    return accs, nmis, aris, f1s

get_final_metrics = lambda file_path: [metrics[-1] for metrics in get_value(file_path)]

get_max_metrics = lambda file_path: [max(metrics) for metrics in get_value(file_path)]
