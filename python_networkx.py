import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import operator
import warnings

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

# read from file
data = nx.read_edgelist('g:/networkx_test.txt', create_using=nx.Graph(), nodetype=str)

# spring layout
pos = nx.spring_layout(data)
warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20, 15)
plt.axis('off')
nx.draw_networkx(data, pos, with_labels=False, node_size=15)
plt.show()

# pagerank
pagerank = nx.pagerank(data)
sorted_pagerank = sorted(pagerank.items(), key=operator.itemgetter(1), reverse=True)

# circular layout
pos = nx.circular_layout(G)
warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (40, 40)
plt.axis('off')
nx.draw_networkx(G, pos, with_labels=True, font_size=6, node_size=12, alpha=0.5) 
plt.show()

# discover cycles in dataset
Gd=nx.from_pandas_dataframe(df_unpivot, source='source', target='target', create_using=nx.DiGraph())
print(nx.find_cycle(Gd))

# directed graph
data = nx.DiGraph(directed=True)

data.add_nodes_from(['A','B'], type='test nodes')
data.add_nodes_from(['D','E'], type='more test nodes')
data.add_edges_from([('A', 'B')], type='test edge')

pos = nx.circular_layout(data)
plt.axis('off')

node_attrs = nx.get_node_attributes(data, 'type')
node_colors = []
for node, attr in node_attrs.items():
    if attr == 'test nodes':
        color = 'blue'
    elif attr == 'more test nodes':
        color = 'red'

    node_colors.append(color)

edge_labels=dict([((u,v,),d['type']) for u,v,d in data.edges(data=True)])
    
nx.draw_networkx_nodes(data, pos,  node_color=node_colors, node_size=300, font_size=12, alpha=.3)
nx.draw_networkx_labels(data, pos, alpha=1, font_color='black')
nx.draw_networkx_edges(data, pos, font_size=8, arrows=True, alpha=.5, arrowsize=10, width=1, arrowstyle='-|>') #arrowsize=5, width=1, arrowstyle='-|>'
nx.draw_networkx_edge_labels(data,pos,edge_labels=edge_labels, alpha=.5)
plt.show()
