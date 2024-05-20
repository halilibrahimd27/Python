import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

graph = {'A': {'B': 1, 'C': 4},
         'B': {'A': 1, 'D': 2, 'E': 5},
         'C': {'A': 4, 'F': 6},
         'D': {'B': 2},
         'E': {'B': 5, 'F': 1},
         'F': {'C': 6, 'E': 1}}
print(dijkstra(graph, 'A'))
