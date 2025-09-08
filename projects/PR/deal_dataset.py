import pandas as pd

# 从文件中读取数据
data = pd.read_csv('./data/KDDTest+.csv', header=None)
data = data.drop(data.columns[-1], axis=1)

attack_types = data.iloc[:, -1]
attack_type_counts = attack_types.value_counts()
selected_attack_types = attack_type_counts[attack_type_counts >= 100].index.tolist()
filtered_data = data[data.iloc[:, -1].isin(selected_attack_types)]

attack_types = filtered_data.iloc[:, -1]
attack_type_counts = attack_types.value_counts()
print(attack_type_counts)


def map_to_numeric(column):
    unique_values = column.unique()
    mapping = {val: i for i, val in enumerate(unique_values)}
    return column.map(mapping)


# 对DataFrame的每一列应用映射函数
for col in data.columns[1:4]:  # 前三列
    filtered_data.loc[:, col] = map_to_numeric(filtered_data[col])

filtered_data.loc[:,  filtered_data.columns[-1]] = map_to_numeric(filtered_data[ data.columns[-1]])

# 定义归一化函数
# def normalize_column(column):
#     return (column - column.min()) / (column.max() - column.min())
#
# # 对每一列应用归一化函数
# normalized_data = filtered_data.apply(normalize_column)
print(filtered_data.head())

last_row = filtered_data.iloc[:,-1]

# 创建包含最后一行的 DataFrame
last_row_df = pd.DataFrame(last_row)

# 保存最后一行数据到文件




last_row_df.to_csv('nsl_label.txt', index=False,sep=' ', header=False)
filtered_data = filtered_data.iloc[:, :-1]

# 保存数据到文件
filtered_data.to_csv('nsl.txt', index=False,sep=' ', header=False)
print(filtered_data.head())
