# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import Interface, Attribute


class INode(Interface):
    """
    Representation of a node in the graph definition.
    """

    name = Attribute('The name of the node')

    edges_from = Attribute('list of edges starting at this node')

    edges_to = Attribute('list of edges ending at this node.')

    edges = Attribute('list of all edges which start '
                      'or end in this node')
