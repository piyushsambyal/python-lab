import numpy as np
import matplotlib.pyplot as plt

# Create a range for number of vertices
V = np.linspace(10, 1000, 100)  # From 10 to 1000 vertices

# Assume a constant k for edges proportional to vertices
k = 5  # For example, E = 5V

# Calculate time complexity O(E + V log V)
E = k * V
time_complexity = E + V * np.log2(V)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(V, time_complexity, label="Time Complexity O(E + V log V)")
plt.title("Time Complexity Analysis: O(E + V log V)")
plt.xlabel("Number of Vertices (V)")
plt.ylabel("Time Complexity (arbitrary units)")
plt.legend()
plt.grid(True)
plt.show()
