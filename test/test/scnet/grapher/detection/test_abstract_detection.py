# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.detection.abstract import AbstractDetection

from test.scnet.grapher.abstract_base_test import AbstractBaseTest


class TestAbstractDetection(AbstractBaseTest):
    """
    Tests the basic functionality of the abstract base test class.
    """

    def test_return_of_node_store(self):
        """
        It should return the node store of the given
        graph.
        """
        graph = self.prepare_graph([], [])
        detection = AbstractDetection(graph)
        self.assertEqual(
            graph.node_store,
            detection._node_store
        )

    def test_return_of_edge_store(self):
        """
        It should return the node store of the given
        graph.
        """
        graph = self.prepare_graph([], [])
        detection = AbstractDetection(graph)
        self.assertEqual(
            graph.edge_store,
            detection._edge_store
        )
