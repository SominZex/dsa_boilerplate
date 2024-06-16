class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = []  # For storing edges as (u, v, weight)
        self.vertex_data = [''] * size  # Store vertex names

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((u, v, weight))  # Add edge with weight
            
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskals_algorithm(self):
        result = []  # MST
        i = 0  # edge counter

        self.edges = sorted(self.edges, key=lambda item: item[2])

        parent, rank = [], []

        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        while i < len(self.edges):
            u, v, weight = self.edges[i]
            i += 1
            
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        print("Edge \tWeight")
        for u, v, weight in result:
            print(f"{self.vertex_data[u]}-{self.vertex_data[v]} \t{weight}")

g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(0, 1, 4)  #A-B,  4
g.add_edge(0, 6, 10) #A-G, 10
g.add_edge(0, 2, 9)  #A-C,  9
g.add_edge(1, 2, 8)  #B-C,  8
g.add_edge(2, 3, 5)  #C-D,  5
g.add_edge(2, 4, 2)  #C-E,  2
g.add_edge(2, 6, 7)  #C-G,  7
g.add_edge(3, 4, 3)  #D-E,  3
g.add_edge(3, 5, 7)  #D-F,  7
g.add_edge(4, 6, 6)  #E-G,  6
g.add_edge(5, 6, 11) #F-G, 11

print("Kruskal's Algorithm MST:")
g.kruskals_algorithm()
