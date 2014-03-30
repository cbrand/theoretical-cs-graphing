# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from scnet.grapher.objects import (
    Edge,
    EdgeStore,
    Node,
)


class TestEdgeStore(unittest.TestCase):
    """
    Tests functionality of the edge store.
    """

    def setUp(self):
        self.edge_from_1_to_2 = Edge("NODE-1", "NODE-2", 100)
        self.edge_from_2_to_3 = Edge("NODE-2", "NODE-3", 120)
        self.edge_from_3_to_4 = Edge("NODE-3", "NODE-4", None)
        self.edge_store = EdgeStore(
            [
                self.edge_from_1_to_2,
                self.edge_from_2_to_3,
                self.edge_from_3_to_4,
            ]
        )

    def test_edges_return(self):
        """
        It should return the correct amount of edges.
        """
        self.assertEqual(
            len(self.edge_store._edges),
            3
        )

    def test_from_node(self):
        """
        It should return the correct edge definitions
        if given a node the edge should come from.
        """
        edges = self.edge_store.from_node(Node('NODE-1'))
        self.assertEqual(
            len(edges),
            1
        )
        self.assertEqual(
            edges[0],
            self.edge_from_1_to_2,
        )

    def test_to_node(self):
        """
        It should return the correct edge definitions
        if given a node the edge should go to.
        """
        edges = self.edge_store.to_node(Node('NODE-2'))
        self.assertEqual(
            len(edges),
            1
        )
        self.assertEqual(
            edges[0],
            self.edge_from_1_to_2,
        )
