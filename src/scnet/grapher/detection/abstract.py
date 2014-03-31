# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.interfaces.graph import IGraph
from scnet.grapher.interfaces.node_store import INodeStore
from scnet.grapher.interfaces.edge_store import IEdgeStore


class AbstractDetection(object):
    """
    Abstract object which has functions
    to be used in graph detection algorithms.
    """

    def __init__(self, graph: IGraph):
        self.graph = graph

    @property
    def _node_store(self) -> INodeStore:
        return self.graph.node_store

    @property
    def _edge_store(self) -> IEdgeStore:
        return self.graph.edge_store
