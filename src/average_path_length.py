import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

def average_path_length_for_weakly_connected(graph):
    weakly_connected_components = list(nx.weakly_connected_components(graph))

    if len(weakly_connected_components) == 1:
        # Zayıf bağlı bileşen yoksa ortalama yol uzunluğu hesaplanamaz.
        return None

    total_path_length = 0
    total_paths = 0

    for component in weakly_connected_components:
        subgraph = graph.subgraph(component)
        if nx.is_strongly_connected(subgraph):
            # Zayıf bağlı bileşenin içinde güçlü bağlı bileşen varsa, ortalama uzunluğa katma.
            total_path_length += nx.average_shortest_path_length(subgraph)
            total_paths += 1

    if total_paths == 0:
        # Hiç güçlü bağlı bileşen yoksa, ortalama yol uzunluğu hesaplanamaz.
        return None

    return total_path_length / total_paths

result = average_path_length_for_weakly_connected(graph)
print(result)
