# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import implementer

from scnet.grapher.interfaces import INode

from .abstract import Abstract
from .edge_proxy import EdgeProxy


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
        self.color = None
        super().__init__()

    def __repr__(self) -> str:
        """
        String representation of this node object.
        """
        return "<Node %s>" % self.name

    @property
    def edges_from(self) -> list:
        """
        Returns a list of edges, which are starting from
        this node.
        @rtype: iter[IEdgeProxy]
        """
        return list(
            EdgeProxy(edge, self)
            for edge in self.edge_store.from_node(self)
        )

    @property
    def edges_to(self) -> list:
        """
        Returns a list of edges, which are ending at this
        node.
        @rtype: iter[IEdgeProxy]
        """
        return list(
            EdgeProxy(edge, self)
            for edge in self.edge_store.to_node(self)
        )

    @property
    def edges(self) -> list:
        """
        Returns a list of edges.
        """
        return self.edges_from + self.edges_to

    @property
    def parent_nodes(self) -> list:
        """
        Returns all nodes this node is a child of.
        @rtype: iter[INode]
        """
        for edge in self.edges_to:
            yield edge.from_node

    @property
    def child_nodes(self) -> list:
        """
        Returns all nodes this node is a parent of.
        @rtype: iter[INode]
        """
        for edge in self.edges_from:
            yield edge.to_node

    @property
    def neighbors(self) -> list:
        """
        Returns all nodes this node is a parent of.
        @rtype: iter[INode]
        """
        nodes = set()
        node_containers = (self.parent_nodes, self.child_nodes)
        for node_container in node_containers:
            for node in node_container:
                if node in nodes:
                    pass
                else:
                    yield node
                    nodes.add(node)

    __hash__ = Abstract.__hash__
    
    @property
    def color(self):
        """
        Returns the color code of this node.
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Sets the color of this node.
        """
        self._color = value

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        else:
            return super(Node, self).__eq__(other)
