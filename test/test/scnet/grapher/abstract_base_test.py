# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest
from scnet.grapher.generator import (
    generate_graph,
    generate_edges,
    generate_nodes,
)

from scnet.grapher.objects import (
    Graph,
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
        return list(generate_nodes(*node_names))

    def generate_edges(self, *edge_defs: tuple) -> iter:
        """
        Generates out of the given tuple definitions
        Edge objects and returns them.
        """
        return list(generate_edges(*edge_defs))

    def prepare_graph(self, nodes, edges) -> Graph:
        """
        Adds a store in the data structures and
        returns a configuration object of it.
        Also sets several data structures as
        instance variables for accessibility
        purposes.
        """
        return generate_graph(nodes, edges)
