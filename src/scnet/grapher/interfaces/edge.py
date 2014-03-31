# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import Interface, Attribute


class IEdge(Interface):
    """
    Interface of an edge which connects
    two nodes with each other and has an
    optional weight.
    """

    from_node_name = Attribute("The node name from which "
                               "this edge starts.")
    to_node_name = Attribute("The node name to which this "
                             "edge goes.")
    from_node = Attribute("The node from which this edge is "
                          "starting from.")
    to_node = Attribute("The node to which this edge is "
                        "going to.")
    nodes = Attribute("Returns the two nodes in this edge.")
    weight = Attribute("The optional weight of this edge.")
