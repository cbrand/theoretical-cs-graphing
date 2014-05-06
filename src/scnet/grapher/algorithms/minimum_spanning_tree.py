# -*- encoding: utf-8 -*-

import itertools
from collections import defaultdict

from scnet.grapher.interfaces import (
    IGraph,
    INode,
)
from scnet.grapher.objects import (
    Graph,
    NodeStore,
    EdgeStore,
    Node,
    Edge,
)


class MinimumSpanningTree(object):
    """
    Creates a minimum spanning tree on base of the
    prim's algorithm.
    """

    def __init__(
            self,
            graph: IGraph,
            start_at: INode=None
            ):
        self._graph = graph
        self._start_at = start_at

    def run(self) -> IGraph:
        """
        Creates a new graph out of the graph
        given to this object throught he constructor
        and returns it.
        """
        node_store = self._graph.node_store
        nodes = node_store
        check_node = self._start_at or node_store.one()

        new_nodes = [
            check_node
        ]
        new_edges = []

        while len(nodes) != len(new_nodes):
            next_edge = min(
                (
                    edge
                    for edge in itertools.chain.from_iterable(
                        node.edges for node in new_nodes
                    )
                    if edge.other.name not in new_nodes
                )
                ,
                key=lambda edge: edge.weight
            )
            new_edges.append(
                Edge(
                    next_edge.root.name,
                    next_edge.other.name,
                    next_edge.weight
                )
            )
            new_nodes.append(
                next_edge.other
            )

        return Graph(
            NodeStore(Node(node.name) for node in new_nodes),
            EdgeStore(new_edges),
        )
