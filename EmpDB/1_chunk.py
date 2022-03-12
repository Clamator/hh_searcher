import pandas as pd

result = None
df2 = pd.Cov = pd.read_csv(r"pp-complete.csv",names=['tui', 'price', 'dot', 'postcode', 'type', 'age', 'duration', 'paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist', 'ppd',  'rec_stat'], parse_dates=['dot'], chunksize=1000000)
for chunk in df2:
    voters_street = chunk[['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist']]
    #chunk_result = voters_street.value_counts()
    if result is None:
        result = voters_street
    else:
        result = result.add(voters_street, fill_value=0)

#result.sort_values(ascending=False, inplace=True)
result_gl = result.select_dtypes(include=['object']).copy()

result_gl = result_gl[result_gl.duplicated(['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first')]

result_gl = result_gl.drop_duplicates(subset=['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first', inplace=False).to_csv('./t2.csv')