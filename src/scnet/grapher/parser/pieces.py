# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from funcparserlib.parser import some

from .definitions import token_types


token_value = lambda input_token: input_token.value
token_type = lambda request_type: some(
    lambda input_token: input_token.type == request_type
)
value_of_type = lambda request_type: token_type(request_type) >> token_value

remove_quotes = lambda value: value[1:-1]
string_value = value_of_type(token_types.STRING) >> remove_quotes

text_value = value_of_type(token_types.SYMBOL) | string_value

number_value = value_of_type(token_types.NUMBER) >> int
