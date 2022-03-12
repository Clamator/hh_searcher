import pandas as pd
import dask
import csv

df2 = pd.Cov = pd.read_csv(r"printer.csv",names=['tui', 'price', 'dot', 'postcode', 'type', 'age', 'duration', 'paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist', 'ppd',  'rec_stat'], parse_dates=['dot'])

df2_gl = df2.select_dtypes(include=['object']).copy()

df2_gl = df2_gl[df2_gl.duplicated(['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first')]

df2_gl = df2_gl.drop_duplicates(subset=['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first', inplace=False).to_csv('./t2.csv')

#print(df2_gl.info(memory_usage='deep'))

#df2_obj = df2.select_dtypes(include=['object']).copy()
#df2_obj.describe()
