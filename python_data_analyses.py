import pandas as pd

# adjust columns on dataframe output
pd.options.display.max_colwidth = 10000
# or
pd.set_option('display.max_columns', None)

# use part of dataframe
df.sample(frac=0.1)
# or
df.sample(n=200)

# group by
df[['column1','column2']].groupby(['column1']).mean()
df[['column1','column2','column3','column4']].groupby(['column1','column2']).agg(['mean','count']).sort_values(by=[('column3','mean')])
df[['column1','column2','column3']].groupby(['column3']).agg({'column1':'mean', 'columns2': 'sum'})

# transform: add new columns based on grouping
df['new column'] = df.groupby('column1')['column2'].transform('sum')
# transform: fill Nan with mean of grouped column
df['column2'] = df.groupby('column1').transform(lambda x: x.fillna(x.mean()))

# pivot + round
pd.crosstab(index=df['column1'], columns=df['column2'], values=df['column3]', aggfunc='mean').round(1)
# or
pd.pivot_table(data=df, index=['column1'], columns=['column2'], values=['column3'], aggfunc='mean').round(1)

# where not + isin
df[~df['column1'].isin([1,2,3])]

# value counts with normalization
df['column'].value_counts(normalize=True)

# unique
df['column'].unique() # items
df['column'].nunique() # number of items

# cumulative sum
df['column'].cumsum()

# contains
df['column'].str.contains('item').sum()
                                                                  
# correlation
df.corr()
