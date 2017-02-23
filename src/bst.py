# _*_ encoding: utf-8 _*_
"""Binary Search Tree Implementation."""
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
