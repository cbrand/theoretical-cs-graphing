# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import implementer

from scnet.grapher.interfaces import (
    INode,
    IEdge,
    IEdgeProxy
)

def proxy_attribute(name):
    """
    Helper function which returns a function which
    proxies the given attribute from the child edge
    entry.
    """
    @property
    def proxy(self):
        return getattr(self._edge, name)

    return proxy


@implementer(IEdgeProxy)
class EdgeProxy(object):
    """
    Proxy object which implements an "other node"
    function, and proxies all other data to the
    originale edge object. This other node data is
    being calculated on initialization by giving
    the root to the constructor.
    """

    def __init__(self,
                 edge: IEdge,
                 root: INode):
        self._edge = edge
        self.root = root

    @property
    def other(self):
        if self.from_node == self.root:
            return self.to_node
        else:
            return self.from_node

    from_node_name = proxy_attribute('from_node_name')
    to_node_name = proxy_attribute('to_node_name')
    from_node = proxy_attribute('from_node')
    to_node = proxy_attribute('to_node')
    nodes = proxy_attribute('nodes')
    weight = proxy_attribute('weight')
