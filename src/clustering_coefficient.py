import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

def get_clustering_coefficient(graph = graph):
    """
    Her düğüm için kümelenme katsayısını dizi olarak döndürür
    """
    return nx.clustering(graph)

def get_average_clustering_coefficient(graph = graph):
    """
    Graf için ortalama kümelenme katsayısını döndürür
    """
    return nx.average_clustering(graph)

print(
    "Her düğüm için ortalama kümelenme katsayısı:",
    get_clustering_coefficient()
)

print(
    "Ortalama kümelenme katsayısı:",
    get_average_clustering_coefficient()
)
