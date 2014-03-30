# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from funcparserlib.lexer import Token
from funcparserlib.parser import a, skip

from .functions import a_case_less
from .definitions import token_types

symbol = lambda symbol_value: skip(
    a_case_less(
        Token(
            token_types.SYMBOL,
            symbol_value
        )
    )
)
symbol_node = symbol('knoten')
symbol_edge = symbol('kante')
