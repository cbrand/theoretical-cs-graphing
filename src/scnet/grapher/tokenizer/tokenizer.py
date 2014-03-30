# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import re

from funcparserlib.lexer import (
    make_tokenizer
)

from .definitions import (
    STRING_DEFINITION,
    WHITE_SPACE_DEFINITION,
    SYMBOL_DEFINITION,
    COMMENT_DEFINITION,
    NUMBER_DEFINITION,
    token_types,
)

re_mode = re.IGNORECASE | re.UNICODE


class Tokenizer(object):
    """Generates tokens from the given input data.
    """

    SPECS = [
        (
            token_types.SPACE,
            (WHITE_SPACE_DEFINITION, re_mode)
        ),
        (
            token_types.SYMBOL,
            (SYMBOL_DEFINITION, re_mode)
        ),
        (
            token_types.STRING,
            (STRING_DEFINITION, re_mode)
        ),
        (
            token_types.COMMENT,
            (COMMENT_DEFINITION, re_mode)
        ),
        (
            token_types.NUMBER,
            (NUMBER_DEFINITION, re_mode)
        )
    ]

    IGNORED = [
        token_types.SPACE,
        token_types.COMMENT,
    ]

    def __init__(self, input_data):
        """
        @param input_data: The data which should be tokenized.
        @type input_data: file or str
        """
        self._input_data = input_data

    @property
    def _input_data(self):
        """
        Returns the input data.
        """
        return self.__input_data

    @_input_data.setter
    def _input_data(self, input_data):
        """
        Sets and normalizes the input data.
        """
        if hasattr(input_data, 'read'):
            input_data = input_data.read()
        else:
            pass
        self.__input_data = input_data

    @property
    def tokens(self):
        """
        Returns an iterator which generates tokens
        out of the given input data.
        """
        for token in self._tokenizer(self._input_data):
            if token.type not in self.IGNORED:
                yield token

    @property
    def _tokenizer(self):
        """
        Returns the funcparserlib tokenizer initialized with the
        configuration data in this tokenizer.
        """
        return make_tokenizer(self.SPECS)