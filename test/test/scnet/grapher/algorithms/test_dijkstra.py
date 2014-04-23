# -*- encoding: utf-8 -*-

import string

from scnet.grapher.algorithms.dijkstra_algorithm import \
    DijkstraAlgorithm

from test.scnet.grapher.abstract_base_test import AbstractBaseTest


class TestDijkstra(AbstractBaseTest):
    """
    Tests the implementation of the dijkstra
    algorithm.
    """

    def setUp(self):
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
        super().setUp()

    def test_input(self):
        """
        It should find the smallest way in a linear
        graph.
        """
        self.nodes = self.generate_nodes(
            "A",
            "B",
            "C",
        )
        self.edges = self.generate_edges(
            ("A", "B", 100),
            ("B", "C", 200),
        )
        self.graph = self.prepare_graph(
            self.nodes,
            self.edges,
        )
        result = DijkstraAlgorithm(
            self.graph,
            from_node="A",
            to_node="C",
        ).run()
        self.assertEqual(
            [node.name for node in result],
            ["A", "B", "C"]
        )

    def test_dijkstra_txt(self):
        """
        It should parse the dijkstra txt file correctly.
        """
        algorithm = DijkstraAlgorithm(
            self.graph,
            from_node='A',
            to_node='D',
        )
        self.assertEqual(
            [node.name for node in algorithm.run()],
            ['A', 'B', 'C', 'D']
        )

