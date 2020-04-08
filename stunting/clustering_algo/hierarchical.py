import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('stunting/hasil_preprocessing_1/data.csv')
dendrogram = sch.dendrogram(sch.linkage(df, method  = "ward"))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()