import pandas as pd

frames = []
df2 = pd.Cov = pd.read_csv(r"pp-complete.csv",names=['tui', 'price', 'dot', 'postcode', 'type', 'age', 'duration', 'paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist', 'ppd',  'rec_stat'], parse_dates=['dot'], chunksize=1000000)
for chunk in df2:
    address = chunk[['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist']]
    #chunk_result = voters_street.value_counts()

    frames.append(pd.DataFrame(address))
    #else:
    #    result = pd.merge(result, pd.DataFrame(address), on=['paon', 'saon', 'street', 'loc', 'city',
    #          'dist', 'main_dist'], how='inner')
keys = [str(x) for x in range(1, 28)]
result = pd.concat(frames, keys=keys)
#result.sort_values(ascending=False, inplace=True)
result_gl = result.select_dtypes(include=['object']).copy()

result_gl = result_gl[result_gl.duplicated(['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first')]

result_gl = result_gl.drop_duplicates(subset=['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist'], keep='first', inplace=False).to_csv('./t2.csv')

print(frames)