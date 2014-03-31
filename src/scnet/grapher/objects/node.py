# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import implementer

from scnet.grapher.interfaces import INode

from .abstract import Abstract


@implementer(INode)
class Node(Abstract):
    """
    Representation of a node in a directed
    or undirected graph.
    """

    def __init__(self, node_name: str):
        """
        @param node_name: The name of the node being
            used.
        @type node_name: str
        """
        assert isinstance(node_name, str), 'Passed entry has to be of type str'
        self.name = node_name
        super().__init__()

    def __str__(self) -> str:
        """
        String representation of this node object.
        """
        return "<Node %s>" % self.name

    @property
    def edges_from(self) -> list:
        """
        Returns a list of edges, which are starting from
        this node.
        @rtype: iter[IEdge]
        """
        return self.edge_store.from_node(self)

    @property
    def edges_to(self) -> list:
        """
        Returns a list of edges, which are ending at this
        node.
        @rtype: iter[IEdge]
        """
        return self.edge_store.to_node(self)

    @property
    def edges(self) -> list:
        """
        Returns a list of edges.
        """
        return self.edges_from + self.edges_to
