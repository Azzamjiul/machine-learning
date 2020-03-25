import pandas as pd

# Read the data
X_full = pd.read_csv('stunting/data_Hogar_hogar.csv', encoding = 'ISO-8859-1')

# To keep things simple, we'll use only numerical predictors
# X = X_full.select_dtypes(exclude=['object'])
X = X_full

############## 
# Preliminary investigation
##############

# Shape of data (num_rows, num_columns)
print(X.shape)

# Number of missing values in each column of training data
missing_val_count_by_column = (X == ' ').sum()
print(missing_val_count_by_column[missing_val_count_by_column > 0])

############## 
# Make ordinal number all
##############

##############
# Kmeans Clustering
##############
import numpy as np
from sklearn.cluster import KMeans
def clustering():
    X = np.asarray(X_full.astype(float))
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    stunting=[]
    notstunting=[]
    for i in range(len(X)):
        predict_me = np.array(X[i].astype(float))
        predict_me = predict_me.reshape(-1, len(predict_me))
        prediction = kmeans.predict(predict_me)
        if prediction == [0]:
            notstunting.append(i)
            # print("row"+str(i)+" : "+str(prediction))
        else:
            stunting.append(i)
    print(len(stunting))
    print(len(notstunting))

clustering()