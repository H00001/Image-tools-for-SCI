from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# 加载鸢尾花数据集
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 重命名列以包含单位
iris_df.columns = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)", "species"]

# 显示数据集的前几行
print(iris_df.head())


sns.set(style="whitegrid")

# 创建一个大的画布来容纳所有子图
fig, axs = plt.subplots(2, 2, figsize=(15, 15))

# Histogram: Distribution of Sepal Length
axs[0, 0].hist(iris_df["sepal length (cm)"], bins=15, edgecolor="k", alpha=0.7)
axs[0, 0].set_title("Distribution of Sepal Length")
axs[0, 0].set_xlabel("Sepal Length (cm)")
axs[0, 0].set_ylabel("Frequency")

# Boxplot: Comparison of Petal Width for Different Iris Species
sns.boxplot(data=iris_df, x="species", y="petal width (cm)", ax=axs[0, 1])
axs[0, 1].set_title("Comparison of Petal Width for Different Iris Species")
axs[0, 1].set_xlabel("Species")
axs[0, 1].set_ylabel("Petal Width (cm)")

# Scatterplot: Relationship between Petal Length and Petal Width
sns.scatterplot(data=iris_df, x="petal length (cm)", y="petal width (cm)", hue="species", palette="viridis", ax=axs[1, 0])
axs[1, 0].set_title("Relationship between Petal Length and Petal Width")
axs[1, 0].set_xlabel("Petal Length (cm)")
axs[1, 0].set_ylabel("Petal Width (cm)")
axs[1, 0].legend(title="Species")

# Violin Plot: Distribution of Petal Length for Different Iris Species
sns.violinplot(data=iris_df, x="species", y="petal length (cm)", ax=axs[1, 1])
axs[1, 1].set_title("Distribution of Petal Length for Different Iris Species")
axs[1, 1].set_xlabel("Species")
axs[1, 1].set_ylabel("Petal Length (cm)")

# plt.tight_layout()

plt.show()


X = iris.data
y = iris.target

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the feature data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Initialize the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)



# Initialize a list to store the K-NN classifiers for different values of K
knn_classifiers = []

# Train K-NN classifiers for K values from 1 to the number of class labels
for k in range(1, len(np.unique(y)) + 1):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    knn_classifiers.append(knn_classifier)

dt_classifier = DecisionTreeClassifier(random_state=42)

# Train the classifier
dt_classifier.fit(X_train, y_train)

from sklearn.svm import SVC

# Initialize the SVM classifier
svm_classifier = SVC(kernel='linear', random_state=42)

# Train the classifier
svm_classifier.fit(X_train, y_train)


from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Function to evaluate a classifier
def evaluate_classifier(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    return accuracy, report, conf_matrix


# Evaluate each classifier and store the results
results = {}
results['Decision Tree'] = evaluate_classifier(dt_classifier, X_test, y_test)
results['Random Forest'] = evaluate_classifier(rf_classifier, X_test, y_test)
# Evaluate K-NN classifiers and store the best result
knn_results = [evaluate_classifier(knn, X_test, y_test) for knn in knn_classifiers]
best_knn_result = max(knn_results, key=lambda x: x[0])
results['K-NN (Best K)'] = best_knn_result
results['SVM'] = evaluate_classifier(svm_classifier, X_test, y_test)

# Now we can create tables and charts to display the results
for method, (accuracy, report, conf_matrix) in results.items():
    print(f"Results for {method}:")
    print(f"Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(report)
    print("Confusion Matrix:")
    print(conf_matrix)
    print("\n")

X_iris = iris.data
y_iris = iris.target

# 步骤2: 选择特征（这里我们使用前两个特征进行示例）
X_iris_reduced = X_iris[:, :2]

# 步骤3: 应用 K-Means 聚类算法
# 假设我们想要将数据点分为3个簇
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_iris_reduced)

# 获取聚类结果
labels = kmeans.labels_

from sklearn.metrics import silhouette_score, davies_bouldin_score, adjusted_rand_score, normalized_mutual_info_score


# 计算轮廓系数
silhouette_avg = silhouette_score(X_iris, labels)
print(f"Silhouette Coefficient: {silhouette_avg:.3f}")

# 计算Davies-Bouldin指数
db_index = davies_bouldin_score(X_iris, labels)
print(f"Davies-Bouldin Index: {db_index:.3f}")

# 如果有真实标签，计算调整兰德指数和归一化互信息
ari = adjusted_rand_score(y_iris, labels)
print(f"Adjusted Rand Index: {ari:.3f}")

nmi = normalized_mutual_info_score(y_iris, labels)
print(f"Normalized Mutual Information: {nmi:.3f}")

# 步骤4: 可视化聚类结果
plt.scatter(X_iris_reduced[:, 0], X_iris_reduced[:, 1], c=labels)
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.title('K-Means Clustering on Iris Dataset')
plt.show()
