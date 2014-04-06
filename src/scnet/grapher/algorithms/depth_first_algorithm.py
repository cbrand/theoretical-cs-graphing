# -*- encoding: utf-8 -*-

import collections

from scnet.grapher.interfaces.graph import IGraph
from scnet.grapher.interfaces.node import INode


class DepthFirstAlgorithm(object):
    """
    Implements the depth first search algorithm for an
    undirected graph.
    """

    def __init__(self, graph: IGraph, start_at: INode=None):
        if start_at is None:
            start_at = graph.node_store.one()
        else:
            pass
        self._graph = graph
        self._start_at = start_at
        self._stop_at = None
        self.sort = False
        self.traverse_tree = None

    @property
    def sort(self):
        """
        Returns if before traversing the tree the neighbors
        of the check node should be sorted. This can be helpful
        if you want to test for the return.
        """
        return self._sort

    @sort.setter
    def sort(self, sort=False):
        """
        Sets if the neighbors of a node should be sorted
        by name before being traversed
        """
        self._sort = bool(sort)

    def traverse(self) -> INode:
        """
        Traverses the given node and returns the to find INode
        if existing in the system.
        """
        first_node = self._start_at
        self.traverse_tree = traverse = []
        stack = [first_node]
        while len(stack):
            item = stack[-1]
            """:type: INode"""
            if item not in traverse:
                traverse.append(item)
            if item.name == self._stop_at:
                return item

            check = False
            neighbors = item.neighbors
            if self.sort:
                neighbors = sorted(
                    neighbors,
                    key=lambda node: node.name
                )
            for neighbor in neighbors:
                if neighbor in traverse:
                    pass
                else:
                    check = True
                    stack.append(
                        neighbor
                    )
                    break
            if not check:
                stack.pop()
        return None

    def find(self, node_name: str) -> INode:
        """
        Searches in the graph after the node with the
        given Node Name and returns this node if found
        or None if no node could be found
        """
        self._stop_at = node_name
        return self.traverse()
