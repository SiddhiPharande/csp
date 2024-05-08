def print_conf(color_array) :
    print("Assigned colors:")
    for i in range(4):
        print("Vertex: ",i, " Color: ",color_array[i])

def is_safe(graph, color_array):
    for i in range(4):
        for j in range(i+1, 4):
            if(graph[i][j] and color_array[i] == color_array[j]):
                return False
    return True

def graph_coloring_algo(graph, m, i, color_array):
    if(i==4):
        if(is_safe(graph, color_array)):
            print_conf(color_array)
            return True
        return False
    for j in range(1, m+1):
        color_array[i] = j
        if (graph_coloring_algo(graph, m, i+1, color_array)):
            return True
        color_array[i] = 0
    return False

if __name__ == '__main__':
    graph = [
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,1],
        [1,0,1,0],
    ]
    m = 3

    color_array = [0 for i in range(4)]

    if(graph_coloring_algo(graph, m, 0, color_array)):
        print("Coloring possible!")
    else:
        print("Not possible!")