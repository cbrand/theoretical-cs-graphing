# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.algorithms.depth_first_algorithm import (
    DepthFirstAlgorithm
)
from scnet.grapher.interfaces.graph import IGraph
from scnet.grapher.interfaces.node import INode

from .abstract import AbstractDetection


class CycleDetection(AbstractDetection):
    """
    Detects a cycle in a given graph and
    returns the first found cycle. Uses
    a slightly adjusted depth first algorithm
    to detect paths in the entry.
    """

    def __init__(self, graph: IGraph, start_at: INode=None):
        super().__init__(graph)
        self.reset()
        self._start_at = start_at or self.graph.node_store.one()
        self.sort = False

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

    def reset_cycle(self):
        """
        Resets the cycle variable, which display the cycle entry.
        """
        self.cycle = None

    def reset_stack(self):
        """
        Resets the stack list
        """
        self.stack = []

    def reset_traverse(self):
        """
        Resets the traverse list
        """
        self.traverse = []

    def reset(self):
        """
        Resets the internal data structures
        used for detection
        """
        self.reset_stack()
        self.reset_traverse()

    def detect(self):
        """
        Returns cycles in the graph.
        """
        found_items = set()
        while len(found_items) < len(self._node_store):
            detect = self._detect()
            if detect:
                return detect
            else:
                found_items.update(self.traverse)
                delta = set(self._node_store) - found_items
                if len(delta):
                    self._start_at = delta.pop()
                else:
                    pass
        return False

    def _detect(self):
        """
        Subprocedure for finding a cycle in
        one path.
        """
        self.reset()
        traverse = self.traverse
        self.stack.append(self._start_at)
        last_pop = None

        while len(self.stack):
            item = self.stack[-1]
            """:type: INode"""
            if item not in traverse:
                traverse.append(item)

            check = False
            neighbors = item.neighbors
            if self.sort:
                neighbors = sorted(
                    neighbors,
                    key=lambda node: node.name
                )
            for neighbor in neighbors:
                if neighbor in traverse:
                    # Already found once. Not sure though if it
                    # is just a neighbor.
                    if (
                        neighbor != last_pop and
                        neighbor in self.stack and
                        (
                            len(self.stack) < 2 or
                            self.stack[-2] != neighbor
                        )
                    ):
                        # Found a cycle.
                        index_in_stack = self.stack.index(neighbor)
                        self.cycle = self.stack[index_in_stack:]
                        return True
                    else:
                        pass
                else:
                    check = True
                    self.stack.append(
                        neighbor
                    )
                    break
            if not check:
                last_pop = self.stack.pop()
        return False


