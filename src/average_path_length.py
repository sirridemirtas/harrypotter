import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

"""Tüm düğümler kenara sahip olmadığı için, kenara sahip olmayan
düğümler çıkarılıp ortalama yol uzunluğu hesaplanacak"""

"""Graf güçlü bağlı (strongly connected) olmadığı için ortalama yol
uzunluğu hesaplanamıyor"""

"""# grafı güçlü bağlı bileşenlerine ayırıyoruz
def get_strongly_connected_components(graph = graph):
    return nx.strongly_connected_components(graph)

def remove_nodes_without_edges(graph = graph):
    nodes_without_edges = []
    for node in graph.nodes():
        if graph.degree(node) == 0:
            nodes_without_edges.append(node)
    graph.remove_nodes_from(nodes_without_edges)
    return graph

def get_average_path_length(graph = graph):
    return nx.average_shortest_path_length(
        remove_nodes_without_edges(graph)
    )

#her bir güçlü bağlı bileşen için ortalama yol uzunluğu hesaplanıyor
for component in get_strongly_connected_components():
    print(get_average_path_length(graph.subgraph(component)))
"""
