import matplotlib.pyplot as plt
import numpy as np
vertices = np.arange(1, 101)  
edges = vertices * (vertices - 1) / 2  
adj_matrix = vertices**2 
adj_list = (vertices + edges) * np.log(vertices) 
plt.figure(figsize=(10, 6))
plt.plot(vertices, adj_matrix, label="Adjacency Matrix: O(V^2)", color='blue')
plt.plot(vertices, adj_list, label="Adjacency List: O((V + E) log V)", color='green')
plt.title("Time Complexity of Dijkstra's Algorithm")
plt.xlabel("Number of Vertices (V)")
plt.ylabel("Time Complexity")
plt.legend()
plt.grid(True)
plt.show()
