import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

def get_clustering_coefficient(graph = graph):
    """
    Her düğüm için kümelenme katsayısını dizi olarak döndürür
    """
    return nx.clustering(graph)

# cc değerlerini csv dosyasına yazar
def write_clustering_coefficient_to_csv():
    with open("./results/clustering_coefficient.csv", "w") as file:
        file.write("Karakter,Kümelenme Katsayısı\n")
        for node, cc in get_clustering_coefficient().items():
            name = graph.nodes[node]["name"]
            file.write(f"{name},{cc}\n")
    print("Her düğüm için CC değerleri clustering_coefficient.csv dosyasına yazdırıldı.")

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

write_clustering_coefficient_to_csv()
