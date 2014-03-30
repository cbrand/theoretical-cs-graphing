# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import Interface, Attribute


class INode(Interface):
    """
    Representation of a node in the graph definition.
    """

    name = Attribute('The name of the node')
