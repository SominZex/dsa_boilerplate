class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.parent = [i for i in range(size)]  # Union-Find array

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        print('Union:',self.vertex_data[x],'+',self.vertex_data[y])
        self.parent[x_root] = y_root
        print(self.parent,'\n')

    def is_cyclic(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.adj_matrix[i][j]:
                    x = self.find(i)
                    y = self.find(j)
                    if x == y:
                        return True
                    self.union(x, y)
        return False

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(1, 0)  # B - A
g.add_edge(0, 3)  # A - D
g.add_edge(0, 2)  # A - C
g.add_edge(2, 3)  # C - D
g.add_edge(3, 4)  # D - E
g.add_edge(3, 5)  # D - F
g.add_edge(3, 6)  # D - G
g.add_edge(4, 5)  # E - F

print("Graph has cycle:", g.is_cyclic())
