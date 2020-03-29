from pandas import *
import pandas as pd

data = pd.read_csv('stunting/data_coba.csv', delimiter=';')
data = data[0:3]
idx = []

for i in range(147):
    idx.append(i)
    # print(i)

idx = Int64Index(idx)
data = data.transpose()
data.set_index(idx, inplace=True)
col_with_cardinal = []

for i in range(147):
    if(data[2][i] == 'kardinal'):
        col_with_cardinal.append(data[0][i])

print('\n\n')
print(col_with_cardinal)
# print(set(col_with_cardinal))