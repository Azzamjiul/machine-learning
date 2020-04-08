import pandas as pd

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, names=['sepal length', 'sepal width', 'petal length', 'petal width', 'target'])

# PCA is effected by scale -> scale the features before applying PCA
from sklearn.preprocessing import StandardScaler

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:,features].values
y = df.loc[:,['target']].values
standarized_x = StandardScaler().fit_transform(x)

# PCA projection to 2D
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
components = pca.fit_transform(standarized_x)
principalDf = pd.DataFrame(data=components, columns=['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['target']]], axis=1)

#visualize 2D
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal 1', fontsize=15)
ax.set_ylabel('Principal 2', fontsize=15)
ax.set_title('2 components PCA', fontsize=20)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r','g','b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(
        finalDf.loc[indicesToKeep, 'principal component 1'],
        finalDf.loc[indicesToKeep, 'principal component 2'],
        c = color,
        s = 50
    )
ax.legend(targets)
ax.grid()
plt.show()