from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# 加载数据
data = load_iris()
x = data.data
y = data.target

# 创建PCA对象，n_components表示要保留的主要成分数量
pca = PCA(n_components=2)

# 对数据进行PCA降维
x_pca= pca.fit_transform(x)

# 画出降维后的数据
plt.figure(figsize=(8, 6))
plt.scatter()