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

# print(X_copy.columns)
# print('hehe')
col_ordinal = list(set(X_copy.columns)-set(col_cardinal))
# print(col_ordinal)

#############################
# Kategorisasi Kardinal     #
#############################
import numpy as np
# print(X_copy['h101'].describe())
X_copy = X_copy.astype('int64')
X_coba = X_copy[col_cardinal]
print(X_coba.shape)

c = pd.cut(
    X_coba.stack(),
    # X_copy['h70101'],
    bins=[-np.inf, 0, 200, 400, 600, 800, np.inf],
    labels=[0,1,2,3,4,5]
)
print(c)
X_coba.join(c.unstack().add_suffix('_cat'))
print(X_coba.shape)

wkwk = [
    'h70101','h70102', 'h70103', 'h70104', 'h70105', 'h70106', 'h70107', 'h70108', 'h70109', 'h70110', 'h70111', 'h70112', 'h70113', 'h70114', 'h70115', 'h70116', 'h70117', 'h70201', 'h70202', 'h70203', 'h70204', 'h70205', 'h70206', 'h70207', 'h70301', 'h70302', 'h70303', 'h70304', 'h70305', 'h70306', 'h70307', 'h70308', 'h70309', 'h70310', 'h70311', 'h70401', 'h70402', 'h70403', 'h70404', 'h70405', 'h70406', 'h70501a', 'h70502a', 'h70503a', 'h70504a', 'h70505a', 'h70506a', 'h706', 'h707'
]

print(X_copy.dtypes)
print('\n\n\n\n\n')
X_copy = X_copy.astype('int64')
print(X_copy.dtypes)

X_coba = X_copy[
            ['h70101','h70102', 'h70103', 'h70104', 'h70105', 'h70106', 'h70107', 'h70108', 'h70109', 'h70110', 'h70111', 'h70112', 'h70113', 'h70114', 'h70115', 'h70116','h70117', 'h70201', 'h70202', 'h70203', 'h70204', 'h70205', 'h70206', 'h70207', 'h70301', 'h70302', 'h70303', 'h70304', 'h70305', 'h70306', 'h70307', 'h70308', 'h70309', 'h70310', 'h70311', 'h70401', 'h70402', 'h70403', 'h70404', 'h70405', 'h70406',]
        ]