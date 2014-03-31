# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from zope.interface import implementer

from scnet.grapher.objects.node import Node
from scnet.grapher.interfaces.node_store import INodeStore


@implementer(INodeStore)
class NodeStore(object):
    """
    Class which is used to register the nodes
    of a graph configuration file.
    """

    def __init__(self, nodes: list):
        """
        @param nodes: The nodes which should be stored
            by this object.
        @type nodes: list[Node]
        """
        self._nodes = nodes

    @property
    def _nodes(self):
        """
        Returns the nodes of this entry.
        """
        return self.__nodes.values()

    @_nodes.setter
    def _nodes(self, values):
        """
        Sets the nodes of this entry.
        @type values: list[Node]
        """
        self.__nodes = {}
        for node in values:
            self.__nodes[node.name] = node

    def get(self, node_name: str) -> Node:
        """
        Returns the which has the given node name.
        @raise: KeyError if the node does not exist.
        """
        return self[node_name]

    def has(self, node_name: str) -> bool:
        """
        Returns if this store has a node stored
        with the given name.
        @rtype: bool
        """
        return node_name in self

    def one(self) -> Node:
        """
        Returns one element in the node store.
        (Useful for general checking algorithms).
        """
        nodes = list(self._nodes)
        return nodes[0]

    def __getitem__(self, key: str) -> Node:
        """
        Returns the entry of this store.
        @raise: KeyError if not found.
        """
        return self.__nodes[key]

    def __contains__(self, node_name: str) -> bool:
        """
        Returns if this store has a node stored
        with the given name.
        @rtype: bool
        """
        return node_name in self.__nodes

    def __iter__(self) -> iter:
        """
        Iterates through all given nodes.
        """
        return self._nodes.__iter__()

    def __len__(self) -> int:
        """
        Returns the amount of stored nodes in
        the system.
        """
        return len(self.__nodes)
