import harry_potter as hp
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

graph = hp.get_graph()
names = hp.get_names()

def get_degree_centrality(graph):
    # Derece merkeziliğini hesapla
    degree_centrality = nx.degree_centrality(graph)

    # DataFrame oluştur
    df = pd.DataFrame(
        list(degree_centrality.items()),
        columns=["Node", "Degree Centrality"]
    )
    return df

def write_degree_centrality_to_file(graph, output_file):
    df = get_degree_centrality(graph)

    # TXT dosyasına yaz
    df.to_csv(output_file, index=False, sep="\t")

    print(f"Derece merkeziliği bilgileri '{output_file}' dosyasına yazdırıldı.")

def plot_graph_from_df(df):
    # Sütun isimlerini al
    nodes = df["Node"]
    degree_centrality = df["Degree Centrality"]

    # Grafik çiz
    plt.bar(nodes, degree_centrality)

    # Grafik başlığını ekle
    plt.title("Derece Merkeziliği")

    # Eksen isimlerini ekle
    plt.xlabel("Kişi Index")
    plt.ylabel("Derece Merkeziliği")

    # Grafikleri göster
    plt.show()

plot_graph_from_df(get_degree_centrality(graph))
#write_degree_centrality_to_file(graph, "./results/degree_centrality.txt")
