import pandas as pd

df2 = pd.Cov = pd.read_csv(r"pp-complete.csv",names=['tui', 'price', 'dot', 'postcode', 'type', 'age', 'duration', 'paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist', 'ppd',  'rec_stat'], parse_dates=['dot'], chunksize=1000000)
for chunk in df2:
    voters_street = chunk[['paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist']]

    result = pd.DataFrame(voters_street)

#result.sort_values(ascending=False, inplace=True)
    result_gl = result.select_dtypes(include=['object']).copy()

    result_gl = result_gl[result_gl.duplicated(['paon', 'saon', 'street', 'loc', 'city',
                  'dist', 'main_dist'], keep='first')]

    result_gl = result_gl.drop_duplicates(subset=['paon', 'saon', 'street', 'loc', 'city',
                  'dist', 'main_dist'], keep='first', inplace=False).to_csv('./t2.csv')