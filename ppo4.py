import numpy as np
import matplotlib.pyplot as plt

# Number of vertices (V) range
V = np.linspace(10, 1000, 200)  # From 10 to 1000 vertices

# Constants for edges (E proportional to V, e.g., sparse graph)
k_values = [2, 5, 10]  # Different constants for E = kV

# Plotting time complexity O(E + V log V)
plt.figure(figsize=(10, 6))

for k in k_values:
    E = k * V  # Edges proportional to vertices
    complexity = E + V * np.log2(V)  # O(E + V log V)
    plt.plot(V, complexity, label=f"E = {k}V")

# Graph labels and legends
plt.title("Time Complexity O(E + V log V)")
plt.xlabel("Number of Vertices (V)")
plt.ylabel("Time Complexity (arbitrary units)")
plt.legend()
plt.grid(True)
plt.show()
