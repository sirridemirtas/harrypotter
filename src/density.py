import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

# çizge çift yönlü olduğu için 2 ile çarpıyoruz
graph_density = float(nx.density(graph)) * 2

print("Graf Yoğunluğu:", graph_density)
