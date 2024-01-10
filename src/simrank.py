import harry_potter as hp
import networkx as nx
import pandas as pd

graph = hp.get_graph()

def calc_simrank_similarity(graph, node1, node2):
    return nx.simrank_similarity(graph, node1, node2)

# bütün node ikilileri için SimRank benzerlik değerini hesaplar
# (1,2) hesaplanmışsa (2,1) hesaplanmaz
def calc_all_simrank_similarities(graph = graph):
    nodes = graph.nodes()
    simrank_similarities = {}
    for i in nodes:
        for j in nodes:
            if i != j:
                if (j, i) not in simrank_similarities:
                    simrank_similarities[i, j] = calc_simrank_similarity(graph, i, j)
    return simrank_similarities

def write_all_simrank_similarities_to_csv_file(graph, output_file):
    simrank_similarities = calc_all_simrank_similarities(graph)
    df = pd.DataFrame(
        list(simrank_similarities.items()),
        columns=["Karakter Çifti", "SimRank Değeri"]
    )
    df["Karakter Çifti"] = df["Karakter Çifti"].apply(lambda x: (names[str(x[0]+1)], names[str(x[1]+1)]))
    df.to_csv(output_file, index=False)
    print(f"Her düğüm çifti için SimRank değeri '{output_file}' dosyasına yazdırıldı.")

write_all_simrank_similarities_to_csv_file(graph, "./results/simrank.csv")
