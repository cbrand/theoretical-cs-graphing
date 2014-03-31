# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.detection.cohesive_graph import CohesiveGraphDetection

from test.scnet.grapher.abstract_base_test import AbstractBaseTest


class TestCohesiveGraphDetection(AbstractBaseTest):
    """
    Tests if the cohesive graph detection is working as
    expected.
    """

    def test_positive_case(self):
        """
        It should say a graph is cohesive if he actually is ;)
        """
        cohesive_detection = CohesiveGraphDetection(
            self.prepare_graph(
                self.generate_nodes("1", "2", "3"),
                self.generate_edges(("1", "2"), ("3", "1"))
            )
        )
        self.assertTrue(
            cohesive_detection.detect()
        )

    def test_negative_case_no_relations(self):
        """
        It should say a graph is not cohesive if it does not have
        edges.
        """
        cohesive_detection = CohesiveGraphDetection(
            self.prepare_graph(
                self.generate_nodes("1", "2", "3"),
                []
            )
        )
        self.assertFalse(
            cohesive_detection.detect()
        )

    def test_negative_case_lonely_node(self):
        """
        It should say the graph is not cohesive if one
        node is not connected.
        """
        cohesive_detection = CohesiveGraphDetection(
            self.prepare_graph(
                self.generate_nodes("1", "2", "3", "4"),
                self.generate_edges(("1", "2"), ("3", "1"))
            )
        )
        self.assertFalse(
            cohesive_detection.detect()
        )

    def test_positive_case_no_nodes(self):
        """
        It should say the graph is cohesive if
        there are no nodes in the graph.
        """
        cohesive_detection = CohesiveGraphDetection(
            self.prepare_graph(
                [],
                []
            )
        )
        self.assertTrue(
            cohesive_detection.detect()
        )

    def test_positive_case_one_node(self):
        """
        It should say the graph is cohesive if
        there is only one node in the graph.
        """
        cohesive_detection = CohesiveGraphDetection(
            self.prepare_graph(
                self.generate_nodes('So lonely'),
                []
            )
        )
        self.assertTrue(
            cohesive_detection.detect()
        )
