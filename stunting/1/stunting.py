import pandas as pd

data = pd.read_csv('stunting/data_Hogar_hogar.csv', encoding = 'ISO-8859-1', low_memory=False)
missing_values = data.isin([' ']).sum()
missing_values = data.isnull().sum()
for value in missing_values:
    print(value)