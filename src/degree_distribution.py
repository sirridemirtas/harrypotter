import harry_potter as hp
import networkx as nx
import matplotlib.pyplot as plt

graph = hp.get_graph(1);

def plot_degree_distribution(G):
    in_degrees = dict(G.in_degree())  # İç dereceleri al
    out_degrees = dict(G.out_degree())  # Dış dereceleri al

    nodes = G.nodes()

    in_values = [in_degrees[node] for node in nodes]
    out_values = [out_degrees[node] for node in nodes]

    # Sütun grafik çizimi
    plt.bar(nodes, in_values, alpha=0.7, label='In Degree')
    plt.bar(nodes, out_values, alpha=0.7, label='Out Degree', bottom=in_values)

    plt.xlabel('Düğümler')
    plt.ylabel('Derece')
    plt.legend()
    plt.title('Harry Potter Karakterlerinin Verdikleri Desteğe Göre Derece Dağılımı')
    plt.show()

# Derece dağılımını çiz
plot_degree_distribution(graph)
