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

    parent_nodes = Attribute('Returns all nodes this node is '
                             'a child of.')
    ":type: list[INode]"

    child_nodes = Attribute('Returns all nodes this node is '
                            'a parent of.')
    ":type: list[INode]"

    neighbors = Attribute('Returns all nodes this node has '
                          'connections to.')
    ":type: list[INode]"

    color = Attribute('The color of the node. None will give '
                      'the entry an automatic color.')
