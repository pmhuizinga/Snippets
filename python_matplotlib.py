# sample code for using matplotlib and seaborn

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

# background colors
fig.patch.set_facecolor('xkcd:gray') # graph background
ax1.set_facecolor('xkcd:salmon') # axis part background

#------------------------------------------------------------------
# line plot
plt.figure(figsize=(20,10))
plt.plot(df['x_values'], df['y_values'])
plt.title('title')
plt.xticks(rotation='vertical')
plt.xlabel('x label')
plt.ylabel('y label')
plt.grid(True)
plt.legend()
plt.text(x_value, y_value, 'Text value') # add text in graph
mean_series = pd.Series(np.repeat(df['column'].mean(), df.shape[0]))
plt.plot(df.index, mean_series, label='average') # plot mean in graph
plt.axvline(np.quantile(df.index.values, .50), color='orange', label='label') # create vertical line in graph (2nd percentile)
plt.savefig('filename.png')
plt.show()

#------------------------------------------------------------------
# basic bar chart
plt.figure(figsize=(20,10))
plt.bar(df['x_values'], df['y_values'])
plt.show()

#------------------------------------------------------------------
# basic scatter plot
# s = size
# hue = distiction value
fig, ax = plt.subplots(figsize=(20,20))
ax = sns.scatterplot(x="x_values",
                    y="y_values",
                    data=df_wijk_coords[['x_values','y_values']], 
                    s=1000, 
                    hue=df['hue_values'],
                    alpha=0.7,
                    c=color, 
                    edgecolors='black')
# annotate values
for i in zip(text_values, x_values, y_values):
    plt.annotate(i[0], xy=i[1:3])
    
# basic 3D scatter plot
fig = plt.figure(figsize=([20,20]))
ax = fig.add_subplot(111, projection='3d')

y = np.array(df['x_values'])
x = np.array(df['y_values'])
z = np.array(df['z_values'])

ax.scatter(x, y, z)
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_zlabel('z label')
plt.show()

#------------------------------------------------------------------
# create subplots with 3 columns and a variable number of rows
nr_or_rows = math.ceil(float(len([list]) / 3.0))
fig = plt.figure()
fig, ax = plt.subplots(nr_or_rows, 3, sharey=True, figsize=(20,10))

#plot positions for each entity in list
for nr, entity in enumerate([list]):
    row = math.ceil((nr + 1) / 3) - 1
    column = round(((((nr + 1) / 3)) - row) * 3) -1
    df = df_pos_total[df_pos_total.entity_name == entity]
    x = df.instrument_name
    y = df.value

    ax[row][column].bar(x,y)
    ax[row][column].set_title(entity.upper())

#------------------------------------------------------------------
# create stacked bar chart with scaled values
N = df['column'].nunique()  # source for x axis
ind = np.arange(N)    # the x locations for the groups
width = .95

# rescale market values to percentage of total
df1 = df_source.groupby(['column1','column2']).agg({'value column': 'sum'})
df = df1.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
df.reset_index(inplace=True)

for index, variable in enumerate(df['column to be stacked'].unique()):
    if index == 0:
        plt.bar(ind, df[df['column to be stacked'] == variable]['value column'], width=width, label=variable)
        t = df[df['column'] == at]['totalmarketvaluebase'] # create list of values
    else:
        plt.bar(ind, df[df['column to be stacked'] == variable]['value column'], bottom=t, width=width, label=variable)
        t = [c + d for c, d in zip(t, df[df['column to be stacked'] == variable]['value column'])] # add values from value column

plt.ylabel('y - label')
plt.xticks(ind, pd.to_datetime(df['date column']).dt.date.unique()) # only relevant for date axis
plt.xticks(rotation=90)
plt.legend()
plt.show()    
