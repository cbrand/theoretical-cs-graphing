# -*- encoding: utf-8 -*-

import collections

from scnet.grapher.interfaces.graph import IGraph
from scnet.grapher.interfaces.node import INode


class DepthFirstAlgorithm(object):
    """
    Implementiert den Depth First
    Search Algorithm eines übergebenen
    Eintrags.
    """

    def __init__(self, graph: IGraph, start_at: INode=None):
        """
        @param graph: Der Graph der durchsucht
            werden soll.
        """
        if start_at is None:
            start_at = graph.node_store.one()
        else:
            pass
        self._graph = graph
        self._start_at = start_at
        self._stop_at = None
        self._sort = False
        self.traverse_tree = None

    @property
    def sort(self):
        """
        Gibt zurück ob die Rückgaben vor der Auswertung
        sortiert werden sollen. Dies kann durchgeführt
        werden um eine nachvollziehbare Algorithmusrückgabe
        zu gewährleisten..
        """
        return self._sort

    @sort.setter
    def sort(self, sort=False):
        """
        Setzt ob die Nodes sortiert werden sollen.
        """
        self._sort = bool(sort)

    def traverse(self) -> INode:
        """
        Traversiert den übergebenen Pfad und gibt
        ein Set zurück, an Nodes die besucht
        wurden.
        """
        first_node = self._start_at
        self.traverse_tree = traverse = []
        stack = [first_node]
        while len(stack):
            item = stack[-1]
            """:type: INode"""
            if item not in traverse:
                traverse.append(item)
            if item.name == self._stop_at:
                return item

            check = False
            neighbors = item.neighbors
            if self.sort:
                neighbors = sorted(
                    neighbors,
                    key=lambda node: node.name
                )
            for neighbor in neighbors:
                if neighbor in traverse:
                    pass
                else:
                    check = True
                    stack.append(
                        neighbor
                    )
                    break
            if not check:
                stack.pop()
        return None

    def find(self, node_name: str) -> INode:
        """
        Sucht den Pfad nach den übergebnenen Nodenamen
        ab und gibt den Eintrag zurück.
        Gibt den gefundenen Node zurück.
        """
        self._stop_at = node_name
        return self.traverse()
