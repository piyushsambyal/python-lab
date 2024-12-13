import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_experiment():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ('P', 'Q', 6),
        ('P', 'R', 3),
        ('P', 'S', 5),
        ('Q', 'R', 2),
        ('Q', 'T', 8),
        ('R', 'S', 7),
        ('R', 'T', 4),
        ('S', 'U', 10),
        ('T', 'U', 1),
    ])
    source_node = 'P'
    shortest_paths = nx.single_source_dijkstra_path(G, source_node)
    shortest_distances = nx.single_source_dijkstra_path_length(G, source_node)
    print(f"Shortest paths from {source_node}:")
    for target, path in shortest_paths.items():
        print(f"Path to {target}: {path}, Distance: {shortest_distances[target]}")
    tree_edges = []
    for target, path in shortest_paths.items():
        if len(path) > 1: 
            tree_edges.extend(zip(path[:-1], path[1:]))
    tree_G = nx.Graph()
    tree_G.add_edges_from(tree_edges)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", edge_color='gray')
    nx.draw_networkx_edges(tree_G, pos, edge_color="red", width=2)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Shortest Path Tree from {source_node}")
    plt.show()

dijkstra_experiment()

