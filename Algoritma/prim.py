import heapq

def prim(graph):
    mst = []
    visited = set()
    start = list(graph.keys())[0]
    queue = [(0, start, None)]
    while queue:
        cost, current, prev = heapq.heappop(queue)
        if current not in visited:
            visited.add(current)
            if prev:
                mst.append((prev, current, cost))
            for neighbor, weight in graph[current].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (weight, neighbor, current))
    return mst

graph = {'A': {'B': 2, 'C': 3},
         'B': {'A': 2, 'C': 1, 'D': 1},
         'C': {'A': 3, 'B': 1, 'D': 4},
         'D': {'B': 1, 'C': 4}}
print(prim(graph))
