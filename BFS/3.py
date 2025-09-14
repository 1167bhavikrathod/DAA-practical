"""3. Apply BFS to find the shortest path between two
nodes in an unweighted graph."""

from collections import deque

def bfs(graph,start,goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                new_path = list(path)
                new_path.append(i)
                queue.append(new_path)


if __name__ == "__main__":
    graph = {
        0 : [1 , 2],
        1 : [0 , 3 , 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }

    start, goal = 0, 5
    print("Shortest path from", start, "to", goal, ":", bfs(graph, start, goal))


        

