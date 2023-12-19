import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

graph_density = nx.density(graph)

print("Graf Yoğunluğu:", graph_density)
