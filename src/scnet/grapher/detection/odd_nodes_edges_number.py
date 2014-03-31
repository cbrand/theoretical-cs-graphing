# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from .abstract import AbstractDetection


class OddNodeEdgesNumberDetection(AbstractDetection):
    """
    Checks if the graph has any nodes with an odd number
    of edges.
    """

    def detect(self):
        """
        Returns if the given graph is cohesive/
        coherent.
        """
        for node in self._node_store:
            if len(node.edges) % 2 == 1:
                return True
            else:
                pass
        return False

    def count_odd(self):
        """
        Returns the number of nodes which have an odd amount
        of edges in the given graph.
        """
        i = 0
        for node in self._node_store:
            if len(node.edges) % 2 == 1:
                i += 1
            else:
                pass
        return i
