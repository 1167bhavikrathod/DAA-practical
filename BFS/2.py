"""Implement BFS traversal of a graph using an
adjacency list and display the order of visited
nodes."""

from collections import deque
def bfs(graph,start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end=' ')
            visited.add(node)

            for i in graph[node]:
                if i not in visited:
                    queue.append(i)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

print("bfs travarsal:")
bfs(graph,'A')
            