"""Use BFS to check whether a given graph is
connected or not."""

from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end='_')  # showing traversal

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

    return visited


# Example graph
graph = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'e'],
    'c': ['a'],
    'd': ['a'],
    'e': ['b'],
    'f': []   # Uncomment to test disconnected case
}

visited = bfs(graph, 'a')

if len(visited) == len(graph):
    print(f"\nGraph is connected.\nTotal nodes: {len(graph)}, Visited nodes: {len(visited)}")
else:
    print(f"\nGraph is NOT connected.\nTotal nodes: {len(graph)}, Visited nodes: {len(visited)}")
