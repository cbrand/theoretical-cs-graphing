# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from scnet.grapher.objects import (
    Node,
    NodeStore,
)


class TestNodeStore(unittest.TestCase):
    """
    Tests functionality of the node store.
    """

    def setUp(self):
        self.node_1 = Node('NODE-1')
        self.node_2 = Node("NODE-2")
        self.node_store = NodeStore(
            [
                self.node_1,
                self.node_2,
            ]
        )

    def test_contains(self):
        """
        It should return True if the node name is
        in the node store.
        """
        self.assertTrue(
            "NODE-1" in self.node_store
        )

    def test_contains_negative(self):
        """
        It should return False if the node name is not
        registered with the entry.
        """
        self.assertFalse(
            "NODE-3" in self.node_store
        )

    def test_has(self):
        """
        It should return Ture if the node name is
        in the node store.
        """
        self.assertTrue(
            self.node_store.has("NODE-2")
        )

    def test_has_negative(self):
        """
        It should return False if the node name is
        not in the node store.
        """
        self.assertFalse(
            self.node_store.has("NODE-3")
        )

    def test_get(self):
        """
        It should return the node if it is requested
        by name and in the store.
        """
        node = self.node_store.get("NODE-2")
        self.assertEqual(
            node,
            self.node_2
        )

    def test_get_exception(self):
        """
        It should raise a KeyError if there is no node
        in the registry.
        """
        with self.assertRaises(KeyError):
            self.node_store.get("NODE-3")

    def test_one(self):
        """
        It should return a node when requesting one
        via the "one" function.
        """
        node = self.node_store.one()
        self.assertIsInstance(
            node,
            Node
        )
        self.assertIn(
            node.name,
            self.node_store
        )

    def test_length(self):
        """
        It should return the correct length.
        """
        self.assertEqual(
            len(self.node_store),
            2
        )
