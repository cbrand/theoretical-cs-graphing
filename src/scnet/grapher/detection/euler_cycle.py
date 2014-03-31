# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from .abstract import AbstractDetection
from .cohesive_graph import CohesiveGraphDetection
from .odd_nodes_edges_number import OddNodeEdgesNumberDetection


class EulerCycleDetection(AbstractDetection):
    """
    Tests if the given graph has an euler cycle.
    """

    COHESIVE_DETECTION_CLASS = CohesiveGraphDetection
    ODD_NODES_EDGES_NUMBER_CLASS = OddNodeEdgesNumberDetection

    def detect(self) -> bool:
        """
        Returns if the given graph has an euler
        cycle.
        """
        return self.is_cohesive() and not self.has_odd_nodes()

    def is_cohesive(self) -> bool:
        """
        Returns if the entry is cohesive.
        """
        cohesive_detection = self.COHESIVE_DETECTION_CLASS(self.graph)
        return cohesive_detection.detect()

    def has_odd_nodes(self) -> bool:
        """
        Returns if a node in the query has an odd number of
        relations.
        """
        odd_edges_detection = self.ODD_NODES_EDGES_NUMBER_CLASS(self.graph)
        return odd_edges_detection.detect()
