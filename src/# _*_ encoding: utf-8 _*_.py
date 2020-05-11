

"""Binary Search Tree Implementation."""
from __future__ import unicode_literals
from queue import Queue
import random
import time


class Bst(object):
    """Implement Binary Search Tree."""

    def __init__(self, value=None, parent=None, left_child=None,
                 right_child=None):
        """Init Tree."""
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    @property
    def left_child(self):
        """Left child."""
        return self._left_child

    @left_child.setter
    def left_child(self, other_node):
        self._left_child = other_node
        if other_node is not None:
            other_node.parent = self

    @property
    def right_child(self):
        """Right child."""
        return self._right_child

    @right_child.setter
    def right_child(self, other_node):
        self._right_child = other_node
        if other_node is not None:
            other_node.parent = self

    def insert(self, value):
        """Insert value into tree if not present."""
        if self.contains(value):
            return
        if self.value is None:
            self.value = value
        try:
            if value > self.value:
                if not self.right_child:
                    self.right_child = Bst(parent=self, value=value)
                else:
                    self.right_child.insert(value)
            elif value < self.value:
                if not self.left_child:
                    self.left_child = Bst(parent=self, value=value)
                else:
                    self.left_child.insert(value)
        except TypeError:
            raise TypeError("Cannot mix types in a binary search tree.")

    def contains(self, value):
        """Return True if value in tree."""
        if self.value == value:
            return True
        left_contains = False
        right_contains = False
        if self.left_child is not None:
            left_contains = self.left_child.contains(value)
        if self.right_child is not None:
            right_contains = self.right_child.contains(value)
        return left_contains or right_contains

    def size(self):
        """Return size of tree."""
        if self.value is None:
            return 0
        if not self.left_child and not self.right_child:
            return 1
        sizes = [child.size()
                 for child in (self.left_child, self.right_child)
                 if child is not None]
        return sum(sizes) + 1

    def depth(self):
        """Return number of levels in the tree."""
        if self.value is None:
            return 0
        if not self.left_child and not self.right_child:
            return 1
        depths = [child.depth()
                  for child in (self.left_child, self.right_child)
                  if child is not None]
        return max(depths) + 1

    def balance(self):
        """Return number expressing balance or lack thereof of tree."""
        left_depth = 0
        right_depth = 0
        if self.left_child is not None:
            left_depth = self.left_child.depth()
        if self.right_child is not None:
            right_depth = self.right_child.depth()
        return left_depth - right_depth

#  -------------------------traverals------------------------

    def in_order(self):
        """Traverse tree with in-order traversal."""
        if self.left_child is not None:
            for item in self.left_child.in_order():
                yield item
        if self.value is not None:
            yield self.value
        if self.right_child is not None:
            for item in self.right_child.in_order():
                yield item

    def pre_order(self):
        """Traverse tree with pre-order traversal."""
        if self.value is not None:
            yield self.value
        if self.left_child is not None:
            for item in self.left_child.pre_order():
                yield item
        if self.right_child is not None:
            for item in self.right_child.pre_order():
                yield item

    def post_order(self):
        """Traverse tree with post-order traversal."""
        if self.left_child is not None:
            for item in self.left_child.post_order():
                yield item
        if self.right_child is not None:
            for item in self.right_child.post_order():
                yield item
        if self.value is not None:
            yield self.value

    def breadth_first(self):
        """Traverse tree with breadth-first traversal."""
        q = Queue()
        q.enqueue(self)
        while q.size() > 0:
            print(q.size())
            tree = q.dequeue()
            if tree.value is not None:
                yield tree.value
            if tree.left_child is not None:
                q.enqueue(tree.left_child)
            if tree.right_child is not None:
                q.enqueue(tree.right_child)


def delete(self, value):
        """Delete value from tree."""
        if self.value == value:
            deleteable = self
            nullable = ['left_child', 'right_child']
        elif self.left_child is not None and self.left_child.value == value:
            deleteable = self.left_child
            nullable = ['left_child']
        elif self.right_child is not None and self.right_child.value == value:
            deleteable = self.right_child
            nullable = ['right_child']
        try:
            deleteable.value = None
            vals = [val for val in deleteable.breadth_first()]
            for attr in nullable:
                setattr(self, attr, None)
            for val in vals:
                self.insert(val)
        # except NameError:
        #     for child in self._children():
        #         child.delete(value)
        # self.rebalance()


    if __name__ == "__main__":
        values = random.sample(range(1000), 100)
        big_tree = Bst()
        for val in values:
            big_tree.insert(val)
        search_val = random.choice(values)

        timescores = []
        for n in range(1000):
            start = time.time()
            big_tree.contains(search_val)
            delta = time.time() - start
            timescores.append((delta, search_val))

        timescores.sort()
        print("The fastest search took {} seconds for {}".format(*timescores[0]))
        print("The slowest search took {} seconds for {}".format(*timescores[-1]))
=======
"""Python graph."""

from deque import Deque
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


def add_node(self, val):
    """Add node to graph."""
    if val in self.graph:
        pass
    else:
        self.graph[val] = {}


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
        raise IndexError("Already not in graph")
    for key in self.graph:
        if val in self.graph[key]:
            del self.graph[key][val]


def delete_edge(self, val, val2):
    """Delete edge from the graph."""
    if self.has_node(val):
        if val2 in self.graph[val]:
            del self.graph[val][val2]
            return
        raise IndexError("No such edge")
    raise IndexError("Your first value is not present in the graph.")


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


def adjacent(self, val, val2):
    """Ensure value is connected to another by an edge."""
    if val not in self.graph or val2 not in self.graph:
        raise IndexError("Value not in graph.")
    edges_list = self.edges()
    if (val, val2) in edges_list or (val2, val) in edges_list:
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
    from test_graph import my_graph, deep_cyclic_graph
    print('Given the following cyclic graph:')
    print(deep_cyclic_graph().graph)
    print('The depth traversal will appear as follows:')
    print(deep_cyclic_graph().depth_traversal('A'))
    print('The breadth traversal will appear as follows:')
    print(deep_cyclic_graph().breadth_traversal('A'))
    print('On the other hand, given this short non-cyclic graph:')
    this_graph = my_graph()
    this_graph.add_edge("codefellows", "python")
    this_graph.add_edge("python", "javascript")
    this_graph.add_edge("codefellows", "css")
    print(this_graph.graph)
    print('The depth traversal will appear as follows:')
    print(this_graph.depth_traversal('codefellows'))
    print('The breadth traversal will appear as follows:')
    print(this_graph.breadth_traversal('codefellows'))

