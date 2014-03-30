# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import Interface


class IEdgeStore(Interface):
    """
    Interface which is being used as a global
    store for the edge entries.
    """

    def from_node_name(self, node_name: str) -> list:
        """
        Queries all Edge configuraitosn which start
        from the node with the given node name.
        @rtype: list[Edge]
        """

    def from_node(self, node: "Node") -> list:
        """
        Queries all Edge configurations which is
        from the given node entry.
        @rtype: list[Edge]
        """

    def to_node_name(self, node_name: str) -> list:
        """
        Queries all Edge configurations which are
        ending in the node with the given name entry.
        @rtype: list[Edge]
        """

    def to_node(self, node: "Node") -> list:
        """
        Queries all Edge configurations which
        are ending in the given node entry.
        @rtype: list[Edge]
        """

    def __iter__(self):
        """
        Returns an iterator through all edges registered in this
        edge store.
        """
