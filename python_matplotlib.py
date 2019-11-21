# sample code for using matplotlib and seaborn

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# basic line plot
plt.figure(figsize=(20,10))
plt.plot(df['x_values'], df['y_values'])
plt.title('title')
plt.xticks(rotation='vertical')
plt.legend()
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
                    hue=df['hue_values'])

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

