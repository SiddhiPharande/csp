from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(self.graph[vertex])

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

if __name__ == "__main__":
    graph = Graph()

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v = map(int, input("Enter an edge (u v): ").split())
        graph.add_edge(u, v)

    start_vertex = int(input("Enter the start vertex: "))

    print("\nBFS Traversal:")
    graph.bfs(start_vertex)

    print("\nDFS Traversal:")
    graph.dfs(start_vertex)
