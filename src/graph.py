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

    def edges(self):
        """List of edges in graph."""
        return [(key, item) for key in self.graph for item in self.graph[key]]

    def add_node(self, val):
        """Add node to graph."""
        if val in self.graph:
            pass
        else:
            self.graph[val] = []
