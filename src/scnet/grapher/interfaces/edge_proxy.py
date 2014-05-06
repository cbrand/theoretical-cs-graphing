# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import Attribute

from .edge import IEdge


class IEdgeProxy(IEdge):
    """
    Proxy object which implements an "other node"
    function, and proxies all other data to the
    originale edge object. This other node data is
    being calculated on initialization by giving
    the root to the constructor.
    """

    other = Attribute('The other node where the query has not come from.')
    """:type: list[INode]"""

    root = Attribute('The root node where the query was originated from.')
    """:type: list[INode]"""
