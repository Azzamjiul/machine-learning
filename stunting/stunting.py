import pandas as pd

# Read the data
X_full = pd.read_csv('stunting/data_Hogar_hogar.csv', encoding = 'ISO-8859-1')

# To keep things simple, we'll use only numerical predictors
# X = X_full.select_dtypes(exclude=['object'])
X = X_full

############## 
# Preliminary investigation
##############
X_copy = X.copy()

# Get list of non-numerical variables
s = (X_copy.dtypes == 'object')
object_cols = list(s[s].index)
# print(object_cols)

#############################
# Preprocessing             #
#############################

# 1. Mengganti spasi dengan null
# X_copy = X_copy[object_cols].replace(' ', '')

# 2. Mengganti spasi dengan 0
X_copy = X_copy.replace(' ', 0)

# 3. pakai average

# Drop columns with string values
cols_with_string = ['h519esp', 'h521esp', 'h522esp', 'h70506sp', 'h812esp', 'code_upm']
X_copy.drop(cols_with_string, axis=1, inplace=True)

#############################
# Rubah Ordinal semuanya    #
#############################

# Check cardinality
from pandas import *

data = pd.read_csv('stunting/data_coba.csv', delimiter=';')
data = data[0:3]
idx = []

for i in range(147):
    idx.append(i)
    # print(i)

idx = Int64Index(idx)
data = data.transpose()
data.set_index(idx, inplace=True)
col_cardinal = []

for i in range(147):
    if(data[2][i] == 'kardinal'):
        col_cardinal.append(data[0][i])

print(col_cardinal)
# bad_label_cols = list(set(object_cols)-set(good_label_cols))
col_ordinal = list(set(X_copy.columns)-set(col_cardinal))
print(col_ordinal)

#############################
# K-means Clustering        #
#############################
from sklearn.cluster import KMeans
import numpy as np

def clustering():
    X_np_array = np.asarray(X_copy.astype(float))
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

# clustering()