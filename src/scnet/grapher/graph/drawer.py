# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import networkx
import matplotlib.pyplot as plt

from zope.component import getSiteManager

from scnet.grapher.interfaces import (
    IEdgeStore,
    INodeStore,
    IEdge
)


class GraphDrawer(object):
    """
    Draws the graph for the entry.
    """

    def __init__(
        self,
        edge_store=None,
        node_store=None,
    ):
        self.edge_store = edge_store
        self.node_store = node_store

    def show(self):  # pragma: no cover
                     # (not testable with unittest)
        self._draw()
        return plt.show()

    def draw_png(self, filename: str):
        """
        Draws the PNG to the given path
        """
        self._draw()
        return plt.savefig(filename)

    def _draw(self) -> networkx.Graph:
        """
        Draws the given data to a graph and returns
        the Graph object.
        """
        graph = networkx.Graph()
        for node in self.node_store:
            graph.add_node(node.name)
        for edge in self.edge_store:
            self._add_edge(graph, edge)

        self._draw_graph(graph)
        return graph

    def _draw_graph(self, graph: networkx.Graph):
        """
        Draws the given graph.
        """
        pos = networkx.fruchterman_reingold_layout(graph)
        networkx.draw(graph, pos, node_size=1000)

        self.edge_weights = self.get_edge_weights_for_label(
            graph
        )
        networkx.draw_networkx_edge_labels(
            graph,
            pos,
            edge_labels=self.get_edge_weights_for_label(
                graph
            )
        )

    def get_edge_weights_for_label(self, graph: networkx.Graph):
        """
        Returns a mapping for all edges which print the
        weight if a weight has been given for the entry.
        """
        edge_labels = {}
        for from_node, to_node, edge_data in graph.edges(data=True):
            if 'weight' in edge_data:
                edge_data[(from_node, to_node,)] = edge_data['weight']
            else:
                pass
        return edge_labels

    def _add_edge(self, graph: networkx.Graph, edge: IEdge):
        """
        Adds an edge to the given graph
        """
        kwargs = {}
        if edge.weight is not None:
            kwargs["weight"] = edge.weight
        else:
            pass

        graph.add_edge(
            edge.from_node_name,
            edge.to_node_name,
            **kwargs
        )

    @property
    def edge_store(self) -> IEdgeStore:
        """
        Returns the for this drawer valid edge store.
        """
        return self._edge_store

    @edge_store.setter
    def edge_store(self, edge_store: IEdgeStore):
        """
        Sets the edge store for the entry.
        """
        if edge_store is None:
            edge_store = getSiteManager().getUtility(IEdgeStore)
        else:
            pass
        self._edge_store = edge_store

    @property
    def node_store(self) -> INodeStore:
        """
        Returns the for this drawer valid node store.
        """
        return self._node_store

    @node_store.setter
    def node_store(self, node_store: INodeStore):
        """
        Sets the node store for this drawer.
        """
        if node_store is None:
            node_store = getSiteManager().getUtility(INodeStore)
        else:
            pass
        self._node_store = node_store
