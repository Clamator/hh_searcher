import pandas as pd
import csv

df2 = pd.Cov = pd.read_csv(r"printer.csv",names=['tui', 'price', 'dot', 'postcode', 'type', 'age', 'duration', 'paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist', 'ppd',  'rec_stat'], parse_dates=['dot'])
#print(df2.shape)
#print(df2.columns)
df2 = df2[df2.duplicated(['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first')]
print(df2)

#df2 = df2.drop_duplicates(subset=['paon', 'saon', 'street', 'loc', 'city',
#              'dist', 'main_dist'], keep='first', inplace=False).to_csv('./ttt.csv')
#print(df2)

print(df2.info(memory_usage='deep'))



import os
import time
import pandas as pd
import numpy as np
df2 = pd.Cov = pd.read_csv(r"printer.csv", names=['tui', 'price', 'dot', 'postcode', 'type', 'age', 'duration', 'paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist', 'ppd',  'rec_stat'], parse_dates=['dot'])

for col in df2.columns:
    num_unique_values = len(df2[col].unique())
    num_total_values = len(df2[col])
    if num_unique_values / num_total_values < 0.5:
        converted_df2.loc[:,col] = df2[col].astype('category')
    else:
        converted_df2.loc[:,col] = df2[col]
def mem_usage(pandas_obj):
    if isinstance(pandas_obj,pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else: # исходим из предположения о том, что если это не DataFrame, то это Series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2 # преобразуем байты в мегабайты
    return "{:03.2f} MB".format(usage_mb)
print (df2.info(memory_usage='deep'))
print('После оптимизации столбцов: '+mem_usage(converted_obj))

print('До оптимизации столбцов: '+mem_usage(df2))


df2_obj = df2.select_dtypes(include=['object']).copy()
df2_obj.describe()
