import pandas as pd
import numpy as np
import statistics 
from sklearn import preprocessing

# Read the data
X_full = pd.read_csv('stunting/data.csv', encoding = 'ISO-8859-1', low_memory=False, na_values=[np.nan, 'NONE', 9999, 9999, ' '])
# X_full = pd.read_csv('stunting/data.csv', encoding = 'ISO-8859-1', low_memory=False)

# To keep things simple, we'll use only numerical predictors
# X = X_full.select_dtypes(exclude=['object'])
X = X_full

############## 
# Preliminary investigation
##############
X_copy = X.copy()

#############################
# Preprocessing             #
#############################

# Drop columns with string values
cols_with_string = ['h519esp', 'h521esp', 'h522esp', 'h70506sp', 'h812esp', 'code_upm']
X_copy.drop(cols_with_string)

col_cardinal = [
    'h70101','h70102', 'h70103', 'h70104', 'h70105', 'h70106', 'h70107', 'h70108', 'h70109', 'h70110', 'h70111', 'h70112', 'h70113', 'h70114', 'h70115', 'h70116', 'h70117', 'h70201', 'h70202', 'h70203', 'h70204', 'h70205', 'h70206', 'h70207', 'h70301', 'h70302', 'h70303', 'h70304', 'h70305', 'h70306', 'h70307', 'h70308', 'h70309', 'h70310', 'h70311', 'h70401', 'h70402', 'h70403', 'h70404', 'h70405', 'h70406', 'h70501a', 'h70502a', 'h70503a', 'h70504a', 'h70505a', 'h70506a', 'h706', 'h707'
]

# print(len(col_cardinal))

col_cardinal_small = ['h101', 'h103', 'h205', 'h505', 'h506']

col_ordinal = list(set(X_copy.columns)-set(col_cardinal)-set(col_cardinal_small))

# 1. Mengganti spasi dengan null
# X_copy = X_copy.replace(' ', None)
# null_columns=X_copy.columns[X_copy.isnull().any()]
# print(X_copy[null_columns].isnull().sum())

# 2. Mengganti spasi dengan 0
# X_copy = X_copy.replace(' ', 0)
# X_copy = X_copy.astype(float)

# print(X_copy[col_cardinal].head(20))

# 3. pakai average
for column in col_cardinal:
# for column in X_copy.columns:
    try:
        X_copy_copy = X_copy[column]
        # X_copy_copy = X_copy_copy.replace(' ', 0)
        X_copy_copy = X_copy_copy.fillna(0)
        X_copy_copy = X_copy_copy.astype(int)
        average = round(X_copy_copy.mean(),0)
        # X_copy[column] = X_copy[column].replace(' ', average) 
        X_copy[column] = X_copy[column].fillna(average)
        X_copy[column] = X_copy[column].astype(int)
    except Exception as e:
        print(column)
        print(X_copy[column].head(20))
        # print(e)
        break

for column in col_cardinal_small:
    try:
        X_copy_copy = X_copy[column]
        # X_copy_copy = X_copy_copy.replace(' ', 0)
        X_copy_copy = X_copy_copy.fillna(0)
        X_copy_copy = X_copy_copy.astype(int)
        average = round(X_copy_copy.mean(),0)
        # X_copy[column] = X_copy[column].replace(' ', average) 
        X_copy[column] = X_copy[column].fillna(average) 
        X_copy[column] = X_copy[column].astype(int)
    except Exception as e:
        print(column)
        print(X_copy[column].head(20))
        # print(e)
        break


# print(X_copy['h807'].head(20))
# X_copy['h807'] = X_copy['h807'].replace(' ', X_copy['h807'].mode())
# print(X_copy['h807'].head(20))

# ordinal with average
# for column in col_ordinal:
#     try:
#         X_copy_copy = X_copy[column]
#         X_copy_copy = X_copy_copy.replace(' ', 0)
#         X_copy_copy = X_copy_copy.astype(int)
#         average = round(X_copy_copy.mean(),0)
#         X_copy[column] = X_copy[column].replace(' ', average) 
#         X_copy[column] = X_copy[column].astype(int)
#     except Exception as e:
#         print('GAGAL')
#         print(column)
#         print(X_copy[column].head(20))
#         # print(e)
#         break

# ordinal with median
# ordinal with mode
for column in col_ordinal:
    try:
        # print(X_copy[column].dtypes)
        X_copy_copy = X_copy[column]
        # X_copy_copy = X_copy_copy.fillna(0)
        # X_copy_copy.dropna()
        median = X_copy_copy.median()
         # print(median)
        # print('median {} = {}'.format(column,median))

        if column not in ['ï»¿folio']:
            X_copy_copy = X_copy_copy.dropna()
            mode = statistics.mode(X_copy_copy)
            print('modus {} = {}'.format(column,mode))
            # X_copy[column] = X_copy[column].fillna(mode)
       
        
        # median = X_copy[column].median()
        # print(column + ' => ' + median)
        X_copy[column] = X_copy[column].fillna(median)
        # X_copy[column] = X_copy[column].replace(' ', mode)
        X_copy[column] = X_copy[column].astype(int)
    except Exception as e:
        print('GAGAL')
        print(column)
        print(X_copy[column].head(20))
        print(e)
        break

##### Kategorisasi
for cardinal in col_cardinal:
    # print(X_copy[cardinal].head(20))
    # print(X_copy[cardinal].describe())
    # print('\n')
    c = pd.cut(
        X_copy[cardinal],
        bins=[-np.inf, 00, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, np.inf],
        labels=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    )
    # print(c.head(20).values)
    X_copy.drop(labels=cardinal, axis=1, inplace=True)
    X_copy[cardinal] = c.values
    # print('\n')
    # print(X_copy[cardinal].head(20))
    # print(X_copy[cardinal].describe())


##### Cek Tipe
# for column  in X_copy.columns:
#     try:
#         print(X_copy[column].dtypes)
#         X_copy[column].astype(float)
#         print('berhasil:')
#         print(column)
#         print(X_copy[column].dtypes)
#         print('\n')
#     except Exception as e:
#         print('GAGAL:')
#         print(column)
#         print(e)
#         print(X_copy[column].dtypes)
#         print('\n')
#         print(X_copy[column].head(20))
#         break

output = pd.DataFrame(X_copy)
output.to_csv('stunting/hasil_preprocessing/data_M4_kategorisasi.csv', index=False)