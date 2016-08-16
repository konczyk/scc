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

    def test_out_edges(self):
        graph = Graph(self.data)

        self.assertSetEqual(graph.out_edges(0), {1})
        self.assertSetEqual(graph.out_edges(1), {2})
        self.assertSetEqual(graph.out_edges(2), set())
        self.assertSetEqual(graph.out_edges(3), {0, 4})
        self.assertSetEqual(graph.out_edges(4), {1, 5})
        self.assertSetEqual(graph.out_edges(5), set())

    def test_in_edges(self):
        graph = Graph(self.data)

        self.assertSetEqual(graph.in_edges(0), {3})
        self.assertSetEqual(graph.in_edges(1), {0, 4})
        self.assertSetEqual(graph.in_edges(2), {1})
        self.assertSetEqual(graph.in_edges(3), set())
        self.assertSetEqual(graph.in_edges(4), {3})
        self.assertSetEqual(graph.in_edges(5), {4})


if __name__ == '__main__':
    unittest.main()
