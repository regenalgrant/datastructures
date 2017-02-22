"""Implementing BST."""
# -*- coding: utf-8 -*-
from collections import deque
import random
import time


class Node(object):
    """Creating class Node."""

    def __init__(self, val):
        """Creating attributes upon initializion of class Node."""
        self.value = val
        self.left = None
        self.right = None
        self.depth = 1



class BST(object):
    """Creating class Binary Search Tree."""
    self.head = None
    self.counter = 0
    if iterable is not None:
            try:
                for item in iterable:
                    self.insert(item)
            except TypeError:
                self.insert(iterable)


    def _insert_node(self, new_node):
            """Insert a new node new node must be an instance of Node."""
            parent = self
            visited_nodes = [self]
            while True:
                if parent.value == new_node.value:
                    break
                if new_node.value > parent.value:
                    if parent.right is None:
                        parent.right = new_node
                        while len(visited_nodes) != 0:
                            visited_node = visited_nodes.pop()
                            visited_node.depth = visited_node.find_depth()
                        break
                    else:
                        parent = parent.right
                        visited_nodes.append(parent)
                elif new_node.value < parent.value:
                    if parent.left is None:
                        parent.left = new_node
                        while len(visited_nodes) != 0:
                            visited_node = visited_nodes.pop()
                            visited_node.depth = visited_node.find_depth()
                        break
                    else:
                        parent = parent.left
                        visited_nodes.append(parent)


    def balance(self):
        """Creating number expressing balance tree."""
        if self.head is None:
            return 0
        if self.head.left is not None:
            left_depth = self.head.left.depth
        else:
            left_depth = 0
        if self.head.right is not None:
            right_depth = self.head.right.depth
        else:
            right_depth = 0
        return left_depth - right_depth


    def contains(self, value):
    """Value in the bst if False."""
    new_node = Node(value)
    if self.head is None:
        return False
    else:
        if new_node._compare_nodes(self.head):
            return True
        else:
            return False

# if __name__ == "__main__":
#     data = random.sample(range(1000), 100)
#     root = BST()
#     for val in data:
#         root.insert(val)
#     search_val = random.choice(data)
#
#     timescores = []
#     for n in range(1000):
#         start = time.time()
#         root.contains(search_val)
#         delta = time.time() - start
#         timescores.append((delta, search_val))
#
#     timescores.sort()
#     print("The fastest search {} seconds for {}".format(*timescores[0]))
#     print("The slowest search {} seconds for {}".format(*timescores[-1]))
