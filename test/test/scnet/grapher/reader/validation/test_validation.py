# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from scnet.grapher.objects import (
    EdgeStore,
    Edge,
    NodeStore,
    Node
)
from scnet.grapher.reader.validation.validator import (
    Validator
)


class TestValidation(unittest.TestCase):
    """
    Tests the Validation entry.
    """

    def setUp(self):
        self.edge_1_to_2 = Edge("NODE-1", "NODE-2")
        self.edge_2_to_1 = Edge("NODE-2", "NODE-1")
        self.node_1 = Node("NODE-1")
        self.node_2 = Node("NODE-2")

    def test_not_found_from_node(self):
        """
        It should raise an error if the node from
        this edge is not being found.
        """
        edge_store = EdgeStore([
            self.edge_1_to_2
        ])
        node_store = NodeStore([
            self.node_2
        ])
        with self.assertRaises(RuntimeError):
            Validator(
                node_store=node_store,
                edge_store=edge_store,
            ).validate()

    def test_not_found_to_node(self):
        """
        It should raise an error if the node this
        edge is going to is not being found.
        """
        edge_store = EdgeStore([
            self.edge_2_to_1
        ])
        node_store = NodeStore([
            self.node_2
        ])
        with self.assertRaises(RuntimeError):
            Validator(
                node_store=node_store,
                edge_store=edge_store,
            ).validate()

    def test_correct_validation(self):
        """
        It should parse the correct validation.
        """
        edge_store = EdgeStore([
            self.edge_1_to_2,
            self.edge_2_to_1,
        ])
        node_store = NodeStore([
            self.node_1,
            self.node_2,
        ])
        Validator(
            node_store=node_store,
            edge_store=edge_store,
        ).validate()
