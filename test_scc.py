import unittest
from graph import Graph
from scc import SCC


class SCCTest(unittest.TestCase):
    data = [
        '1 2',
        '2 3',
        '3 1',
        '3 4',
        '5 4',
        '6 4',
        '8 6',
        '6 7',
        '7 8',
        '4 3',
        '4 6'
    ]

    def test_components(self):
        scc = SCC(Graph(self.data))

        comps = scc.components()

        self.assertEqual(len(comps), 2)
        self.assertEquals({1, 2, 3, 4, 6, 7, 8}, comps[0])
        self.assertEquals({5}, comps[1])

    def test_sizes(self):
        scc = SCC(Graph(self.data))

        sizes = scc.sizes()

        self.assertEqual(len(sizes), 2)
        self.assertEquals(7, sizes[0])
        self.assertEquals(1, sizes[1])


if __name__ == '__main__':
    unittest.main()
