import heapq


class Node: 
    def __init__(self, state, parent=None, cost=0, heuristic=0): 
        self.state = state 
        self.parent = parent 
        self.cost = cost 
        self.heuristic = heuristic 
        
    def total_cost(self): 
        return self.cost + self.heuristic 

    # Define comparison operators 
    def __lt__(self, other): 
        return self.total_cost() < other.total_cost() 

    def __eq__(self, other): 
        return self.state == other.state 

def astar(start_state, goal_state, heuristic_func, neighbors_func): 
    start_node = Node(start_state, cost=0, heuristic=heuristic_func(start_state)) 
    frontier = [(start_node.total_cost(), start_node)] 
    explored = set() 
    
    while frontier: 
        current_node = heapq.heappop(frontier)[1] 
        if current_node.state == goal_state: 
            return construct_path(current_node) 
        explored.add(current_node.state) 
        for neighbor_state, step_cost in neighbors_func(current_node.state): 
            if neighbor_state not in explored: 
                neighbor_node = Node(neighbor_state, parent=current_node, cost=current_node.cost + step_cost,  
                                     heuristic=heuristic_func(neighbor_state)) 
                heapq.heappush(frontier, (neighbor_node.total_cost(), neighbor_node)) 
    return None # No path found 

def construct_path(node): 
    path = [] 
    current = node 
    while current: 
        path.append(current.state) 
        current = current.parent 
    return list(reversed(path)) 

# Example usage: 
# Define a heuristic function 
def manhattan_distance(state): 
    # Assuming state is a tuple of (x, y) coordinates 
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1]) 

# Define a function to generate neighboring states and their costs 
def get_neighbors(state): 
    x, y = state 
    neighbors = [] 
    # Assuming 4-connected grid 
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
        new_x, new_y = x + dx, y + dy 
        if 0 <= new_x < width and 0 <= new_y < height: 
            neighbors.append(((new_x, new_y), 1)) # Assuming uniform cost for each step 
    return neighbors 

start_state = (0, 0) 
goal_state = (5, 5) 
width = 10 
height = 10 

path = astar(start_state, goal_state, manhattan_distance, get_neighbors) 
if path: 
    print("Path found:", path) 
else: 
    print("No path found") 
