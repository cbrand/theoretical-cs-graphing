# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.algorithms.depth_first_algorithm import \
    DepthFirstAlgorithm
from scnet.grapher.interfaces.node import INode

from test.scnet.grapher.abstract_base_test import AbstractBaseTest


class TestDepthFirstAlgorithm(AbstractBaseTest):
    """
    Tests the depth first algorithm entry.
    """

    def setUp(self):
        self.nodes = self.generate_nodes(
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
        )
        self.edges = self.generate_edges(
            ("A", "B"),
            ("A", "I"),
            ("I", "C"),
            ("I", "G"),
            ("C", "D"),
            ("C", "E"),
            ("C", "F"),
            ("E", "H"),
            ("H", "G"),
            ("F", "G"),
        )
        self.graph = self.prepare_graph(
            self.nodes,
            self.edges,
        )

    def test_traversal(self):
        """
        Tests if the graph is being traversed correct.
        """
        start_at = self.graph.node_store.get("A")
        depth_first = DepthFirstAlgorithm(self.graph, start_at)
        depth_first.traverse()
        traversed_tree = depth_first.traverse_tree
        traversed_tree_node_names = tuple(
            node.name
            for node in traversed_tree
        )
        self.assertEqual(
            traversed_tree_node_names,
            (
                "A",
                "B",
                "I",
                "C",
                "D",
                "E",
                "H",
                "G",
                "F",
            )
        )

    def test_find_negative(self):
        """
        Es sollte None zurück geben, wenn der Eintrag nicht
        gefunden werden kann.
        """
        depth_first = DepthFirstAlgorithm(self.graph)
        self.assertIsNone(
            depth_first.find('Z')
        )

    def test_find_positive(self):
        """
        Es sollte beim finden eines existierenden Eintrags
        korrekt
        """
        depth_first = DepthFirstAlgorithm(
            self.graph,
            self.graph.node_store.get('A')
        )
        search_result = depth_first.find("I")
        self.assertTrue(
            INode.providedBy(search_result)
        )

        self.assertEqual(
            tuple(node.name for node in depth_first.traverse_tree),
            (
                "A",
                "B",
                "I"
            )
        )

    def test_sort(self):
        """
        Es sollte möglich sein die Suche zu sortieren.
        """
        graph = self.prepare_graph(
            self.generate_nodes(
                "C",
                "B",
                "A",
            ),
            self.generate_edges(
                ("C", "A"),
                ("B", "A"),
            ),
        )
        depth_first = DepthFirstAlgorithm(
            graph,
            graph.node_store.get('A')
        )
        depth_first.sort = True
        depth_first.traverse()
        self.assertEqual(
            tuple(item.name for item in depth_first.traverse_tree),
            (
                "A", "B", "C"
            )
        )
