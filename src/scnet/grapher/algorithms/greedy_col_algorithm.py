# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from collections import defaultdict, Iterable

from scnet.grapher.interfaces import (
    IGraph,
)


class GreedyColAlgorithm(object):
    """
    Implementation of the greedy col coloring algorithm.
    """

    def __init__(
            self,
            graph: IGraph,
    ):
        self.graph = graph

    @staticmethod
    def get_colors(amount: int) -> list:
        """
        Returns evenly spreaded colors.
        :param amount: The number of colors needed.
        """
        return [float(i)/float(amount) for i in range(amount)]

    @staticmethod
    def possible_minimum(data: Iterable):
        """
        Returns the possible minimum value. Expects a set
        with integers. If the data does not have 0 it returns
        that. If not it returns the minimum value not given in
        the itertable entry.
        """
        if isinstance(data, set):
            set_data = data
        else:
            set_data = set(data)

        i = 0
        while i in set_data:
            i += 1
        return i

    def run(self) -> IGraph:
        """
        Runs the graph entry.
        """

        node_store = self.graph.node_store
        colormap = defaultdict(lambda: None)
        for node in node_store:
            min_index = self.possible_minimum(
                colormap[neighbor]
                for neighbor in node.neighbors
                if colormap[neighbor] is not None
            )
            colormap[node] = min_index

        num_colors = max(colormap.values()) + 1
        colors = self.get_colors(num_colors)
        for node, color_index in colormap.items():
            node.color = colors[color_index]
        return self.graph
