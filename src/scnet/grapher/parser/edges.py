# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from funcparserlib.parser import maybe

from scnet.grapher.objects.edge import Edge

from .symbols import symbol_edge
from .pieces import text_value, number_value


def create_edge_definition(definitions):
    """
    Creates an Edge out of the Edge Text Data
    @rtype: Edge
    """
    edge = Edge()
    edge.from_node_name = definitions[0]
    edge.to_node_name = definitions[1]
    if len(definitions) > 2 and definitions[2] is not None:
        edge.weight = int(definitions[2])
    return edge

edge_definition = (
    symbol_edge + text_value + text_value + maybe(number_value)
) >> create_edge_definition
