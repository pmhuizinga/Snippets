import pandas as pd

# adjust columns on dataframe output
pd.options.display.max_colwidth = 10000

# use part of dataframe
df.sample(frac=0.1)
# or
df.sample(n=200)

# group by
df[['column1','column2']].groupby(['column1']).mean()
df[['column1','column2','column3','column4']].groupby(['column1','column2']).agg(['mean','count']).sort_values(by=[('column3','mean')])

# where not + isin
df[~df['column1'].isin([1,2,3])]

# value counts with normalization
df['column'].value_counts(normalize=True)

# unique
df['column'].unique() # items
df['column'].nunique() # number of items
