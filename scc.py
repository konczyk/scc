from collections import defaultdict


class SCC:
    """
    Compute strongly connected components of a directed graph using
    Kosaraju's algorithm
    """

    def __init__(self, graph):
        """
        Init data structures and run the computation
        """

        self._graph = graph
        self._components = defaultdict(set)
        self._compute()

    def _compute(self):
        """
        Compute the components by running two Depth-first searches
        """

        sorted_vertices = self._finish_times()

        self._graph.reverse()
        marked = set()
        for v in reversed(sorted_vertices):
            if v not in marked:
                self._components[v].update([u for u in self._dfs(v, marked)])

    def _finish_times(self):
        """
        Run iterative Depth First Search to find out the finish time
        to find each vertex
        """

        marked, finished = set(), []
        for k in list(self._graph.vertices()):
            if k not in marked:
                finished.extend([v for v in self._dfs(k, marked)])

        return finished

    def _dfs(self, source, marked):
        stack, popped = [source], set()
        while stack:
            vertex = stack[-1]
            to_visit = self._graph.edges(vertex) - marked
            if vertex not in marked:
                marked.add(vertex)
                stack.extend(to_visit)
            if not to_visit:
                stack.pop()
                if vertex not in popped:
                    popped.add(vertex)
                    yield vertex

    def components(self):
        """
        Return found components
        """

        return self._components.values()

    def sizes(self, n=None):
        """
        Return sorted sizes of found components
        """

        num = n or len(self._components)
        return sorted([len(v) for v in self.components()], reverse=True)[0:num]

