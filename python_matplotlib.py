# sample code for using matplotlib and seaborn

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

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
plt.axvline(np.quantile(df.index.values, .50), color='orange', label='label') # create vertical line in graph (2nd percentile)
plt.savefig('filename.png')
plt.show()


# basic bar chart
plt.figure(figsize=(20,10))
plt.bar(df['x_values'], df['y_values'])
plt.show()


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

