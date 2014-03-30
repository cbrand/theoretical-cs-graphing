# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from scnet.grapher.tokenizer import Tokenizer


class AbstractTest(unittest.TestCase):
    """
    Abstract Test for the Parser related tests.
    """

    def tokenize(self, input_data):
        """
        Tokenizes the given input data and returns
        the generated tokens.
        @rtype: list[Token]
        """
        return list(Tokenizer(input_data).tokens)
