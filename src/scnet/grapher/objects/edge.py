# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import implementer

from scnet.grapher.interfaces import INode
from scnet.grapher.interfaces.edge import IEdge

from .abstract import Abstract


@implementer(IEdge)
class Edge(Abstract):
    """
    Representation of an edge in the graph. This points
    from an edge to another edge with an optional weight.
    """

    def __init__(
            self,
            from_node: str=None,
            to_node: str=None,
            weight: int=None
    ):
        self.from_node_name = from_node
        self.to_node_name = to_node
        self.weight = weight
        super().__init__()

    def __str__(self):
        """
        Returns the string representation of this edge.
        """
        result = "<Edge from: %s, to: %s" % (
            self.from_node_name,
            self.to_node_name
        )
        if self.weight is not None:
            result += ", weight: %s" % (
                self.weight
            )

        result += ">"
        return result

    @property
    def from_node(self) -> INode:
        """
        Returns the node from which this edge is
        starting.
        """
        return self.node_store[self.from_node_name]

    @property
    def to_node(self) -> INode:
        """
        Returns the node where this edge is going
        to.
        """
        return self.node_store[self.to_node_name]

    @property
    def nodes(self) -> iter:
        """
        list of all edges which start
        or end in this node
        """
        yield self.from_node
        yield self.to_node

    def __eq__(self, other: IEdge):
        """
        Prüft ob der andere Edge dem gleichen entspricht.
        """
        if not IEdge.providedBy(other):
            return super().__eq__(other)
        else:
            return (
                other.from_node_name == self.from_node_name and
                other.to_node_name == self.to_node_name and
                other.weight == self.weight
            )
