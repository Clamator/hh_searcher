import pandas as pd
import dask.dataframe as dd
filename = 'printer2.csv'

df = dd.read_table(filename)
#df.to_parquet('printer2_parc')
df2 = dd.read_parquet('printer2_parc/part.*.parquet', columns=['a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p'])
print(df2['b'].mean().compute())


#print(df['b'].mean().compute())

