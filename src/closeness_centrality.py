import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

def get_closeness_centrality(graph = graph):
    return nx.closeness_centrality(graph)

print(get_closeness_centrality())
