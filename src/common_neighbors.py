import harry_potter as hp
import networkx as nx
import pandas as pd

graph = hp.get_graph()
names = hp.get_names()

def calc_common_neighbors(graph, node1, node2):
    set1 = set(graph.neighbors(node1))
    set2 = set(graph.neighbors(node2))
    return len(set1 & set2)

# bütün node ikilileri için "ortak komşular" değerini hesaplar, DataFrame olarak döndürür
# (1,2) hesaplanmışsa (2,1) hesaplanmaz
def calc_all_common_neighbors(graph = graph):
    nodes = graph.nodes()
    common_neighbors = {}
    for i in nodes:
        for j in nodes:
            if i != j:
                if (j, i) not in common_neighbors:
                    common_neighbors[
                        #(graph.nodes[i]["name"],
                        #graph.nodes[j]["name"])
                        i, j
                    ] = calc_common_neighbors(graph, i, j)
    return common_neighbors

def write_all_common_neighbors_to_csv_file(graph, output_file):
    common_neighbors = calc_all_common_neighbors(graph)
    df = pd.DataFrame(
        list(common_neighbors.items()),
        columns=["Karakter Çifti", "Ortak Komşular"]
    )
    df["Karakter Çifti"] = df["Karakter Çifti"].apply(lambda x: (names[str(x[0]+1)], names[str(x[1]+1)]))
    df.to_csv(output_file, index=False)
    print(f"Her düğüm çifti için ortak komşular '{output_file}' dosyasına yazdırıldı.")

write_all_common_neighbors_to_csv_file(graph, "./results/common_neighbors.csv")
