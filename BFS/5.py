"""Implement BFS on a real-world problem (e.g.,
finding the shortest route between cities)."""

from collections import deque

def bfs_shortest_route(graph, start, goal):
    # queue stores paths instead of just nodes
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        city = path[-1]

        if city == goal:
            return path  # shortest route found

        for neighbor in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # if no route exists


# Real-world example graph (cities + roads)
city_graph = {
    "Mumbai": ["Pune", "Surat"],
    "Pune": ["Mumbai", "Nashik"],
    "Surat": ["Mumbai", "Vadodara"],
    "Nashik": ["Pune", "Indore"],
    "Vadodara": ["Surat", "Ahmedabad"],
    "Indore": ["Nashik", "Bhopal"],
    "Ahmedabad": ["Vadodara"],
    "Bhopal": ["Indore"]
}

start_city = "Mumbai"
goal_city = "Bhopal"

route = bfs_shortest_route(city_graph, start_city, goal_city)

if route:
    print(f"Shortest route from {start_city} to {goal_city}: {', '.join(route)}")
else:
    print(f"No route found between {start_city} and {goal_city}")
