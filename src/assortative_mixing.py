import harry_potter as hp
import networkx as nx

graph = hp.get_graph()

print(
    "Akranlığa göre homofili katsayısı:",
    nx.attribute_assortativity_coefficient(graph, 'schoolyear')
)

print(
    "Cinsiyet bilgisine göre homofili katsayısı:",
    nx.attribute_assortativity_coefficient(graph, 'gender')
)

print(
    "Hane bilgisine göre homofili katsayısı:",
    nx.attribute_assortativity_coefficient(graph, 'house')
)
