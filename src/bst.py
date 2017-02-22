"""An implementation of a binary search tree."""



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