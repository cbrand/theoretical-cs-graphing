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

    @property
    def _site_manager(self):
        """
        Returns the current valid site manager.
        """
        return getSiteManager()

    @property
    def _edge_store(self) -> IEdgeStore:
        """
        Returns the current valid edge store.
        """
        return self._site_manager.getUtility(IEdgeStore)

    @property
    def _node_store(self) -> INodeStore:
        """
        Returns the current valid node store
        """
        return self._site_manager.getUtility(INodeStore)
