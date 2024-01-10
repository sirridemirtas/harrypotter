import harry_potter as hp
import matplotlib.pyplot as plt
import networkx as nx

graph = hp.get_graph()

def get_strongly_connected_components(graph = graph):
    return nx.strongly_connected_components(graph)

def print_strongly_connected_components(graph = graph):
    for i in get_strongly_connected_components(graph):
        print(i)

def draw_strongly_connected_components(graph = graph):
    print(graph)

    nx.draw(graph, with_labels=True)
    plt.show()

#print_strongly_connected_components()
draw_strongly_connected_components()
