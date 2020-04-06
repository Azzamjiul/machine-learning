#############################
# K-means Clustering        #
#############################
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

df = pd.read_csv('stunting/hasil_preprocessing/data_M3_kategorisasi.csv')

# df['h103'].replace(' ',0)
# for v in df['h103']:
#     print(v)

# for col in df.columns: 
    # print('%s => %s' % (col, df[col].dtypes))
    # print(df[col].dtypes) 

def clustering(hehe):
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
    hehe = hehe + 1
    print('percobaan ke-%d' % hehe)
    print('stunting: %d' % len(stunting))
    print('not stunting: %d' % len(notstunting))

for i in range(3):
    clustering(i)