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
        self.assertIn({1, 2, 3, 4, 6, 7, 8}, comps)
        self.assertIn({5}, comps)


if __name__ == '__main__':
    unittest.main()
