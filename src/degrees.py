import harry_potter as hp
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

graph = harry_potter.get_graph(1);

def draw_degree_graph_directed(G):
    """
    Verilen yönlü grafın iç ve dış derecelerini çizdirir.
    
    Args:
    - G (DiGraph): Yönlü graf (networkx DiGraph türünde).
    """
    # İç dereceyi ve dış dereceyi hesaplayın
    in_degrees = dict(G.in_degree())
    out_degrees = dict(G.out_degree())

    # Grafı çizdirin
    pos = nx.spring_layout(G)
    nx.draw(G, pos, 
        with_labels=True, 
        node_size=700, 
        node_color="skyblue", 
        font_size=10, 
        font_color="black", 
        font_weight="bold"
    )

    # İç dereceleri göster
    nx.draw_networkx_labels(G, pos, 
        labels=in_degrees, 
        font_color="red", 
        font_size=8, 
        font_weight="bold"
    )

    # Dış dereceleri göster
    nx.draw_networkx_labels(G, pos, 
        labels=out_degrees, 
        font_color="green", 
        font_size=8, 
        font_weight="bold"
    )

    # Grafı göster
    plt.show()

def degree_table_directed(G):
    """
    Verilen yönlü grafın iç ve dış derecelerini bir tablo olarak gösterir.
    
    Args:
    - G (DiGraph): Yönlü graf (networkx DiGraph türünde).
    
    Returns:
    - pd.DataFrame: İç ve dış dereceleri içeren bir DataFrame.
    """
    # İç dereceyi ve dış dereceyi hesaplayın
    in_degrees = dict(G.in_degree())
    out_degrees = dict(G.out_degree())

    # Verileri bir DataFrame'e dönüştürün
    data = {
        "Node": list(G.nodes()),
        "In Degree": list(in_degrees.values()),
        "Out Degree": list(out_degrees.values())
    }
    df = pd.DataFrame(data)

    return df
