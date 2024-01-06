import harry_potter as hp
import networkx as nx
import matplotlib.pyplot as plt

graph = hp.get_graph();

def plot_degree_distribution(graph, power_law = False):
    in_degrees = dict(graph.in_degree())  # İç dereceleri al
    out_degrees = dict(graph.out_degree())  # Dış dereceleri al

    nodes = graph.nodes()

    in_values = [in_degrees[node] for node in nodes]
    out_values = [out_degrees[node] for node in nodes]

    if power_law:
        in_values.sort(reverse=True)
        out_values.sort(reverse=True)
    # Sütun grafik çizimi
    plt.bar(nodes, in_values, alpha=0.7, label='In Degree')
    plt.bar(nodes, out_values, alpha=0.7, label='Out Degree', bottom=in_values)

    plt.xlabel('Düğümler')
    plt.ylabel('Derece')
    plt.legend()
    plt.title(
        "Derece Dağılımı" if power_law==False
        else "Derece Dağılımı (Güç Yasası)"
    )
    plt.show()

# Derece dağılımını çiz
plot_degree_distribution(graph)
plot_degree_distribution(graph, power_law=True)
