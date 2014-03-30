# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from funcparserlib.parser import NoParseError

from test.scnet.grapher.parser.abstract_test import AbstractTest

from scnet.grapher.objects import Edge
from scnet.grapher.parser.edges import edge_definition


class TestEdges(AbstractTest):
    """
    Tests the Parsing of an Edge Definition.
    """

    def parse_and_return(self, text_value: str) -> Edge:
        """
        Takes the text tokenizes it and tries to parse
        the tokens with the edge definition.
        """
        return edge_definition.parse(
            self.tokenize(
                text_value
            )
        )

    def test_edge_type_return(self):
        """
        It should return an Edge Object when parsing.
        """
        edge = self.parse_and_return("Kante Test Test2")
        self.assertIsInstance(edge, Edge)

    def test_edge_from_node(self):
        """
        It should return the right from node entry.
        """
        edge = self.parse_and_return("Kante Test Test2")
        self.assertEqual(
            edge.from_node_name,
            "Test"
        )

    def test_edge_to_node(self):
        """
        It should return the right to node entry.
        """
        edge = self.parse_and_return("Kante Test Test2")
        self.assertEqual(
            edge.to_node_name,
            "Test2"
        )

    def test_edge_from_node_from_string(self):
        """
        It should return the correct from node when being
        passed as a string.
        """
        edge = self.parse_and_return("Kante \"Test Entry\" Test2")
        self.assertEqual(
            edge.from_node_name,
            "Test Entry"
        )

    def test_edge_to_node_from_string(self):
        """
        It should return the correct to node when being
        passed as a string.
        """
        edge = self.parse_and_return("Kante Test \"Test 2'\"")
        self.assertEqual(
            edge.to_node_name,
            "Test 2'"
        )

    def test_edge_weight_not_set(self):
        """
        It should not set a weight if None is being given in the
        definition.
        """
        edge = self.parse_and_return("Kante Test Test2")
        self.assertIsNone(edge.weight)

    def test_edge_weight(self):
        """
        It should return the correct weight when being given.
        """
        edge = self.parse_and_return("Kante Test Test2 200")
        self.assertEqual(edge.weight, 200)

    def test_error_trigger(self):
        """
        It should raise an Error if the format is not correct.
        """
        with self.assertRaises(NoParseError):
            self.parse_and_return("Konnte Test Test Test")

    def test_edge_string(self):
        """
        It should return the correct string representation.
        """
        edge = self.parse_and_return("Kante Test Test2 200")
        edge_string = str(edge)
        self.assertIn(
            "<Edge",
            edge_string,
        )
        self.assertIn(
            "from: %s" % edge.from_node_name,
            edge_string,
        )
        self.assertIn(
            "to: %s" % edge.to_node_name,
            edge_string,
        )
        self.assertIn(
            "weight: %s" % edge.weight,
            edge_string
        )

    def test_edge_string_without_weight(self):
        """
        It should return the correct string representation
        when no weight is given to the parser.
        """
        edge = self.parse_and_return("Kante Test Test2")
        edge_string = str(edge)
        self.assertIn(
            "<Edge",
            edge_string,
        )
        self.assertIn(
            "from: %s" % edge.from_node_name,
            edge_string,
        )
        self.assertIn(
            "to: %s" % edge.to_node_name,
            edge_string,
        )
