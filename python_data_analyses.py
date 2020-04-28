import pandas as pd

# adjust columns on dataframe output
pd.options.display.max_colwidth = 10000

# use part of dataframe
df = df.sample(frac=0.1)


