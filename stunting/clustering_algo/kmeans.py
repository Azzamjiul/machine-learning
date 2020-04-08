#############################
# K-means Clustering        #
#############################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('stunting/hasil_preprocessing_1/data.csv')

def clustering(hehe):
    X_np_array = np.asarray(df.astype(float))
    kmeans = KMeans(n_clusters=2, max_iter=3000, n_init=1000 )
    kmeans.fit(X_np_array)
    stunting=[]
    notstunting=[]
    for i in range(len(X_np_array)):
        predict_me = np.array(X_np_array[i].astype(float))
        predict_me = predict_me.reshape(-1, len(predict_me))
        prediction = kmeans.predict(predict_me)
        if prediction == [0]:
            notstunting.append(i)
            # print("row"+str(i)+" : "+str(prediction))
        else:
            stunting.append(i)
    hehe = hehe + 1
    print('percobaan ke-%d' % hehe)
    print('stunting: %d' % len(stunting))
    print('not stunting: %d' % len(notstunting))

for i in range(3):
    clustering(i)