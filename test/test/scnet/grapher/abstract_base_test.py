# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from scnet.grapher.objects import (
    Graph,
    NodeStore,
    EdgeStore,
    Node,
    Edge,
)


class AbstractBaseTest(unittest.TestCase):
    """
    Abstract Test which has some helper functions
    needed in several test case scenarios.
    """

    def generate_nodes(self, *node_names: str) -> iter:
        """
        Generates out of the given node names a list
        of node objects and returns it.
        """
        return (
            Node(node_name)
            for node_name in node_names
        )

    def generate_edges(self, *edge_defs: tuple) -> iter:
        """
        Generates out of the given tuple definitions
        Edge objects and returns them.
        """
        for edge_def in edge_defs:
            edge_def_length = len(edge_def)
            if edge_def_length == 2:
                yield Edge(*edge_def)
            else:
                from_node = edge_def[0]
                to_node = edge_def[1]
                if edge_def[2] is None:
                    weight = None
                else:
                    weight = int(edge_def[2])
                yield Edge(
                    from_node,
                    to_node,
                    weight,
                )

    def assign_stores(self, abstract_obj):
        """
        Assigns the stores for a given entry.
        """
        abstract_obj.node_store = self.node_store
        abstract_obj.edge_store = self.edge_store

    def prepare_graph(self, nodes, edges) -> Graph:
        """
        Adds a store in the data structures and
        returns a configuration object of it.
        Also sets several data structures as
        instance variables for accessibility
        purposes.
        """
        if not isinstance(nodes, list):
            nodes = list(nodes)
        if not isinstance(edges, list):
            edges = list(edges)

        self.node_store = NodeStore(nodes)
        self.edge_store = EdgeStore(edges)

        for node in nodes:
            self.assign_stores(node)
        for edge in edges:
            self.assign_stores(edge)
        self.graph = Graph(
            node_store=self.node_store,
            edge_store=self.edge_store,
        )
        return self.graph
