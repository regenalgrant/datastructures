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
