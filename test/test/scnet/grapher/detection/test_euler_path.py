# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.detection.euler_path import EulerPathDetection

from test.scnet.grapher.abstract_base_test import AbstractBaseTest


class TestEulerCycleDetection(AbstractBaseTest):
    """
    Tests if the euler path detection is working as
    expected.
    """

    def check(self, graph):
        """
        Checks the given graph and returns the result.
        """
        return EulerPathDetection(graph).detect()

    def test_positive_case(self):
        """
        It should say that the graph has an euler cycle if
        the correct data is given.
        """
        self.assertTrue(
            self.check(
                self.prepare_graph(
                    nodes=self.generate_nodes(
                        "1", "2", "3"
                    ),
                    edges=self.generate_edges(
                        ("1", "2"),
                        ("2", "3"),
                        ("3", "1")
                    )
                )
            )
        )

    def test_positive_case_two_uneven(self):
        """
        It should return True if there are exactly
        2 nodes with odd number of edges in the graph.
        """
        self.assertTrue(
            self.check(
                self.prepare_graph(
                    nodes=self.generate_nodes(
                        "1", "2", "3", "4"
                    ),
                    edges=self.generate_edges(
                        ("1", "2"),
                        ("2", "3"),
                        ("3", "1"),
                        ("3", "4"),
                    )
                )
            )
        )

    def test_positive_case_one_edge(self):
        """
        It should return True if there is one edge in
        the whole graph
        """
        self.assertTrue(
            self.check(
                self.prepare_graph(
                    nodes=self.generate_nodes(
                        "1", "2"
                    ),
                    edges=self.generate_edges(
                        ("1", "2"),
                    )
                )
            )
        )

    def test_negative_case_multiple_odds(self):
        """
        It should return False if it is a graph with more than
        two nodes which have uneven edges.
        """
        self.assertFalse(
            self.check(
                self.prepare_graph(
                    nodes=self.generate_nodes(
                        "1", "2", "3", "4", "5"
                    ),
                    edges=self.generate_edges(
                        ("1", "2"),
                        ("2", "3"),
                        ("3", "1"),
                        ("3", "4"),
                        ("1", "5"),
                    )
                )
            )
        )

    def test_negative_case_lonely_node(self):
        """
        It should return false if there is a lonely node
        in the graph.
        """
        self.assertFalse(
            self.check(
                self.prepare_graph(
                    nodes=self.generate_nodes(
                        "1", "2", "3", "4"
                    ),
                    edges=self.generate_edges(
                        ("1", "2"),
                        ("2", "3"),
                        ("3", "1")
                    )
                )
            )
        )
