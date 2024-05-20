def floyd_warshall(graph):
    distance = {v: {w: float('infinity') for w in graph} for v in graph}
    for v in graph:
        distance[v][v] = 0
    for v in graph:
        for w in graph[v]:
            distance[v][w] = graph[v][w]
    for k in graph:
        for v in graph:
            for w in graph:
                distance[v][w] = min(distance[v][w], distance[v][k] + distance[k][w])
    return distance

graph = {'A': {'B': 3, 'C': 8},
         'B': {'A': 2, 'C': 1},
         'C': {'A': 4, 'B': 7}}
print(floyd_warshall(graph))
