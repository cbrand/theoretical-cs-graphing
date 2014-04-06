# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from collections import Iterable
from scnet.grapher.interfaces.edge import IEdge

from scnet.grapher.interfaces.graph import IGraph
from scnet.grapher.interfaces.node import INode
from scnet.grapher.objects.abstract import Abstract
from scnet.grapher.objects.edge import Edge
from scnet.grapher.objects.graph import Graph
from scnet.grapher.objects.node import Node
from scnet.grapher.objects.stores.edge_store import EdgeStore
from scnet.grapher.objects.stores.node_store import NodeStore


def generate_nodes(
    *nodes: str
) -> Iterable:
    """
    Generates Nodes with the given names.
    @rtype: Iterable[INode]
    """
    for node_name in nodes:
        if INode.providedBy(node_name):
            yield node_name
        else:
            yield Node(node_name)

def generate_edges(
    *edges: Iterable
) -> Iterable:
    """
    Generates Edge objects with the given configuration.
    @param edges: tuples with two strings (from_node, to_node)
        in it.
    @type edges: Iterable[str]
    """
    for edge_def in edges:
        if IEdge.providedBy(edge_def):
            yield edge_def
            continue

        edge_def_length = len(edge_def)
        if edge_def_length == 2:
            yield Edge(*edge_def)
        else:
            from_node = edge_def[0]
            to_node = edge_def[1]
            if edge_def[2] is None:
                weight = None
            else:
                weight = int(edge_def[2])
            yield Edge(
                from_node,
                to_node,
                weight,
            )


class _Generator():
    """
    Generator. Helperfunctions to generate a graph.
    """

    def __init__(
        self,
        nodes: Iterable,
        edges: Iterable,
    ):
        """
        @param nodes: A list of node names.
        @type nodes: Iterable[str]
        @param edges: A list of tuples with two strings (from_node, to_node)
            in it.
        @type edges: Iterable[Iterable[str]]
        """
        self.nodes = list(generate_nodes(*nodes))
        self.edges = list(generate_edges(*edges))
        self.node_store = NodeStore(self.nodes)
        self.edge_store = EdgeStore(self.edges)

    def assign_stores(self, abstract_obj: Abstract):
        """
        Assigns the stores for a given entry.
        """
        abstract_obj.node_store = self.node_store
        abstract_obj.edge_store = self.edge_store

    def graph(
        self,
    ) -> IGraph:
        """
        Generates the graph object.
        """
        for edge in self.edge_store:
            self.assign_stores(edge)
        for node in self.node_store:
            self.assign_stores(node)
        return Graph(
            node_store=self.node_store,
            edge_store=self.edge_store,
        )


def generate_graph(
    nodes: Iterable,
    edges: Iterable,
    ) -> IGraph:
    """
    Generates a graph with the given configuration
    @param nodes: A list of node names.
    @type nodes: Iterable[str]
    @param edges: A list of tuples with two strings (from_node, to_node)
        in it.
    @type edges: Iterable[Iterable[str]]
    """
    return _Generator(
        nodes,
        edges
    ).graph()
