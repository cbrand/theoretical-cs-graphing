# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import string

from test.scnet.grapher.abstract_base_test import AbstractBaseTest

from scnet.grapher.algorithms.minimum_spanning_tree import (
    MinimumSpanningTree
)


class TestMinimumSpanningTree(AbstractBaseTest):
    """
    Tests the minimum spanning tree definition.
    """

    def test_dijkstra(self):
        """
        Tests the algorithm with giving test data into
        it.
        """
        self.nodes = self.generate_nodes(
            *[
                str(string.ascii_uppercase[i])
                for i in range(9)
            ]
        )
        self.edges = self.generate_edges(*[
            ("A", "B", 2),
            ("A", "F", 9),
            ("A", "G", 15),
            ("B", "C", 4),
            ("B", "G", 6),
            ("C", "D", 2),
            ("C", "I", 15),
            ("D", "E", 1),
            ("D", "I", 1),
            ("E", "F", 6),
            ("E", "H", 3),
            ("F", "H", 11),
            ("G", "H", 15),
            ("G", "I", 2),
            ("H", "I", 4),
        ])
        self.graph = self.prepare_graph(
            nodes=self.nodes,
            edges=self.edges,
        )
        MinimumSpanningTree(self.graph).run()
