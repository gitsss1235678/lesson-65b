class Graph:
    def __init__(self, num_nodes):
        self.num_nods = num_nodes
        self.adjacency_matrix = [[0 for i in range(num_nodes)] for j in range(num_nodes)]

        def add_edge(self, node1, node2, weight=1):
            self.adjacency_matrix[node1][node2] = weight
            self.adjacency_matric[node1][node2] = weight

        def get_nodes(self):
            return range(self.num_nodes)

        def get_edges(self):
            edges = []
            for i in range(self.num_nodes):
                for j in range(self.num_nodes):
                    if self.adjacency_matrix[i][j] != 0:
                        edges.append((i, j))
            return edges

        def __repr__(self):
            return str(self.adjacency_matrix)

graph = Graph(3)

graph.add_edge(4, 8)
graph.add_edge(4, 2)
graph.add_edge(2, 5)

print(graph)