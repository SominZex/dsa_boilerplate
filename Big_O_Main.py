# calculating time complexity / WOrst case scenerio
import time
#import the Algorithm developed as module from specific directory. i.e. Algorithms.binary_search.binary_search
from Algorithms.shortest_path.Dijkstra_Algo_Implemented import Graph

def calculate_time_complexity(func, *args, **kwargs):
    """
    Calculate the time complexity of a function.

    Parameters:
        func (function): The function to analyze.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        time_taken (float): Time taken to execute the function.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

def rate_time_complexity(time_taken, thresholds):
    """
    Rate the time complexity based on time taken and thresholds.

    Parameters:
        time_taken (float): Time taken for the function.
        thresholds (dict): Dictionary of threshold values for ratings.

    Returns:
        rating (str): Rating based on time complexity.
    """
    if time_taken <= thresholds['excellent']:
        return 'Excellent'
    elif time_taken <= thresholds['good']:
        return 'Good'
    elif time_taken <= thresholds['fair']:
        return 'Fair'
    else:
        return 'Poor'

# Create an instance of the Graph class
g = Graph(7)

# Add vertex data
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

# Add edges with weights
g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

# Dijkstra's algorithm from D to all vertices
print("Dijkstra's Algorithm starting from vertex D:\n")
distances, predecessors = g.dijkstra('D')
for i, d in enumerate(distances):
    path = g.get_path(predecessors, 'D', g.vertex_data[i])
    print(f"{path}, Distance: {d}")

# Calculate the time taken for the dijkstra method
input_size = g.size  # Number of vertices in the graph
time_taken = calculate_time_complexity(g.dijkstra, 'D')

# Define rating thresholds
thresholds = {
    'excellent': 0.001,  # Threshold for excellent rating (in seconds)
    'good': 0.01,         # Threshold for good rating (in seconds)
    'fair': 0.1           # Threshold for fair rating (in seconds)
}

# Calculate the time taken for the dijkstra method
input_size = g.size  # Number of vertices in the graph
time_taken = calculate_time_complexity(g.dijkstra, 'D')
print(f"Time taken for Dijkstra's algorithm with input size {input_size}: {time_taken} seconds")

# Get the rating based on time complexity
rating = rate_time_complexity(time_taken, thresholds)
print(f"Rating for Dijkstra's algorithm with input size {input_size}: {rating}")
