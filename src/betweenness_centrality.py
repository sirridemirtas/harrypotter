import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

def get_betweenness_centrality(graph = graph):
    return nx.betweenness_centrality(graph)

print(get_betweenness_centrality())

# anlamsız bulunduğu için iptal edildi
