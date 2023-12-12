import networkx as nx
import numpy as np

def read_matrix_from_file(file_path):
    return np.loadtxt(file_path, dtype=int)

def create_graph_from_matrix(matrix):
    graph = nx.DiGraph()
    num_nodes = matrix.shape[0]

    for i in range(num_nodes):
        graph.add_node(i)

    for i in range(num_nodes):
        for j in range(num_nodes):
            if matrix[i, j] == 1:
                graph.add_edge(i, j)

    return graph

def get_graph(book=1):
    file_path = "./data/hpbook"+str(book if (book<7 and book>1) else 1)+".txt"
    matrix = read_matrix_from_file(file_path)

    return create_graph_from_matrix(matrix)
