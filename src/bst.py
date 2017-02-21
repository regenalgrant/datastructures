"""Implementing BST"""
# -*- coding: utf-8 -*-

from  collections import deque




class Node(object):
    """Creating class Node."""

    def __init__(self, data, right=None,left=None, parent=None):
        """Creating attributes upon initializion of class Node."""
        self.data = data
        self.right = right
        self.left = left
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
    def left(self):
        """Left."""
        return self.left


    @left.setter
    def left(self, node):
        """Set construct for left."""
        self.left = node
        if node is not None:
            node.parent = self


    @property
    def right(self):
        """Right."""
        return self.right


    @right.setter
    def right(self, node):
        """Set construct for right."""
        self.right = node
        if node is not None:
            node.parent = self


    def insert(self, data=None, node=None):
        """Add nodes to the binary search tree in proper location."""
        new_node = Node(data)
        if self.root is None:  #check node if none then empty
            self.root = new_node #if node then assign it
        if node is None:
            node = self.root
        if node.data > data:
            if node.left is None:
                node.left = new_node
            else:
                self.insert(data, node.left)
        if node.data < data:
            if node.right is None:
                node.right = new_node
            else:
                self.insert(data, node.right)


    def search(self, data=None, node=None):
        """Creating the search method."""
        search_found = Node(data)
        if self.root is None:
            return None
        else:
            if self.root < data:
                return True
                self.root = search_found


    def contains(self, value):
        """Return True if value in tree."""
        if self.value == value:
            return True
        left.contains = False
        right.contains = False
        if self.left is not None:
            left.contains = self.left.contains(value)
        if self.right is not None:
            right.contains = self.right.contains(value)
        return left.contains or right.contains

    def size(self):
        """Return size of tree."""
        if self.data is None:
            return 0
        if not self.left and not self.right:
            return 1
        sizes = [node.size()
                 for node in (self.left, self.right)
                 if node is not None]
        return sum(sizes) + 1
