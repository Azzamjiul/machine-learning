import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
df = pd.read_csv(url)
print(df.head())
# print(df[df['Age'].isnull()].head())
df['Sex'] = df['Sex'].replace('male', np.nan)
print(df.head())