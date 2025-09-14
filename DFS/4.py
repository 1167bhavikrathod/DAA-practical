"""4. Apply DFS to check whether a graph is connected
or not."""
count = 1
def dfs(graph,start,visited=None):
    global count
    if visited is None:
        visited = set()
    print(start , end='_')
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            count += 1

graph = {
    'a' : ['b','c','d'],
    'b' : ['a','e'],
    'c' : ['a'],
    'd' : ['a'],
    'e' : ['b']
    # 'f' : []
}

dfs(graph,'a')

if(len(graph) != count):
    print(f"\nthe graph is not connected.\ntotal nodes:{len(graph)}, visited node:{count}")
else:
    print(f"\ngraph is connected.\ntotal nodes:{len(graph)}, visited node:{count}")
            


