# -*- encoding: utf-8 -*-
"""Funktionsdefinitionen die für das Matchen von Werten verwendet werden.
"""

from __future__ import unicode_literals

from funcparserlib.parser import some


def a_case_less(value):
    """Eq(a) -> Parser(a, a)

    Gibt einen Parser zurück, der auf den Wert der Tokens matcht,
    ohne dabei auf Groß oder Kleinschreibung zu achten.
    """
    name = getattr(value, 'name', value)
    value = getattr(value, 'value', value)
    return some(
        lambda t: t.value.lower() == value.lower()
    ).named(u'(a_case_less "%s")' % (name,))
