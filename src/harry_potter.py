import networkx as nx
import numpy as np

def merge_matrice_files():
    """
    hpbook1.txt, hpbook2.txt, hpbook3.txt, hpbook4.txt, hpbook5.txt, hpbook6.txt
    dosyalarında bulunan komşuluk matrislerini birleştirir ve hpbook.txt dosyasına
    yazar.
    """
    for i in range(1, 7):
        file_path = f"./data/hpbook{i}.txt"
        matrix = read_matrix_from_file(file_path)
        matrix[matrix > 0] = 1

        if i == 1:
            result = matrix
        else:
            result += matrix

    result[result > 0] = 1

    np.savetxt("./data/hpbook.txt", result, fmt="%d")

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

def get_graph(book = 0):
    """
    Verilen kitaba ait yönlü grafı döndürür.
    Kitap numarası verilmezse tüm kitapların bulunduğu ortak graf döndürülür.

    Args:
    - book (int): Kitap numarası (1, 2, 3, 4, 5, 6).
    """
    file_path = f"./data/hpbook{book if 0 < book < 7 else ''}.txt"
    matrix = read_matrix_from_file(file_path)

    return create_graph_from_matrix(matrix)

def read_names_from_file(file_path = "./data/hpnames.txt"):
    """
    Verilen TXT dosyasını okuyarak içeriği bir Numpy dizisi olarak döndürür.

    Parameters:
    - file_path (str): Okunacak TXT dosyasının yolu.

    Returns:
    - data (np.ndarray): Dosyadaki verileri içeren bir Numpy dizisi.
    """

    data = np.genfromtxt(
        file_path, delimiter='\t',
        dtype=None, names=True,
        encoding='utf-8'
    )

    return data

def get_names():
    """
    Karakter isimlerini döndürür.
    """
    file_path = "./data/hpnames.txt"

    return read_names_from_file(file_path)

def get_houses():
    """
    Karakter hanelerini döndürür.
    """
    file_path = "./data/hphouses.txt"

    return read_names_from_file(file_path)

"""merge_matrice_files()
x = 0
for i in range(1, 7):
    print(i, ": ", get_graph(i))
    x += get_graph(i).number_of_edges()

print("toplam kenar sayısı: ", x)
print("farklı toplam kenar sayısı: ", get_graph())"""
