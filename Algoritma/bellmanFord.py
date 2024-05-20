def bellman_ford(graph, start):
    distance = {v: float('infinity') for v in graph}
    distance[start] = 0
    for _ in range(len(graph) - 1):
        for v in graph:
            for w in graph[v]:
                if distance[v] + graph[v][w] < distance[w]:
                    distance[w] = distance[v] + graph[v][w]
    for v in graph:
        for w in graph[v]:
            if distance[v] + graph[v][w] < distance[w]:
                return "Negative cycle detected"
    return distance

graph = {'A': {'B': -1, 'C': 4},
         'B': {'C': 3, 'D': 2, 'E': 2},
         'C': {},
         'D': {'B': 1, 'C': 5},
         'E': {'D': -3}}
print(bellman_ford(graph, 'A'))
