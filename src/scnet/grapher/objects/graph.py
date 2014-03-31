# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import implementer

from scnet.grapher.interfaces import IGraph


@implementer(IGraph)
class Graph(object):
    """
    Representation of a graph.
    """

    def __init__(
            self,
            node_store,
            edge_store
    ):
        self.node_store = node_store
        self.edge_store = edge_store
