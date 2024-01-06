import harry_potter as hp
import matplotlib.pyplot as plt

graph = hp.get_graph()

def plot_power_law_distribution(graph):
    degrees = dict(graph.degree())
    nodes = graph.nodes()

    values = [degrees[node] for node in nodes]
    values.sort(reverse=True)

    # Sütun grafik çizimi
    plt.bar(nodes, values, alpha=0.7, label='Derece')

    plt.xlabel('Düğümler')
    plt.ylabel('Derece')
    plt.legend()
    plt.title('Güç Yasası Dağılımı')
    plt.show()

def plot_power_law_distribution_2(graph):
    degrees = dict(graph.degree())
    nodes = graph.nodes()
    values = [degrees[node] for node in nodes]
    values.sort(reverse=True)

    plt.xscale('log')
    plt.loglog(values, 'b-', marker='o')
    plt.xlabel('Düğümler')
    plt.ylabel('Derece')
    plt.title('Güç Yasası Dağılımı')
    plt.show()

plot_power_law_distribution(graph)
plot_power_law_distribution_2(graph)
