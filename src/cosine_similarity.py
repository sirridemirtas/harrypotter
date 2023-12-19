import harry_potter as hp
import networkx as nx
import numpy as np
import pandas as pd

graph = hp.get_graph()

def calc_cosine_similarity(graph, node_a, node_b):
    """
    Verilen DiGraph üzerinde iki düğüm arasındaki kosinüs benzerliğini hesaplar.

    Args:
    - graph (nx.DiGraph): DiGraph türündeki graf.
    - node_a: İlk düğüm.
    - node_b: İkinci düğüm.

    Returns:
    - similarity (float): Kosinüs benzerliği.
    """
    # Düğümleri temsil eden vektörleri al
    vector_a = np.array(list(graph.nodes[node_a].values()))
    vector_b = np.array(list(graph.nodes[node_b].values()))

    # Kosinüs benzerliğini hesapla
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)

    # Paydanın sıfır olma durumunu kontrol et
    if norm_a == 0 or norm_b == 0:
        return 0.0  # veya başka bir değer

    similarity = dot_product / (norm_a * norm_b)

    return similarity

def calc_all_cosine_similarity(graph = graph):
    """
    Verilen DiGraph üzerindeki bütün düğüm ikilileri için kosinüs benzerliğini hesaplar.
    (1,2) hesaplanmışsa (2,1) hesaplanmaz.

    Args:
    - graph (nx.DiGraph): DiGraph türündeki graf.

    Returns:
    - similarity (DataFrame): Kosinüs benzerliği değerlerini tutan DataFrame.
    """
    nodes = graph.nodes()
    similarity = {}
    for i in nodes:
        for j in nodes:
            if i != j:
                if (j, i) not in similarity:
                    similarity[(i, j)] = calc_cosine_similarity(graph, i, j)
    return similarity


# her düğüm çifti için kosinüs benzerliğini bir CSV dosyasına yazar, (1,2) hesaplanmışsa (2,1) hesaplanmaz
def write_all_cossine_similarity_to_csv_file(graph, output_file):
    similarity = calc_all_cosine_similarity(graph)

    # DataFrame oluştur
    df = pd.DataFrame(
        list(similarity.items()),
        columns=["Node", "Cosine Similarity"]
    )

    # CSV dosyasına yaz
    df.to_csv(output_file, index=False)

    print(f"Kosinüs benzerliği bilgileri '{output_file}' dosyasına yazdırıldı.")

write_all_cossine_similarity_to_csv_file(graph, "./results/cosine_similarity.csv")
