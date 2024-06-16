vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjacency_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print(row)

def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print(vertices[j], end=" ")
        print()  # new line

print_adjacency_matrix(adjacency_matrix)
print_connections(adjacency_matrix, vertexData)