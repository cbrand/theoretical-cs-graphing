# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import os
import unittest

from zope.component import getSiteManager

from tempfile import NamedTemporaryFile

from scnet.grapher.graph.drawer import GraphDrawer
from scnet.grapher.interfaces import (
    INodeStore,
    IEdgeStore
)
from scnet.grapher.objects import (
    EdgeStore,
    NodeStore,
    Edge,
    Node,
)


class TestDrawer(unittest.TestCase):

    def setUp(self):
        # Bridge problem graph
        self.nodes = [
            Node(str(number))
            for number in range(1, 12)
        ]
        self.node_store = NodeStore(self.nodes)
        self.edges = [
            Edge("1", "2"),
            Edge("1", "3"),
            Edge("1", "4"),
            Edge("3", "5"),
            Edge("4", "5"),
            Edge("5", "6"),
            Edge("6", "7"),
            Edge("2", "7"),
            Edge("5", "8"),
            Edge("5", "9"),
            Edge("8", "10"),
            Edge("9", "10"),
            Edge("10", "11"),
            Edge("7", "11"),
        ]
        self.edge_store = EdgeStore(self.edges)

        def assign_entries(abstract_obj):
            abstract_obj.node_store = self.node_store
            abstract_obj.edge_store = self.edge_store

        for node in self.nodes:
            assign_entries(node)
        for edge in self.edges:
            assign_entries(edge)

        self.graph_drawer = GraphDrawer(
            edge_store=self.edge_store,
            node_store=self.node_store,
        )

    def get_temp_filename(self, suffix='.png'):
        temp_png_file_handle = NamedTemporaryFile(
            delete=False,
            suffix=suffix
        )
        temp_png_file_name = temp_png_file_handle.name
        temp_png_file_handle.close()
        return temp_png_file_name

    def test_dump_as_png(self):
        """
        It should be able to dump the graph as png.
        """
        temp_png_file_name = self.get_temp_filename()
        try:
            self.graph_drawer.draw_png(
                temp_png_file_name
            )
        finally:
            os.remove(temp_png_file_name)

    def test_dump_as_png_via_registry(self):
        """
        It should be able to dump the last graph
        without passing the Edge and Node Store
        if they are registered as an Utility
        """
        getSiteManager().registerUtility(
            self.node_store,
            INodeStore
        )
        getSiteManager().registerUtility(
            self.edge_store,
            IEdgeStore
        )
        temp_png_file_name = self.get_temp_filename()
        try:
            GraphDrawer().draw_png(temp_png_file_name)
        finally:
            os.remove(temp_png_file_name)

    def test_dump_with_weight(self):
        """
        It should be able to dump an edge
        with a weight configured for it.
        """
        self.edges[0].weight = 100
        temp_png_file_name = self.get_temp_filename()
        try:
            self.graph_drawer.draw_png(
                temp_png_file_name
            )
        finally:
            os.remove(temp_png_file_name)
