import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

# calculate clustering coefficient of grap with function
def get_clustering_coefficient(graph = graph):
    return nx.clustering(graph)

print(get_clustering_coefficient())
