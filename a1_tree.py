class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree():
    print("Enter the elements of the tree separated by spaces (use -1 for null nodes):")
    elements = list(map(int, input().split()))
    if not elements:
        return None
    root = TreeNode(elements[0])
    queue = [root]
    i = 1
    while queue and i < len(elements):
        current = queue.pop(0)
        if elements[i] != -1:
            child = TreeNode(elements[i])
            current.children.append(child)
            queue.append(child)
        i += 1
        if i < len(elements) and elements[i] != -1:
            child = TreeNode(elements[i])
            current.children.append(child)
            queue.append(child)
        i += 1
    return root

def bfs(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")
        for child in node.children:
            queue.append(child)

def dfs(root):
    if not root:
        return
    print(root.value, end=" ")
    for child in root.children:
        dfs(child)

if __name__ == "__main__":
    root = build_tree()
    print("\nBFS Traversal:")
    bfs(root)
    print("\nDFS Traversal:")
    dfs(root)
