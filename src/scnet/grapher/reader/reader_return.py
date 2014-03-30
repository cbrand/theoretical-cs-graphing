# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from scnet.grapher.objects import (
    NodeStore,
    EdgeStore,
)


class ReaderReturn(object):
    """
    Representation of a return
    of the reader data.
    """

    def __init__(self, node_store: NodeStore, edge_store: EdgeStore):
        self.node_store = node_store
        self.edge_store = edge_store