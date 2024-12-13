import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_experiment():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ('A', 'B', 4),
        ('A', 'C', 1),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3),
    ])
    
    source_node = 'A'
    
    # Run Dijkstra's algorithm to find shortest paths and distances
    shortest_paths = nx.single_source_dijkstra_path(G, source_node)
    shortest_distances = nx.single_source_dijkstra_path_length(G, source_node)
    
    print(f"Shortest paths from {source_node}:")
    for target, path in shortest_paths.items():
        print(f"Path to {target}: {path}, Distance: {shortest_distances[target]}")
    
    # Extract edges that form the shortest path tree
    tree_edges = []
    for target, path in shortest_paths.items():
        if len(path) > 1:  # Avoid the source node as it's not part of any path
            # Form edges from the path
            tree_edges.extend(zip(path[:-1], path[1:]))
    
    # Create a new graph for the shortest path tree
    tree_G = nx.Graph()
    tree_G.add_edges_from(tree_edges)
    
    # Positioning nodes using spring layout for better visualization
    pos = nx.spring_layout(G)
    
    # Plot the original graph and the shortest path tree
    plt.figure(figsize=(8, 6))
    
    # Draw original graph (in gray)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", edge_color='gray')
    
    # Highlight the shortest path tree edges (in red)
    nx.draw_networkx_edges(tree_G, pos, edge_color="red", width=2)
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Title and display
    plt.title(f"Shortest Path Tree from {source_node}")
    plt.show()

dijkstra_experiment()
