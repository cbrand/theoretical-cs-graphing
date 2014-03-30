# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import Interface


class INodeStore(Interface):
    """
    Interface which holds all Nodes of one graph
    configuration entry.
    """

    def get(self, node_name: str) -> "Node":
        """
        Returns the which has the given node name.
        @raise: KeyError if the node does not exist.
        """

    def has(self, node_name: str) -> bool:
        """
        Returns if this store has a node stored
        with the given name.
        @rtype: bool
        """

    def __getitem__(self, key: str) -> "Node":
        """
        Returns the entry of this store.
        @raise: KeyError if not found.
        """

    def __contains__(self, node_name: str) -> bool:
        """
        Returns if this store has a node stored
        with the given name.
        @rtype: bool
        """

    def __iter__(self) -> iter:
        """
        Iterates through all given nodes.
        @rtype: iter[INode]
        """
