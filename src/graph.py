
# # _*_ encoding: utf-8 _*_
# """Python graph."""
#
# from deque import Deque
# from stack import Stack
# from queue import Queue
#
#
# class Graph(object):
#     """Class Graph."""
#
#
# def __init__(self):
#     """Initiatiliztion graph."""
#     self.graph = {}
#
#
# def node(self):
#     """Nodes in graph."""
#     node = []
#     for key in self.graph:
#         node.append(key)
#     return node
#
#
# def edges(self):
#     """List of edges in graph."""
#     return [{(key1, key2): self.graph[key1][key2]} for key1 in self.graph for key2 in self.graph[key1]]
#
#
# def add_node(self, val):
#     """Add node to graph."""
#     if val in self.graph:
#         pass
#     else:
#         self.graph[val] = {}
#
#
# def add_edge(self, val, val2):
#     """Add edge to graph."""
#     if val not in self.graph:
#         self.add_node(val)
#     if val2 not in self.graph:
#         self.add_node(val2)
#     if val2 in self.graph[val]:
#         pass
#     else:
#         self.graph[val].append(val2)
#
#
#
# def has_node(self, val):
#     """Check to see a given value is a node in the graph."""
#     if val in self.nodes():
#         return True
#     return False
#
#
# def delete_node(self, val):
#     """Delete node from the graph."""
#     present = False
#     for key in self.graph:
#         if key is val:
#             del self.graph[key]
#             present = True
#             break
#     if not present:
#         raise IndexError("Already not in graph")
#     for key in self.graph:
#         if val in self.graph[key]:
#             del self.graph[key][val]
#
#
# def delete_edge(self, val, val2):
#     """Delete edge from the graph."""
#     if self.has_node(val):
#         if val2 in self.graph[val]:
#             del self.graph[val][val2]
#             return
#         raise IndexError("No such edge")
#     raise IndexError("Your first value is not present in the graph.")
#
#
# def neighbors(self, val):
#     """Return all the neighbors of given value."""
#     neighbors = []
#     if val not in self.graph:
#         raise IndexError("not in graph")
#     for key in self.graph:
#         if val in self.graph[key]:
#             neighbors.append(key)
#     for item in self.graph[val]:
#         if item not in neighbors:
#             neighbors.append(item)
#     return neighbors
#
#
# def adjacent(self, val, val2):
#     """Ensure value is connected to another by an edge."""
#     if val not in self.graph or val2 not in self.graph:
#         raise IndexError("Value not in graph.")
#     edges_list = self.edges()
#     if (val, val2) in edges_list or (val2, val) in edges_list:
#         return True
#     return False
#
#
# def breadth_traversal(self, start):
#     """Breadth-first traversal of our graph."""
#     path = []
#     breadth_queue = Queue()
#     breadth_queue.enqueue(start)
#     try:
#         while start in self.graph:
#             current = breadth_queue.dequeue()
#             if current not in path:
#                 path = path + [current]
#                 for node in self.graph[current]:
#                     breadth_queue.enqueue(node)
#         return path
#     except (IndexError, KeyError):
#         return path
#
#     def depth_traversal(self, start):
#         """Depth-first traversal of our graph."""
#         path = []
#         depth_stack = Stack()
#         depth_stack.push(start)
#         try:
#             while start in self.graph:
#                 current = depth_stack.pop()
#                 if current not in path:
#                     path = path + [current]
#                     for node in self.graph[current]:
#                         depth_stack.push(node)
#             return path
#         except (IndexError, KeyError):
#             return path
#
#
# if __name__ == '__main__':
#     from test_graph import my_graph, deep_cyclic_graph
#     print('Given the following cyclic graph:')
#     print(deep_cyclic_graph().graph)
#     print('The depth traversal will appear as follows:')
#     print(deep_cyclic_graph().depth_traversal('A'))
#     print('The breadth traversal will appear as follows:')
#     print(deep_cyclic_graph().breadth_traversal('A'))
#     print('On the other hand, given this short non-cyclic graph:')
#     this_graph = my_graph()
#     this_graph.add_edge("codefellows", "python")
#     this_graph.add_edge("python", "javascript")
#     this_graph.add_edge("codefellows", "css")
#     print(this_graph.graph)
#     print('The depth traversal will appear as follows:')
#     print(this_graph.depth_traversal('codefellows'))
#     print('The breadth traversal will appear as follows:')
#     print(this_graph.breadth_traversal('codefellows'))
=======
# _*_ encoding: utf-8 _*_
"""Python graph."""

from stack import Stack
from queue import Queue


class Graph(object):
    """Class Graph."""


    def __init__(self):
        """Initiatiliztion graph."""
        self.graph = {}


    def node(self):
        """Nodes in graph."""
        node = []
        for key in self.graph:
            node.append(key)
        return node


    def edges(self):
        """List of edges in graph."""
        return [{(key1, key2): self.graph[key1][key2]} for key1 in self.graph for key2 in self.graph[key1]]


    def add_node(self, value):
        """Add node to graph."""
        if value in self.graph:
            pass
        else:
            self.graph[value] = {}


    def add_edge(self, value, value2):
        """Add edge to graph."""
        if value not in self.graph:
            self.add_node(value)
        if value2 not in self.graph:
            self.add_node(value2)
        if value2 in self.graph[value]:
            pass
        else:
            self.graph[value].append(value2)


    def has_node(self, value):
        """Check to see a given value is a node in the graph."""
        if value in self.nodes():
            return True
        return False


    def delete_node(self, value):
        """Delete node from the graph."""
        present = False
        for key in self.graph:
            if key is value:
                del self.graph[key]
                present = True
                break
        if not present:
            raise IndexError("Already not in graph")
        for key in self.graph:
            if value in self.graph[key]:
                del self.graph[key][value]


    def delete_edge(self, value, value2):
        """Delete edge from the graph."""
        if self.has_node(value):
            if value2 in self.graph[value]:
                del self.graph[value][value2]
                return
            raise IndexError("No such edge")
        raise IndexError("Your first value is not present in the graph.")


    def neighbors(self, value):
        """Return all the neighbors of given value."""
        neighbors = []
        if value not in self.graph:
            raise IndexError("not in graph")
        for key in self.graph:
            if value in self.graph[key]:
                neighbors.append(key)
        for item in self.graph[value]:
            if item not in neighbors:
                neighbors.append(item)
        return neighbors


    def adjacent(self, value, value2):
        """Ensure valueue is connected to another by an edge."""
        if value not in self.graph or value2 not in self.graph:
            raise IndexError("Value not in graph.")
        edges_list = self.edges()
        if (value, value2) in edges_list or (value2, value) in edges_list:
            return True
        return False


    def breadth_traversal(self, start):
        """Breadth-first traversal of our graph."""
        path = []
        breadth_queue = Queue()
        breadth_queue.enqueue(start)
        try:
            while start in self.graph:
                current = breadth_queue.dequeue()
                if current not in path:
                    path = path + [current]
                    for node in self.graph[current]:
                        breadth_queue.enqueue(node)
            return path
        except (IndexError, KeyError):
            return path

    def depth_traversal(self, start):
        """Depth-first traversal of our graph."""
        path = []
        depth_stack = Stack()
        depth_stack.push(start)
        try:
            while start in self.graph:
                current = depth_stack.pop()
                if current not in path:
                    path = path + [current]
                    for node in self.graph[current]:
                        depth_stack.push(node)
            return path
        except (IndexError, KeyError):
            return path


    if __name__ == '__main__':
        from test_graph import native_graph, deep_cyclic_graph
        print('Given the following cyclic graph:')
        print(deep_cyclic_graph().graph)
        print('The depth traversal will appear as follows:')
        print(deep_cyclic_graph().depth_traversal('A'))
        print('The breadth traversal will appear as follows:')
        print(deep_cyclic_graph().breadth_traversal('A'))
        print('On the other hand, given this short non-cyclic graph:')
        this_graph = native_graph()
        this_graph.add_edge("codefellows", "python")
        this_graph.add_edge("python", "javascript")
        this_graph.add_edge("codefellows", "css")
        print(this_graph.graph)
        print('The depth traversal will appear as follows:')
        print(this_graph.depth_traversal('codefellows'))
        print('The breadth traversal will appear as follows:')
        print(this_graph.breadth_traversal('codefellows'))

