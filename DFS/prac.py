def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start,end=',')

    for i in graph[start]:

        if matrix[start][i] == 1 and i not in visited:

            dfs(graph,i,visited)

