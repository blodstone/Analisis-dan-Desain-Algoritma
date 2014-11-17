class MiGraph(object):
    __ADD_EDGE_ERROR ="""
    The edge parameter should be a tuple 
    with 3 elements: vertex1, vertex2, 
    and weight
    """

    __GET_WEIGHT_ERROR = """
    There is no edge from {0} to {1}
    """

    __GET_NEIGHBOUR_ERROR = """
    No vertex {0} in graph.
    """

    def __init__(self, adj_list = {}):
        self.__adj_list = adj_list

    def vertices(self):
        return sorted(list(self.__adj_list.keys()))

    def edges(self):
        e = []
        for vertex in self.__adj_list:
            for neighbour in self.__adj_list[vertex]:
                edge = {neighbour, vertex}
                if edge not in e:
                    e.append(edge)

        return e

    def is_adjacent(self, v1, v2):
        return v2 in self.__adj_list[v1]

    def add_vertex(self, vertex):
        if vertex not in self.__adj_list:
            self.__adj_list[vertex] = {}

    def add_vertices(self, vertices):
        for vertex in vertices:
            self.add_vertex(vertex)

    def add_edge(self, edge):
        if len(edge) != 3:
            raise ValueError(self.__ADD_EDGE_ERROR)

        (v1, v2, w) = tuple(edge)

        if v1 in self.vertices():
            self.__adj_list[v1][v2] = w
        else:
            self.__adj_list[v1] = {v2: w}

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def get_neighbour(self, vertex):
        if vertex in self.vertices():
            return sorted(list(self.__adj_list[vertex].keys()))

        raise ValueError(self.__GET_NEIGHBOUR_ERROR.format(vertex))

    def get_neighbour_weight(self, v1, v2):
        if {v1, v2} in self.edges():
            return self.__adj_list[v1][v2]

        raise ValueError(self.__GET_WEIGHT_ERROR.format(v1, v2))

    def remove_vertex(self, vertex):
        self.__adj_list.pop(vertex, None)

        for v in self.__adj_list:
            if vertex in v:
                v.pop(vertex)

    def remove_edge(self, v1, v2):
        return self.__adj_list[v1].pop(v2, None)

