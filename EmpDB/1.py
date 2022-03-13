import pandas as pd
df2 = pd.read_csv(r"pp-complete.csv", engine='python', sep=",", chunksize=1000000, names=['tui', 'price', 'dot', 'postcode', 'type', 'age', 'duration', 'paon', 'saon', 'street', 'loc', 'city',
              'dist', 'main_dist', 'ppd',  'rec_stat'])

