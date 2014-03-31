# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.component.hooks import getSiteManager

from scnet.grapher.interfaces.edge_store import IEdgeStore
from scnet.grapher.interfaces.node_store import INodeStore


class Abstract(object):
    """
    Abstract class which has some utlity
    functions for the given objects.
    """

    def __init__(self):
        self._node_store = None
        self._edge_store = None

    @property
    def edge_store(self) -> IEdgeStore:
        """
        Returns the current valid edge store.
        """
        return self._edge_store

    @edge_store.setter
    def edge_store(self, value: IEdgeStore):
        """
        Sets the edge store of the given
        """
        self._edge_store = value

    @property
    def node_store(self) -> INodeStore:
        """
        Returns the current valid node store
        """
        return self._node_store

    @node_store.setter
    def node_store(self, value: INodeStore):
        """
        Sets a specific node store for this element.
        """
        self._node_store = value
