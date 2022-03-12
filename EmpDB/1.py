import pandas as pd
import dask
import csv

df2 = pd.Cov = pd.read_csv(r"printer.csv",names=['tui', 'price', 'dot', 'postcode', 'type', 'age', 'duration', 'paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist', 'ppd',  'rec_stat'], parse_dates=['dot'])

df2 = df2[df2.duplicated(['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first')]

df2 = df2.drop_duplicates(subset=['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first', inplace=False).to_csv('./tt.csv')

#print(df2.info(memory_usage='deep'))

#df2_obj = df2.select_dtypes(include=['object']).copy()
#df2_obj.describe()
