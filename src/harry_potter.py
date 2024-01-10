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
    print("Birleştirilmiş matris './data/hpbook.txt' dosyasına yazdırıldı.")

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

def add_attrs_to_graph(graph):
    """
    Verilen grafa hpattributes.txt dosyasındaki özellikleri ekler.

    Args:
    - graph (nx.DiGraph): Graf.
    """
    attrs = get_attrs()

    for node in graph.nodes:
        for key, value in attrs[node+1].items():
            graph.nodes[node][key] = value

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

    return add_attrs_to_graph(create_graph_from_matrix(matrix))

def get_houses():
    return {
        "1": "Gryffindor",
        "2": "Hufflepuff",
        "3": "Ravenclaw",
        "4": "Slytherin"
    }

def get_names():
    """
    Karakterlerin isimlerini okur ve sözlük olarak döndürür.
    """
    file_path = "./data/hpnames.txt"
    names = {}

    with open(file_path, "r") as file:
        lines = file.readlines()
        lines = lines[1:] #ilk satırı atla

        for line in lines:
            line = line.strip()
            line = line.replace('"', "")
            line = line.split("\t")

            names[(line[0])] = line[1]

    return names

def get_attrs():
    """
    Karakterlerin özelliklerini okur ve sözlük olarak döndürür.
    """
    file_path = "./data/hpattributes.txt"
    characters = {}

    names = get_names()
    houses = get_houses()

    with open(file_path, "r") as file:
        lines = file.readlines()
        lines = lines[1:] #ilk satırı atla

        for line in lines:
            line = line.strip()
            line = line.replace('"', "")
            line = line.split("\t")

            characters[int(line[0])] = {
                "schoolyear": line[1:][0],
                "gender": line[1:][1],
                "house": houses[line[1:][2]],
                "name": names[line[0]]
            }
    return characters
