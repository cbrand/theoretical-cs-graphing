# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from funcparserlib.parser import oneplus, finished

from .edges import edge_definition
from .nodes import node_definition

parser_definition = oneplus(
    edge_definition | node_definition
) + finished
