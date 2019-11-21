# sample code for wrangling data in pandas

# DATE AND TIME
# convert to date
df['datecolumn'] = pd.to_datetime(df['datecolumn'], format="%Y-%m-%d %H:%M:%S.0000000")
df['datecolumn'] = df['datecolumn'].dt.date
df['datecolumn'] = pd.to_datetime(df['datecolumn'])
# convert to time
df['timecolumn'] = pd.to_datetime(df['timecolumn'],format= '%H:%M' ).dt.time
# extract hour value in column
df_scan['uur'] = df['datecolumn'].dt.hour

# INFO
nr_of_unique_times = df['column'].nunique()
list_of_unique_items = df['column'].unique().tolist()
# dataframe information
df.info()
df.describe()

