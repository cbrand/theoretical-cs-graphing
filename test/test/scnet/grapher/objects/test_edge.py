# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from scnet.grapher.objects import (
    EdgeStore,
    NodeStore,
    Edge,
    Node,
)


class TestEdge(unittest.TestCase):
    """
    Tests the Edge object.
    """

    def setUp(self):
        self.edge = Edge('FromNode', 'ToNode')
        self.edge.edge_store = EdgeStore([self.edge])
        self.edge.node_store = NodeStore([
            Node('FromNode'),
            Node('ToNode')
        ])

    def test_access_node_from(self):
        """
        It should support the access of the node this
        edge is starting from.
        """
        self.assertIsInstance(
            self.edge.from_node,
            Node
        )
        self.assertEqual(
            self.edge.from_node.name,
            'FromNode'
        )

    def test_access_node_to(self):
        """
        It should support the access to the node this
        edge is ending at.
        """
        self.assertIsInstance(
            self.edge.to_node,
            Node
        )
        self.assertEqual(
            self.edge.to_node.name,
            'ToNode'
        )
