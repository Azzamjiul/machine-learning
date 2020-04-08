import numpy as np
import pandas as pd
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt

df = pd.read_csv('stunting/hasil_preprocessing_1/data.csv')
X_np_array = np.asarray(df.astype(float))

ms = ['Cao', 'Huang']

for  m in  ms:
    kmode = KModes(n_clusters=2, init =  m, n_init = 1, verbose=1)
    fitClusters_cao = kmode.fit_predict(X_np_array)
    cluster = pd.DataFrame(fitClusters_cao)
    stunting = cluster.sum()
    not_stunting = cluster.count() - stunting
    print("Kmodes {} \nStunting = {}\nNot Stunting = {}".format( m, stunting, not_stunting))

