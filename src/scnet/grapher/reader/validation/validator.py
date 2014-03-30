# -*- encoding: utf-8 -*-

from __future__ import unicode_literals


class Validator(object):
    """
    Validates the input data.
    """

    def __init__(
        self,
        node_store,
        edge_store
    ):
        """
        Validates the input data.
        """
        self.node_store = node_store
        self.edge_store = edge_store

    def validate(self):
        """
        Validates the data given in the stores.
        """
        def raise_error(node_name, edge):
            raise RuntimeError(
                "Could not find node %s in definition %s" % (
                    node_name,
                    edge
                )
            )

        for edge in self.edge_store:
            if edge.from_node_name not in self.node_store:
                raise_error(
                    edge.from_node_name,
                    edge
                )
            elif edge.to_node_name not in self.node_store:
                raise_error(
                    edge.from_node_name,
                    edge
                )
            else:
                pass
