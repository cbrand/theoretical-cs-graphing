# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import collections

from .abstract import AbstractDetection


class CohesiveGraphDetection(AbstractDetection):
    """
    Checks if the graph is combined and there
    are no non interconnected clusters in
    the path.
    """

    def detect(self):
        """
        Returns if the given graph is cohesive/
        coherent.
        """
        node_store = self._node_store
        if len(node_store) == 0:
            return True
        node = node_store.one()
        seen = {node}
        to_process = collections.deque((node,))
        while len(to_process):
            node = to_process.popleft()
            for edge in node.edges:
                for node in edge.nodes:
                    if node not in seen:
                        to_process.append(node)
                        seen.add(node)
                    else:
                        pass
        return len(seen) == len(node_store)
