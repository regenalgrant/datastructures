"""Implementing BST."""
# -*- coding: utf-8 -*-
from collections import deque
import random
import time


class Node(object):
    """Creating class Node."""

    def __init__(self, data=None, right_child=None,left_child=None, parent=None):
        """Creating attributes upon initializion of class Node."""
        self.data = data
        self.right_child = right_child
        self.left_child = left_child
        self.parent = parent



class BST(object):
    """Creating class Binary Search Tree."""

    def __init__(self, data=None):
        if data is None:
            self.root = None
            return
        for item in data:
            self.insert(data)

    @property
    def parent(self):
        """Return Parent Property."""
        return self.parent

    @parent.setter
    def parent(self, node):
        """Set the parent of the node, and set parent child."""
        self.parent = node
        if node is None:
            self.parent = None
        elif isinstance(node, Node):
            if self.data and self.data > node.data:
                node.right_child = self
            else:
                node.left_child = self
        else:
            raise TypeError
    #
    # @property
    # def left(self):
    #     """left."""
    #     return self.left_child
    #
    #
    def left(self, node):
        """Set construct for left_child."""
        return self.left_child.left() if self.left_child else self
    #
    #
    # @property
    # def right_child(self):
    #     """right_child."""
    #     return self.right_child
    #
    #
    # @right_child.setter
    # def right_child(self, node):
    #     """Set construct for right_child."""
    #     self.right_child = node
    #     if node is not None:
    #         node.parent = self
    #
    #
    # def insert(self, data=None, node=None):
    #     """Add nodes to the binary search tree in proper location."""
    #     new_node = Node(data)
    #     if self.root is None:  #check node if none then empty
    #         self.root = new_node #if node then assign it
    #     if node is None:
    #         node = self.root
    #     if node.data > data:
    #         if node.left_child is None:
    #             node.left_child = new_node
    #         else:
    #             self.insert(data, node.left_child)
    #     if node.data < data:
    #         if node.right_child is None:
    #             node.right_child = new_node
    #         else:
    #             self.insert(data, node.right_child)
    #
    #
    # def search(self, data=None, node=None):
    #     """Creating the search method."""
    #     search_found = Node(data)
    #     if self.root is None:
    #         return None
    #     else:
    #         if self.root < data:
    #             return True
    #             self.root = search_found

    def size(self):
        """Return size property of tree."""
        return self.size


    def depth(self):
        """Create return number of levels in the tree."""
        left_child.depth = self.left_child_child.depth() if self.left_child else 0
        right_child.depth = self.right_child.depth() if self.right_child else 0
        return 1 + max(left_depth, right_child.depth)


    # def balance(self):
    #     """Creating number expressing balance tree."""
    #     left_depth = 0
    #     right_depth = 0
    #     if self.left_child is not None:
    #         left_depth = self.left.depth()
    #     if self.right_child is not None:
    #         right_depth = self.right_child.depth()
    #     return left_depth - right_depth


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
