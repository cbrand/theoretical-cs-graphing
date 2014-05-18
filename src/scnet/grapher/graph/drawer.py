# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import networkx
import matplotlib.pyplot as plt

from zope.component import getSiteManager

from scnet.grapher.interfaces import (
    IEdgeStore,
    INodeStore,
    IEdge,
    INode
)
from scnet.grapher.interfaces.graph import IGraph


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

    @classmethod
    def from_graph(cls, graph: IGraph):
        """
        Creates a drawer instance from a given graph.
        """
        return cls(
            node_store=graph.node_store,
            edge_store=graph.edge_store,
        )

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
            self._add_node(graph, node)
        for edge in self.edge_store:
            self._add_edge(graph, edge)

        self._draw_graph(graph)
        return graph

    def _draw_graph(self, graph: networkx.Graph):
        """
        Draws the given graph.
        """
        pos = networkx.fruchterman_reingold_layout(graph)

        draw_args = dict(
            node_size=1000,
            node_color=self._get_node_colors(
                graph
            ),
            cmap=plt.get_cmap('Set1')
        )

        networkx.draw(
            graph,
            pos,
            **draw_args
        )

        networkx.draw_networkx_edge_labels(
            graph,
            pos,
            edge_labels=self._get_edge_weights_for_label(
                graph
            )
        )

    def _get_node_colors(self, graph: networkx.Graph):
        """
        Returns a mapping for all nodes with a given color,
        if a color has been specified. Does not add nodes
        which don't have a color.
        """
        color_list = []
        for node, node_data in graph.nodes(data=True):
            color_list.append(node_data.get('node_color', 0.0))
        return color_list


    def _get_edge_weights_for_label(self, graph: networkx.Graph):
        """
        Returns a mapping for all edges which print the
        weight if a weight has been given for the entry.
        """
        edge_labels = {}
        for from_node, to_node, edge_data in graph.edges(data=True):
            if 'weight' in edge_data:
                edge_labels[(from_node, to_node,)] = edge_data['weight']
            else:
                pass
        return edge_labels

    def _add_node(self, graph: networkx.Graph, node: INode):
        """
        Adds a node to the given graph.
        """
        kwargs = dict()
        if node.color:
            kwargs.update(
                dict(
                    node_color=node.color,
                )
            )
        graph.add_node(node.name, **kwargs)


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
