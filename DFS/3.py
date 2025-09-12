# DFS using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # to keep track of visited nodes
    
    # print(start, end=" ")  # Process the current node
    visited.add(start)

    # Visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            print(f"from {start} to {neighbor}")
            dfs(graph, neighbor, visited)
            print(f"from {neighbor} to {start}")


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

print("DFS Traversal:")
dfs(graph, 'A')
