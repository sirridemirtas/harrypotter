import harry_potter as hp
import networkx as nx
import pandas as pd

graph = hp.get_graph()

# networkx ile aldığı DiGraph objesinin iki düğümü için jaccard benzerliğini hesaplayan fonksiyon
def jaccard_similarity(node1, node2):
    """
    Verilen iki düğümün jaccard benzerliğini hesaplar.

    Args:
    - node1 (int): Birinci düğüm.
    - node2 (int): İkinci düğüm.
    - graph (DiGraph): Yönlü graf (networkx DiGraph türünde).

    Returns:
    - float: Jaccard benzerliği.
    """
    # node1'in komşularını al
    neighbors1 = set(graph.neighbors(node1))

    # node2'nin komşularını al
    neighbors2 = set(graph.neighbors(node2))

    # node1'in komşuları ile node2'nin komşularının kesişimini al
    intersection = neighbors1.intersection(neighbors2)

    # node1'in komşuları ile node2'nin komşularının birleşimini al
    union = neighbors1.union(neighbors2)

    # kesişim kümesinin boyutunu al
    intersection_size = len(intersection)

    # birleşim kümesinin boyutunu al
    union_size = len(union)

    if union_size == 0:
        jaccard = 0
    else:
        jaccard = intersection_size / union_size

    return jaccard


#her düğüm çifti için jaccard benzerliğini bir CSV dosyasına yazar, (1,2) hesaplanmışsa (2,1) hesaplanmaz
def write_all_jaccard_similarity_to_csv_file(output_file):
    """
    Verilen yönlü grafın bütün düğüm ikilileri için jaccard benzerliğini hesaplar.
    (1,2) hesaplanmışsa (2,1) hesaplanmaz.

    Args:
    - graph (DiGraph): Yönlü graf (networkx DiGraph türünde).
    - output_file (str): CSV dosyasının yolu.
    """
    # bütün düğüm ikilileri için jaccard benzerliğini hesapla
    similarity = {}
    for i in graph.nodes():
        for j in graph.nodes():
            if i != j:
                if (j, i) not in similarity:
                    similarity[
                        graph.nodes[i]["name"],
                        graph.nodes[j]["name"]
                    ] = jaccard_similarity(i, j)

    # CSV dosyasına yaz
    df = pd.DataFrame.from_dict((similarity), orient='index', columns=["Jacard Benzerliği"])
    df.to_csv(output_file)

    print(f"Jaccard benzerlikleri '{output_file}' dosyasına yazdırıldı.")

write_all_jaccard_similarity_to_csv_file("./results/jaccard_similarity.csv")
