# -*- encoding: utf-8 -*-

from __future__ import unicode_literals


class token_types(object):
    """
    Token types which are being used during the
    tokenizer process.
    """
    SPACE = 'space'
    SYMBOL = 'symbol'
    STRING = 'string'
    COMMENT = 'comment'
    NUMBER = 'number'

NUMBER_DEFINITION = r'[0-9]+'
WHITE_SPACE_DEFINITION = r'[\s]'
STRING_PART_DEFINITION = r'(\\")|[^"\\]|(\\.)'
STRING_DEFINITION = r'"({string_part})*"'.format(
    string_part=STRING_PART_DEFINITION,
)
SYMBOL_DEFINITION = r'[a-zA-Z]{1}([a-zA-Z]|%s|-|\\_)+' % NUMBER_DEFINITION
COMMENT_DEFINITION = r'#[^\n]*'
