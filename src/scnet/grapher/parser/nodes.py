# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from .symbols import symbol_node
from .pieces import text_value

from scnet.grapher.objects.node import Node

node_definition = symbol_node + text_value >> (
    lambda value: Node(value)
)
"""Definition of a node in the graph"""
