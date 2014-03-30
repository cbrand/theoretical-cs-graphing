# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import io

from zope.component.hooks import getSiteManager

from scnet.grapher.tokenizer import Tokenizer
from scnet.grapher.parser import parser_definition
from scnet.grapher.objects import (
    EdgeStore,
    Edge,
    NodeStore,
    Node,
)
from scnet.grapher.interfaces import (
    IEdgeStore,
    INodeStore,
)
from .reader_return import ReaderReturn
from .validation.validator import Validator


class Reader(object):
    """
    A reader which is being used to get the data out of a
    file and returns the given representation of the
    entries.
    """

    def __init__(self, file_handle: io.FileIO):
        """
        @param file_handle: The handle the data should be parsed from.
        """
        self._site_manager = getSiteManager()
        """:type: SiteManager"""
        self._file_handle = file_handle

    @classmethod
    def from_filename(cls, filename: str) -> "Reader":
        """
        Parses the data from a filename and returns the
        configuration object.
        """
        handle = open(filename, 'r')
        return cls(handle)

    def __del__(self):
        """
        Frees the resources being reserved by this object.
        """
        try:
            self._file_handle.close()
        except (IOError, OSError):  # pragma: no cover
            pass

    def parse(self) -> ReaderReturn:
        """
        Parses the data and returns the configuration
        objects which hold the information stored in the
        file handle.
        @raise: RuntimeError if the construct is not valid.
        """
        tokens = list(
            Tokenizer(self._file_handle).tokens
        )
        entries = list(
            self.flatten(
                parser_definition.parse(tokens)
            )
        )
        edge_store = self._set_edge_store(entries)
        node_store = self._set_node_store(entries)
        Validator(
            edge_store=edge_store,
            node_store=node_store,
        ).validate()

        return ReaderReturn(
            edge_store=edge_store,
            node_store=node_store,
        )

    def flatten(self, list_object: list):
        """
        Flattens the given list in lists.
        """
        for list_item in list_object:
            if isinstance(list_item, (tuple, list)):
                yield from self.flatten(list_item)
            else:
                yield list_item

    def _set_edge_store(self, entries: list) -> EdgeStore:
        """
        Sets the edge store in the given context
        from the given entries.
        """
        edge_store = EdgeStore(
            edges=[
                edge
                for edge in entries
                if isinstance(edge, Edge)
            ]
        )
        self._site_manager.registerUtility(
            edge_store,
            provided=IEdgeStore
        )
        return edge_store

    def _set_node_store(self, entries: list) -> NodeStore:
        """
        Sets the node store out of the given entries.
        """
        node_store = NodeStore(
            nodes=[
                node
                for node in entries
                if isinstance(node, Node)
            ]
        )
        self._site_manager.registerUtility(
            node_store,
            provided=INodeStore
        )
        return node_store
