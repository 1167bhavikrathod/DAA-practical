"""Write a program to implement BFS traversal of a
graph using an adjacency matrix."""

from collections import deque
def bfs(matrix,start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end=' ')
            visited.add(node)

            for i in range(len(matrix)):
                if matrix[node][i] == 1 and i not in visited:
                    queue.append(i)

matrix = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

print("bfs travarsal:")
bfs(matrix,0)