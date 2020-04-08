import pandas as pd
import numpy as np
import statistics
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('stunting/data.csv', encoding = 'ISO-8859-1', low_memory=False, na_values=[np.nan, 'NONE', ' ', '99', '9999', '99999', '999999' ])
cols_with_string = ['ï»¿folio', 'deciles', 'quintiles', 'h519esp', 'h521esp', 'h522esp', 'h70506sp', 'h812esp', 'code_upm', 'est_dis', 'est_urb','est_marg','pondeh','est_var']
df = df.drop(cols_with_string, axis=1)

col_cardinal = ['h70101','h70102', 'h70103', 'h70104', 'h70105', 'h70106', 'h70107', 'h70108', 'h70109', 'h70110', 'h70111', 'h70112', 'h70113', 'h70114', 'h70115', 'h70116', 'h70117', 'h70201', 'h70202', 'h70203', 'h70204', 'h70205', 'h70206', 'h70207', 'h70301', 'h70302', 'h70303', 'h70304', 'h70305', 'h70306', 'h70307', 'h70308', 'h70309', 'h70310', 'h70311', 'h70401', 'h70402', 'h70403', 'h70404', 'h70405', 'h70406', 'h70501a', 'h70502a', 'h70503a', 'h70504a', 'h70505a', 'h70506a', 'h706', 'h707']
col_cardinal_small = ['h101', 'h103', 'h205', 'h505', 'h506']
col_ordinal = list(set(df.columns)-set(col_cardinal)-set(col_cardinal_small))

null_column = [] # kolom yang missing value > 45%
for column in df.columns:
    percent = df[column].isnull().sum()/len(df[column])*100
    percent = round(percent,2)
    if percent > 45 :
        null_column.append(column)
    # print('{} -> {}%'.format(column,percent))

# drop kolom yang missing value lebih dari 45%
df = df.drop(null_column, axis=1)

col_cardinal = list(set(col_cardinal)-set(null_column))
col_cardinal_small = list(set(col_cardinal_small)-set(null_column))
col_ordinal = list(set(col_ordinal)-set(null_column))

# Replace ordinal missing value with average
for column in col_cardinal:
    df[column].fillna(int(round(df[column].mean(),0)), inplace=True)
for column in col_cardinal_small:
    df[column].fillna(int(round(df[column].mean(),0)), inplace=True)

# Replace ordinal missing value with mode
for column in col_ordinal:
    df[column].fillna(int(statistics.mode(df[column])), inplace=True)

#Kategorisasi
for column in col_cardinal_small:
    c = pd.cut(
        df[column],
        bins    =   [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,30,35,40,45,50,60,70,80],
        labels  =   [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    )
    df[column] = c.values
for column in col_cardinal:
    c = pd.cut(
        df[column],
        bins=[-np.inf, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, np.inf],
        labels=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    )
    df[column] = c.values

# output = pd.DataFrame(df)
# output.to_csv('stunting/hasil_preprocessing_1/data.csv', index=False)
