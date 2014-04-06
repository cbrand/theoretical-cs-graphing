# -*- encoding: utf-8 -*-
"""
"""

from __future__ import unicode_literals

import unittest

from scnet.grapher.generator import generate_edges
from scnet.grapher.interfaces.edge import IEdge


class TestGenerator(unittest.TestCase):
    """
    Tests the generator functionality.
    """

    def test_edge_creation(self):
        """
        It should generate an edge creation correctly.
        """
        edges = list(generate_edges(('A', 'B')))
        self.assertEqual(
            len(edges),
            1
        )
        edge = edges[0]
        """:type: IEdge"""
        self.assertTrue(
            IEdge.providedBy(edge)
        )
        self.assertEqual(
            edge.from_node_name,
            'A'
        )
        self.assertEqual(
            edge.to_node_name,
            'B'
        )
        self.assertIsNone(
            edge.weight
        )

    def test_edge_weight_creation(self):
        """
        It should generate an edge with a given weight
        correctly.
        """
        edges = list(generate_edges(('D', 'C', '100')))
        edge = edges[0]
        self.assertEqual(
            edge.from_node_name,
            'D'
        )
        self.assertEqual(
            edge.to_node_name,
            'C'
        )
        self.assertEqual(
            edge.weight,
            100
        )

    def test_edge_weight_none(self):
        """
        It should accept None as third argument.
        """
        edges = list(generate_edges(('D', 'C', None)))
        edge = edges[0]
        self.assertIsNone(edge.weight)
