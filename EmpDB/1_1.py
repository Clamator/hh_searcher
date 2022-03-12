import pandas as pd
import dask.dataframe as dd
filename = 'printer2.csv'

df = dd.read_csv(filename)

df2 = df[['h', 'k']].drop_duplicates().compute() # unique


#df.to_parquet('printer2_parc')
#df2 = dd.read_parquet('printer2_parc/part.*.parquet', columns=['a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p'])
#print(df2['b'].mean().compute())

#print(df.mean(2).compute())
#print(df)
#print(df['b'].mean().compute())
#['h', 'i','j','k', 'l', 'm', 'n']


import dask.dataframe as dd
import dask


df = pd.DataFrame({"temp1":[1,2,2,4],"temp2":[1,2,3,4]})
ddf = dd.from_pandas(df,npartitions=2)
for unique_value in [ddf.temp1.unique(), df.temp2.unique()]:
    print(unique_value)

print(df)