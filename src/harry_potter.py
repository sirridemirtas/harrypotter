import networkx as nx
import numpy as np

def read_matrix_from_file(file_path):
    """
    Verilen dosyadan matrisi okur ve döndürür.

    Args:
    - file_path (str): Dosya yolu.
    """
    return np.loadtxt(file_path, dtype=int)

def create_graph_from_matrix(matrix):
    """
    Verilen matristen yönlü graf oluşturur ve döndürür.

    Args:
    - matrix (np.ndarray): Matris.
    """
    graph = nx.DiGraph()
    num_nodes = matrix.shape[0]

    for i in range(num_nodes):
        graph.add_node(i)

    for i in range(num_nodes):
        for j in range(num_nodes):
            if matrix[i, j] == 1:
                graph.add_edge(i, j)

    return graph

book = 1

def get_graph(_book = book):
    """
    Verilen kitaba ait yönlü grafı döndürür.

    Args:
    - book (int): Kitap numarası (1, 2, 3, 4, 5, 6).
    """
    file_path = f"./data/hpbook{book if 1 < _book < 7 else 1}.txt"
    matrix = read_matrix_from_file(file_path)

    return create_graph_from_matrix(matrix)
