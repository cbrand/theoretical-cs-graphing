# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from scnet.grapher.objects import (
    EdgeStore,
    NodeStore,
    Edge,
    Node,
)

from test.scnet.grapher.abstract_base_test import AbstractBaseTest


class TestEdge(AbstractBaseTest):
    """
    Tests the Edge object.
    """

    def setUp(self):
        self.edges = [
            Edge('Node1', 'Node2'),
            Edge('Node2', 'Node3'),
            Edge('Node3', 'Node1'),
        ]
        self.nodes = [
            Node('Node1'),
            Node('Node2'),
            Node('Node3'),
        ]
        self.prepare_graph(
            nodes=self.nodes,
            edges=self.edges,
        )

    def test_edges_access(self):
        """
        It should return all edges of a node
        when requesting them via "edges" regardless
        if they originate or end in the node.
        """
        node1 = self.nodes[0]
        edges = node1.edges
        self.assertEqual(
            len(edges),
            2
        )
        self.assertIn(
            self.edges[0],
            edges
        )
        self.assertIn(
            self.edges[2],
            edges
        )

    def test_parent_node_access(self):
        """
        IT should return all nodes the given node is a child of.
        """
        node1 = self.nodes[0]
        parent_nodes = tuple(node1.parent_nodes)
        self.assertEqual(
            len(parent_nodes),
            1
        )
        self.assertEqual(
            parent_nodes[0],
            self.nodes[2]
        )
    
    def test_child_node_access(self):
        """
        It should return all nodes the given node is a parent of.
        """
        node1 = self.nodes[0]
        child_nodes = tuple(node1.child_nodes)
        self.assertEqual(
            len(child_nodes),
            1
        )
        self.assertEqual(
            child_nodes[0],
            self.nodes[1]
        )

    def test_neighbors_access(self):
        """
        Es sollte alle Nachbarn über die Neighbors Funktion
        zurück geben.
        """
        node1 = self.nodes[0]
        neighbors = tuple(node1.neighbors)
        self.assertEqual(
            len(neighbors),
            2
        )
        self.assertIn(
            self.nodes[1],
            neighbors,
        )
        self.assertIn(
            self.nodes[2],
            neighbors,
        )
