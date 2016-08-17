import unittest
from graph import Graph


class GraphTest(unittest.TestCase):
    """
    0 --> 1 --> 2
    ^     ^
    |     |
    3 --> 4 --> 5
    """
    data = [
        '0 1',
        '1 2',
        '3 0',
        '3 4',
        '4 1',
        '4 5'
    ]

    def test_edges(self):
        graph = Graph(self.data)

        self.assertSetEqual(graph.edges(0), {1})
        self.assertSetEqual(graph.edges(1), {2})
        self.assertSetEqual(graph.edges(2), set())
        self.assertSetEqual(graph.edges(3), {0, 4})
        self.assertSetEqual(graph.edges(4), {1, 5})
        self.assertSetEqual(graph.edges(5), set())

    def test_reversed_edges(self):
        graph = Graph(self.data)
        graph.reverse()

        self.assertSetEqual(graph.edges(0), {3})
        self.assertSetEqual(graph.edges(1), {0, 4})
        self.assertSetEqual(graph.edges(2), {1})
        self.assertSetEqual(graph.edges(3), set())
        self.assertSetEqual(graph.edges(4), {3})
        self.assertSetEqual(graph.edges(5), {4})

    def test_vertices(self):
        graph = Graph(self.data)

        self.assertEqual(sorted(graph.vertices()), [0, 1, 3, 4])


if __name__ == '__main__':
    unittest.main()
