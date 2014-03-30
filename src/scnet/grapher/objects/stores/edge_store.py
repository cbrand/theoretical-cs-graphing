# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import collections

from zope.interface import implementer

from scnet.grapher.interfaces import IEdgeStore

from scnet.grapher.objects.edge import Edge
from scnet.grapher.objects.node import Node


@implementer(IEdgeStore)
class EdgeStore(object):
    """
    Class which is being used as a global
    store for the edge entries.
    """

    def __init__(self, edges: "list[Edge]"):
        """
        Initializes the Edge Store.
        @param edges: The Edges which should be saved by the store.
        """
        self._edges = edges

    @property
    def _edges(self):
        """
        Returns the edges.
        """
        return self.__edges

    @_edges.setter
    def _edges(self, value: "list[Edge]"):
        """
        Sets the Edges which should be stored.
        """
        self._from_nodes = collections.defaultdict(list)
        self._to_nodes = collections.defaultdict(list)

        for edge in value:
            lists = (
                self._from_nodes[edge.from_node_name],
                self._to_nodes[edge.to_node_name],
            )
            for to_add in lists:
                to_add.append(edge)

        self.__edges = value

    def __iter__(self):
        """
        Returns an iterator through all edges registered in this
        edge store.
        """
        return self._edges.__iter__()

    def from_node_name(self, node_name: str) -> list:
        """
        Queries all Edge configuraitosn which start
        from the node with the given node name.
        @rtype: list[Edge]
        """
        return self._from_nodes[node_name]

    def from_node(self, node: Node) -> list:
        """
        Queries all Edge configurations which is
        from the given node entry.
        @rtype: list[Edge]
        """
        return self.from_node_name(node_name=node.name)

    def to_node_name(self, node_name: str) -> list:
        """
        Queries all Edge configurations which are
        ending in the node with the given name entry.
        @rtype: list[Edge]
        """
        return self._to_nodes[node_name]

    def to_node(self, node: Node) -> list:
        """
        Queries all Edge configurations which
        are ending in the given node entry.
        @rtype: list[Edge]
        """
        return self.to_node_name(node_name=node.name)
