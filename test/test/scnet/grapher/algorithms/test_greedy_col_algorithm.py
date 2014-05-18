# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import string

from test.scnet.grapher.abstract_base_test import AbstractBaseTest

from scnet.grapher.algorithms.greedy_col_algorithm import GreedyColAlgorithm


class TestGreedyColAlgorithm(AbstractBaseTest):
    """
    Tests the minimum spanning tree definition.
    """

    def test_greedy_col(self):
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
        graph = GreedyColAlgorithm(self.graph).run()
        data = set(node.color for node in graph.node_store)
        self.assertLessEqual(
            len(data),
            4
        )

    def test_minimum_with_set(self):
        """
        It should also be able to extract
        the minimum from a python set with
        integers in it.
        """
        self.assertEqual(
            GreedyColAlgorithm.possible_minimum(set(range(0, 211))),
            211
        )
