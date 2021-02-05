# sample code for wrangling data in pandas

# DATE AND TIME
# convert to date
df['datecolumn'] = pd.to_datetime(df['datecolumn'], format="%Y-%m-%d %H:%M:%S.0000000")
df['datecolumn'] = df['datecolumn'].dt.date
df['datecolumn'] = pd.to_datetime(df['datecolumn'])
# or
df['datecolumn'] = df['datecolumn'].astype("datetime64")
# convert to time
df['timecolumn'] = pd.to_datetime(df['timecolumn'],format= '%H:%M' ).dt.time
# extract hour value in column
df_scan['uur'] = df['datecolumn'].dt.hour
# all workingdays
all_working_days = [d.strftime("%Y-%m-%d") for d in pd.date_range(start='1/1/2019', end='1/08/2019').to_datetime().date if d.isoweekday() <= 5]

# NUMERIC
pd.to_numeric(df["column"], errors='coerce')

# INFO
nr_of_unique_times = df['column'].nunique()
list_of_unique_items = df['column'].unique().tolist()
# dataframe information
df.info()
df.describe()

# WRANGLING
# fill empty values
df['column'].fillna('fill value', inplace=True)

# merge both dataframes
df_a = pd.merge(df_b, df_c,
                      left_on=['column df_b'],
                      right_on=['column df_c'])
# Pivot
# melt dataframe
df = pd.melt(df,id_vars=['CADIS_PORTFOLIO_GROUP_CODE', 'AS_OF_DATE'],
                     value_vars=[‘col1’,’col2’],
                     var_name='TENOR',
                     value_name='VALUE')
