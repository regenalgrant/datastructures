# _*_ encoding: utf-8 _*_
"""Python graph."""


class Graph(object):
    """Class Graph."""

    def __init__(self):
        """Initiatiliztion graph."""
        self.graph = {}

    def nodes(self):
        """Nodes in graph."""
        nodes = []
        for key in self.graph:
            nodes.append(key)
        return nodes
