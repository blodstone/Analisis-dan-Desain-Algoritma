from migraph import MiGraph

def prims(graph, starting):
    vtx = graph.vertices()

    q = dict()
    for v in vtx:
        q[v] = 99999

    q[vtx[starting]] = 0

    t = dict()
    t[vtx[starting]] = None

    while q:
        min_v = min(q, key=q.get)
        adj_v = graph.get_neighbour(min_v)

        for v in adj_v:
            w = graph.get_neighbour_weight(min_v, v)
            if v in q and w < q[v]:
                t[v] = min_v
                q[v] = w
        
        q.pop(min_v)

    result = MiGraph()
    for key, val in t.items():
        if val is not None:
            result.add_vertices([key, val])
            result.add_edge((key, val, graph.get_neighbour_weight(key, val)))
            
    return result

def kruskal(graph):
    parent = dict()
    rank = dict()

    def make_set(vertice):
        parent[vertice] = vertice
        rank[vertice] = 0

    def find(vertice):
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(vertice1, vertice2):
        root1 = find(vertice1)
        root2 = find(vertice2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]: rank[root2] += 1

    for vertex in graph.vertices():
        make_set(vertex)

    mst = set()
    edges = graph.edges_with_weight()
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        v1, v2, w = edge
        if find(v1) != find(v2):
            union(v1, v2)
            mst.add(edge)

    return mst

