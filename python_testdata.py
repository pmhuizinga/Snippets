import pandas as pd

# create dummy table with 30 records and 4 columns
pd.util.testing.makeDataFrame()

# modify rows and columns
pd.util.testing.N = 10
pd.util.testing.K = 5
pd.util.testing.makeDataFrame()
