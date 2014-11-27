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
