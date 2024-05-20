def kruskal(graph):
    mst = []
    parent = {v: v for v in graph}
    edges = [(graph[u][v], u, v) for u in graph for v in graph[u]]
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        while u != parent[u]:
            u = parent[u]
        while v != parent[v]:
            v = parent[v]
        if u != v:
            mst.append((u, v, weight))
            parent[v] = u
    return mst

graph = {'A': {'B': 2, 'C': 3},
         'B': {'A': 2, 'C': 1, 'D': 1},
         'C': {'A': 3, 'B': 1, 'D': 4},
         'D': {'B': 1, 'C': 4}}
print(kruskal(graph))
