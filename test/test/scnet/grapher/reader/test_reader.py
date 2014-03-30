# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import os
import io
import unittest

from tempfile import NamedTemporaryFile

from scnet.grapher.reader import Reader


TEST_FILE_STRING = """
knoten NAME-1
knoten NAME-2
knoten NAME-3
knoten NAME-4
# Kommentarzeilen beginnen mit #

# Leerzeilen werden ignoriert
kante NAME-1 NAME-4 200
kante NAME-2 NAME-1
kante NAME-3 NAME-4
"""


class TestReader(unittest.TestCase):
    """
    Tests the functionality of the reader class.
    """

    @property
    def _io_data(self) -> io.StringIO:
        """
        Returns the test data.
        """
        return io.StringIO(
            TEST_FILE_STRING
        )

    def _test_filename(self) -> str:
        """
        Writes the data to a temporary file and
        returns the filename to it.
        """
        tempfile = NamedTemporaryFile(delete=False)
        tempfile.write(
            TEST_FILE_STRING.encode('utf-8')
        )
        tempfile.close()
        return tempfile.name

    def _parse(self):
        """
        Tries to parse the data and gets the result
        back.
        """
        return Reader(self._io_data).parse()

    def test_parse(self):
        """
        It should be able to parse the test data
        without raising an error.
        """
        self._parse()

    def test_parse_from_file(self):
        """
        It should be able to parse the data from
        a filename.
        """
        filename = self._test_filename()
        try:
            Reader.from_filename(filename).parse()
        finally:
            os.remove(filename)

    def test_parse_nodes(self):
        """
        It should parse correctly all given node names.
        """
        stores = self._parse()
        node_names = [
            node.name for node in stores.node_store
        ]

        test_node_names = [
            "NAME-1",
            "NAME-2",
            "NAME-3",
            "NAME-4",
        ]
        for test_node_name in test_node_names:
            self.assertIn(test_node_name, node_names)

    def test_parse_edges_node_1(self):
        """
        It should parse all given edges correctly from
        NAME-1 correctly.
        """
        stores = self._parse()
        edges = stores.edge_store
        name_1_edges = edges.from_node_name("NAME-1")
        self.assertEqual(
            len(name_1_edges),
            1
        )
        name_1_edge = name_1_edges[0]
        self.assertEqual(
            name_1_edge.to_node_name,
            "NAME-4"
        )
        self.assertEqual(
            name_1_edge.weight,
            200
        )

    def test_parse_edges_node_2(self):
        """
        It should parse all given edges correctly from
        NAME-2 correctly.
        """
        stores = self._parse()
        edges = stores.edge_store
        name_2_edges = edges.from_node_name("NAME-2")
        self.assertEqual(
            len(name_2_edges),
            1
        )
        name_2_edge = name_2_edges[0]
        self.assertEqual(
            name_2_edge.to_node_name,
            "NAME-1"
        )

    def test_parse_edges_node_3(self):
        """
        It should parse all given edges correctly from
        NAME-2 correctly.
        """
        stores = self._parse()
        edges = stores.edge_store
        name_3_edges = edges.from_node_name("NAME-3")
        self.assertEqual(
            len(name_3_edges),
            1
        )
        name_3_edge = name_3_edges[0]
        self.assertEqual(
            name_3_edge.to_node_name,
            "NAME-4"
        )

    def test_parse_edges_to_node_1(self):
        """
        It should parse all given edges correctly to
        NAME-1 correctly.
        """
        stores = self._parse()
        edges = stores.edge_store
        name_1_edges = edges.to_node_name("NAME-1")
        self.assertEqual(
            len(name_1_edges),
            1
        )
        name_1_edge = name_1_edges[0]
        self.assertEqual(
            name_1_edge.from_node_name,
            "NAME-2"
        )

    def test_node_edge_resolve_from(self):
        """
        It should resolve the from node entry
        correctly.
        """
        stores = self._parse()
        nodes = stores.node_store
        node = nodes['NAME-1']
        edges_from = node.edges_from
        self.assertEqual(
            len(edges_from),
            1
        )
        self.assertEqual(
            edges_from,
            stores.edge_store.from_node(node)
        )

    def test_node_edge_resolve_to(self):
        """
        It should reoslve the to node entry
        correctly.
        """
        stores = self._parse()
        nodes = stores.node_store
        node = nodes['NAME-1']
        edges_to = node.edges_to
        self.assertEqual(
            len(edges_to),
            1
        )
        self.assertEqual(
            edges_to,
            stores.edge_store.to_node(node)
        )
