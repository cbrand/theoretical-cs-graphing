# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.detection.euler_cycle import EulerCycleDetection


class EulerPathDetection(EulerCycleDetection):
    """
    Tests the given graph has an euler path.
    """

    def detect(self) -> bool:
        """
        Returns if the given graph has an euler
        path.
        """
        number_odd = self.count_nodes_with_odd_edges()
        return self.is_cohesive() and number_odd in (0, 2)

    def count_nodes_with_odd_edges(self):
        """
        Returns the amount of nodes which have an odd
        number of edges.
        """
        odd_checker = self.ODD_NODES_EDGES_NUMBER_CLASS(self.graph)
        return odd_checker.count_odd()
