import pandas as pd

cluster = pd.read_csv('stunting/hasil_clustering/hasil.csv')
cluster_0 = cluster[cluster['0'] == 0]
cluster_1 = cluster[cluster['0'] == 1]
print(len(cluster_0))
print(len(cluster_1))