# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.detection.cycle_detection import CycleDetection
from test.scnet.grapher.abstract_base_test import AbstractBaseTest


class TestCycleDetection(AbstractBaseTest):

    def test_only_cycle(self):
        """
        It should detect a cycle in a graph with
        only one cycle and nothing else.
        """
        graph = self.prepare_graph(
            ("A", "B", "C", "D"),
            (
                ("A", "B"),
                ("B", "C"),
                ("C", "D"),
                ("D", "A"),
            )
        )
        cycle_detection = CycleDetection(
            graph,
            start_at=graph.node_store.get('A')
        )
        cycle_detection.sort = True
        self.assertTrue(
            cycle_detection.detect()
        )
        self.assertEqual(
            tuple(node.name for node in cycle_detection.cycle),
            ("A", "B", "C", "D")
        )

    def test_cycle_in_graph(self):
        """
        Checks if it can detect a cycle in a fully connected
        graph.
        """
        graph = self.prepare_graph(
            ("A", "B", "C", "D", "E", "F", "G", "H", "I",),
            (
                ("A", "B"),
                ("A", "I"),
                ("I", "G"),
                ("C", "D"),
                ("C", "E"),
                ("C", "F"),
                ("E", "H"),
                ("H", "G"),
                ("F", "G"),
            )
        )
        cycle_detection = CycleDetection(
            graph,
            start_at=graph.node_store.get('B')
        )
        cycle_detection.sort = True
        self.assertTrue(cycle_detection.detect())
        self.assertEqual(
            tuple(node.name for node in cycle_detection.cycle),
            (
                "G", "F", "C", "E", "H"
            )
        )

    def test_cycle_in_not_connected_graph(self):
        """
        It should detect a cycle even if the starting
        point to search for is not connected
        to the search cluster.
        """
        graph = self.prepare_graph(
            ("A", "B", "C", "D", "E", "F", "G", "H", "I",),
            (
                ("B", "C"),
                ("B", "A"),
                ("D", "E"),
                ("F", "H"),
                ("H", "D"),
                ("F", "E"),
            )
        )
        cycle_detection = CycleDetection(
            graph,
            start_at=graph.node_store.get('A')
        )
        cycle_detection.sort = True
        self.assertTrue(cycle_detection.detect())
        node_names = tuple(node.name for node in cycle_detection.cycle)
        self.assertIn(
            "F",
            node_names
        )
        self.assertIn(
            "H",
            node_names
        )
        self.assertIn(
            "D",
            node_names
        )
        self.assertIn(
            "E",
            node_names
        )
        self.assertEqual(
            len(node_names),
            4
        )

    def test_no_cycle_in_not_connected_graph(self):
        """
        It should detect that there are no cycles in
        several non connected clusters in one graph.
        """
        graph = self.prepare_graph(
            ("A", "B", "C", "D", "E", "F", "G", "H", "I",),
            (
                ("B", "C"),
                ("B", "A"),
                ("D", "E"),
                ("F", "H"),
                ("H", "D"),
                ("H", "I")
            )
        )
        cycle_detection = CycleDetection(
            graph,
        )
        self.assertFalse(cycle_detection.detect())
