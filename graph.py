from collections import defaultdict


class Graph:
    """
    Directed graph data structure represented as an adjacency list with both
    incoming and outgoing edges
    """

    def __init__(self, data):
        self._v = 0
        self._graph = defaultdict(lambda: defaultdict(set))
        self._load_data(data)

    def _load_data(self, data):
        """
        Load connections from the data, where each row represents a tuple of
        a vertex and an outgoing edge
        """

        for line in data:
            vertex, out_edge = [int(i) for i in line.split()]
            self._add_edge(vertex, 'out', out_edge)
            self._add_edge(out_edge, 'in', vertex)

    def _add_edge(self, vertex, edge_type, edge):
        self._graph[vertex][edge_type].add(edge)

    def out_edges(self, vertex):
        return self._graph[vertex]['out']

    def in_edges(self, vertex):
        return self._graph[vertex]['in']
