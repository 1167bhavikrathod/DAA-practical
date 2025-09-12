"""Write a program to implement DFS traversal of a
graph using an adjacency matrix."""
def dfs(matrix,start,visited=None):
    if visited is None:
        visited = set()
    # print(start , end='_')
    visited.add(start)
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and i not in visited:
            print(f"from {start} to {i}")
            dfs(matrix,i,visited)
            print(f"from {i} to {start}")

graph_matrix = [
    [0, 1, 1, 0, 0],  
    [1, 0, 0, 1, 1],  
    [1, 0, 0, 0, 0],  
    [0, 1, 0, 0, 0],  
    [0, 1, 0, 0, 0]   
]
print("DFS Traversal:")
dfs(graph_matrix, 0)