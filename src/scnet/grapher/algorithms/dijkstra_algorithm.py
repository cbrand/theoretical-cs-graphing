# -*- encoding: utf-8 -*-

from collections import defaultdict

from scnet.grapher.interfaces import (
    IGraph,
    INode,
)


class DijkstraAlgorithm(object):
    """
    Implementation of the dijkstra shortest
    path algorithm for an undirected graph.
    """

    def __init__(
            self,
            graph: IGraph,
            from_node: INode,
            to_node: INode
            ):
        self.graph = graph
        if isinstance(from_node, str):
            from_node = graph.node_store.get(from_node)
        self.from_node = from_node
        if isinstance(to_node, str):
            to_node = graph.node_store.get(to_node)
        self.to_node = to_node
        self.distances = None

    def run(self):
        """
        Runs the algorithm. Returns a sequence of the
        shortest found path.
        """
        distances = defaultdict(lambda: {
            'from_node': None,
            'weight': float('inf')
        })
        min_node = self.from_node
        distances[min_node]['weight'] = 0
        nodes = set(self.graph.node_store)

        while nodes:
            min_node = min(
                (
                    node
                    for node in nodes
                    if node in distances
                ),
                key=lambda node: distances[node]['weight']
            )
            if min_node == self.to_node:
                break

            nodes.remove(min_node)
            current_distance = distances[min_node]

            for edge in min_node.edges:
                other_node = (
                    edge.from_node
                    if edge.from_node != min_node
                    else edge.to_node
                )
                path_weight = current_distance['weight'] + edge.weight
                if distances[other_node]['weight'] > path_weight:
                    distances[other_node] = {
                        'from_node': min_node,
                        'weight': path_weight,
                    }
        self.distances = distances

        temp_node = self.to_node
        path = []
        while temp_node != self.from_node:
            path.append(temp_node)
            temp_node = self.distances[temp_node]['from_node']
        path.append(temp_node)
        return path[::-1]
