from collections import defaultdict


class Graph:
    """
    Directed graph data structure represented as an adjacency list with both
    incoming and outgoing edges
    """

    def __init__(self, data):
        self._v = 0
        self._graph = defaultdict(set)
        self._load_data(data)

    def _load_data(self, data):
        """
        Load connections from the data, where each row represents a tuple of
        a vertex and an outgoing edge
        """

        for line in data:
            vertex, edge = [int(i) for i in line.split()]
            self._graph[vertex].add(edge)

    def vertices(self):
        """
        Return the iterator over vertices
        """

        return self._graph.keys()

    def edges(self, vertex):
        """
        Return the set of edges of the given vertex
        """

        return self._graph[vertex]

    def reverse(self):
        """
        Reverse the graph in-place
        """
        reversed_graph = defaultdict(set)
        while len(self._graph) > 0:
            vertex, edges = self._graph.popitem()
            for edge in edges:
                reversed_graph[edge].add(vertex)
        self._graph = reversed_graph
