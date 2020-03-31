import pandas as pd
df = pd.read_csv('stunting/ENSANUT_average_all.csv')
#############################
# K-means Clustering        #
#############################
from sklearn.cluster import KMeans
import numpy as np

def clustering():
    X_np_array = np.asarray(df.astype(float))
    kmeans = KMeans(n_clusters=2)
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

    print('stunting: %d' % len(stunting))
    print('not stunting: %d' % len(notstunting))

clustering()