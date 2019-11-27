import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# create sample data
node_list = ['A', 'B', 'C', 'D']
source = ['A', 'B', 'C', 'D']
target = ['B', 'C', 'D', 'A']
df = pd.DataFrame({'source': source, 'target': target})

# create graph database
G = nx.Graph()

# add nodes
G.add_nodes_from(node_list, type="test")

# add edges
edges = []
for index, row in df.iterrows():
    print(row)
    edges.append((row['source'], row['target']))

G.add_edges_from(edges)

# draw graph
plt.figure(3, figsize=(12, 12))
nx.draw(G)
plt.show()

# alternative way to 'populate' G using a dataframe:
G = nx.from_pandas_dataframe(df=bd_sub, source='Source', target='Target', edge_attr='gender', 
                            create_using=nx.Graph())

# shortest path sample
import networkx as nx
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
nx.shortest_path(G, 'A', 'D', weight='weight')