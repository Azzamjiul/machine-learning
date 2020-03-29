import pandas as pd
import numpy as np

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

col_cardinal = [
    'h70101','h70102', 'h70103', 'h70104', 'h70105', 'h70106', 'h70107', 'h70108', 'h70109', 'h70110', 'h70111', 'h70112', 'h70113', 'h70114', 'h70115', 'h70116', 'h70117', 'h70201', 'h70202', 'h70203', 'h70204', 'h70205', 'h70206', 'h70207', 'h70301', 'h70302', 'h70303', 'h70304', 'h70305', 'h70306', 'h70307', 'h70308', 'h70309', 'h70310', 'h70311', 'h70401', 'h70402', 'h70403', 'h70404', 'h70405', 'h70406', 'h70501a', 'h70502a', 'h70503a', 'h70504a', 'h70505a', 'h70506a', 'h706', 'h707'
]
X_copy = X_copy.astype(float)

for cardinal in col_cardinal:
    print(cardinal)
    print(X_copy[cardinal].head(20).values)
    c = pd.cut(
        X_copy[cardinal],
        bins=[-np.inf, 0, 200, 400, 600, 800, np.inf],
        labels=[0,1,2,3,4,5]
    )
    # print(c.head(20).values)
    X_copy.drop(labels=cardinal, axis=1, inplace=True)
    X_copy[cardinal] = c.values
    print(X_copy[cardinal].head(20).values)

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

clustering()