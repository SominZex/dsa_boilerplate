class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            #self.adj_matrix[v][u] = 1 <- used for undirected Graphs

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
            
    def dfs_util(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        print("Current vertex:",self.vertex_data[v])

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, recStack):
                        return True
                elif recStack[i]:
                    return True
        
        recStack[v] = False
        return False
    
    def is_cyclic(self):
        visited = [False] * self.size
        recStack = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                print() #new line
                if self.dfs_util(i, visited, recStack):
                    return True
        return False

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 1)  # C -> B
g.add_edge(2, 4)  # C -> E
g.add_edge(1, 5)  # B -> F
g.add_edge(4, 0)  # E -> A
g.add_edge(2, 6)  # C -> G

g.print_graph()

print("\nGraph has cycle:", g.is_cyclic())
