# city_graph = {}

# def get_graph():
#     num_cities = int(input("Enter no. of cities: "))
#     for city in range(num_cities):
#         key = input("Enter city: ")
#         value = input("Enter it's nodes: ")
#         city_graph[key] = value
#     return city_graph    

# def put_graph(graph):
#      print(graph)

# def bfs(graph, initial):
#     visited = []
#     queue = [initial]
#     while queue:
#         node = queue.pop(0)
#         if node not in visited:
#             visited.append(node)
#             neighbours = graph[node]
#             for neighbour in neighbours:
#                 queue.append(neighbour)
#     return visited
# graph = get_graph()
# put_graph(graph)
# initial = input('Enter initial point: ')
# bfs = bfs(graph,initial)

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

def bfs(graph, initial):
    visited = []
    queue = [initial]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

print(bfs(graph,'A'))

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

graph = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}

dfs(graph, '0')
