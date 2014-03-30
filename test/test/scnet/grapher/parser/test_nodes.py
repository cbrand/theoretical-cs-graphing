# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from test.scnet.grapher.parser.abstract_test import AbstractTest

from scnet.grapher.objects.node import Node

from scnet.grapher.parser.nodes import node_definition


class TestNodes(AbstractTest):
    """
    Tests the parsing of node entries.
    """

    def parse_and_return(self, text):
        """
        Parses the given text with the node definition
        and returns a result.
        """
        return node_definition.parse(
            self.tokenize(
                text
            )
        )

    def test_node_type(self):
        """
        It should return the correct object when parsing
        a node definition
        """
        result = self.parse_and_return(
            "Knoten Hallo"
        )
        self.assertIsInstance(
            result,
            Node
        )

    def test_node_name(self):
        """
        It should parse a correct node definition.
        """
        result = self.parse_and_return(
            "Knoten Hallo"
        )
        self.assertEqual(
            result.name,
            "Hallo"
        )

    def test_node_parsing_string(self):
        """
        It should parse a correct node definition
        with a name being passed as a string.
        """
        result = self.parse_and_return(
            "Knoten \"Hallo Welt\""
        )
        self.assertEqual(
            result.name,
            "Hallo Welt"
        )

    def test_string_representation(self):
        """
        It should parse correctly the string
        representation.
        """
        result = self.parse_and_return("knoten Hallo")
        result_text = str(result)
        self.assertEqual(
            result_text,
            "<Node Hallo>"
        )
