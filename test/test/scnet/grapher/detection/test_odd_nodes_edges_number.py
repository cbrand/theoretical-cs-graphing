# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.detection.odd_nodes_edges_number import (
    OddNodeEdgesNumberDetection
)

from test.scnet.grapher.abstract_base_test import AbstractBaseTest


class TestOddNodeEdgesNumberDetection(AbstractBaseTest):
    """
    Tests if the odd nodes detection is working as
    expected.
    """

    def test_positive_case(self):
        """
        It should say that the graph has an odd amount of
        edges on his nodes when this is the case.
        """
        odd_node_detection = OddNodeEdgesNumberDetection(
            self.prepare_graph(
                self.generate_nodes("1", "2", "3"),
                self.generate_edges(("1", "2"), ("3", "1"))
            )
        )
        self.assertTrue(
            odd_node_detection.detect()
        )

    def test_negative_case(self):
        """
        It should say the graph has no odd amount of edges on a
        node when there are only even ones.
        """
        odd_node_detection = OddNodeEdgesNumberDetection(
            self.prepare_graph(
                self.generate_nodes("1", "2", "3"),
                self.generate_edges(("1", "2"), ("2", "3"), ("3", "1"))
            )
        )
        self.assertFalse(
            odd_node_detection.detect()
        )

    def test_negative_case_no_relations(self):
        """
        It should say it has no odd edges when there
        are no edges at all.
        """
        odd_node_detection = OddNodeEdgesNumberDetection(
            self.prepare_graph(
                self.generate_nodes("1", "2", "3"),
                []
            )
        )
        self.assertFalse(
            odd_node_detection.detect()
        )

    def test_negative_case_no_nodes(self):
        """
        It should say the graph has no odd edges
        when there are no edges and graphs at all.
        """
        odd_node_detection = OddNodeEdgesNumberDetection(
            self.prepare_graph(
                [],
                []
            )
        )
        self.assertFalse(
            odd_node_detection.detect()
        )
