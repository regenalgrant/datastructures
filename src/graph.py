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

    def add_edge(self, val, val2):
        """Add edge to graph."""
        if val not in self.graph:
            self.add_node(val)
        if val2 not in self.graph:
            self.add_node(val2)

        if val2 in self.graph[val]:
            pass
        else:
            self.graph[val].append(val2)

    def has_node(self, val):
        """Check to see a given value is a node in the graph."""
        if val in self.nodes():
            return True
        return False

    def delete_node(self, val):
        """Delete node from the graph."""
        present = False
        for key in self.graph:
            if key is val:
                del self.graph[key]
                present = True
                break
        if not present:
            raise IndexError("Not in graph")
        for key in self.graph:
            if val in self.graph[key]:
                self.graph[key].remove(val)

    def delete_edge(self, val, val2):
        """Delete edge from the graph."""
        if self.has_node(val):
            if val2 in self.graph[val]:
                self.graph[val].remove(val2)
                return
            raise IndexError("No edge")
        raise IndexError("Value is not present in the graph in first Node.")

    def neighbors(self, val):
        """Return all the neighbors of given value."""
        neighbors = []
        if val not in self.graph:
            raise IndexError("not in graph")
        for key in self.graph:
            if val in self.graph[key]:
                neighbors.append(key)
        for item in self.graph[val]:
            if item not in neighbors:
                neighbors.append(item)
        return neighbors
