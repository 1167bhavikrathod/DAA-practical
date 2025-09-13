"""Implement DFS traversal of a graph using an
adjacency list and display the order of visited
nodes."""
def dfs(matrix,start,visited=None):
    if visited is None:
        visited = set()
    print(start,end = ' ')
    visited.add(start)
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and i not in visited:
                dfs(matrix,i,visited)

matrix = [
    [0, 1, 1, 0, 0],  
    [1, 0, 0, 1, 1],  
    [1, 0, 0, 0, 0],  
    [0, 1, 0, 0, 0],  
    [0, 1, 0, 0, 0]   
]

print("dfs travarsal:")
dfs(matrix,0)