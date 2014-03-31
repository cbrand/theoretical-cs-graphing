# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import Interface, Attribute


class IGraph(Interface):
    """
    Interface which is the representation
    of a graph.
    """

    node_store = Attribute('The store which holds '
                           'the nodes of this graph.')
    edge_store = Attribute('The store which holds '
                           'the edges of this graph.')