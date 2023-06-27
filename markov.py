import matplotlib.pyplot as plt
import networkx as nx

# Define the transition probabilities
edges = {
    ("State1", "State1"): 0.5,
    ("State1", "State2"): 0.5,
    ("State1", "State3"): 0.5,
    ("State2", "State1"): 0.7,
    ("State2", "State3"): 0.3,
    ("State3", "State1"): 1.0
}

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for edge, prob in edges.items():
    G.add_edge(edge[0], edge[1], weight=prob, label=prob)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=40)
labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
