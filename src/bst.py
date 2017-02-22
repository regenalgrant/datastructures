"""An implementation of a binary search tree."""
from deque import Deque


class Node(object):
    """Create node to for use in a binary search tree."""

    def __init__(self, value=None, left_child=None, right_child=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class BST(object):
    """The Binary search tree class."""

    def __init__(self, iterable=None):
        """Initialize a BST."""
        self.root = None
        self._size = 0
        if iterable and hasattr(iterable, "__iter__"):
            for i in iterable:
                self.insert(i)
        elif iterable:
            raise TypeError("Can't init with a non iterable."


    def insert(self, value):
        """Insert value into the binary search tree."""
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = Node(value)
            self._size += 1



    def _insert(self, value, node):
        if value == node.value:
            pass
        elif value > node.value:
            if node.right_child:
                self._insert(value, node.right_child)
            else:
                node.right_child = Node(value)
                self._size += 1
        else:
            if node.left_child:
                self._insert(value, node.left_child)
            else:
                node.left_child = Node(value)
                self._size += 


    def _search(self, value, node):
            if node.value == value:
                return node
            elif value > node.value:
                if node.right_child:
                    return self._search(value, node.right_child)
                else:
                    return None
            else:
                if node.left_child:
                    return self._search(value, node.left_child)
                else:
                    return None


