"""Implementing BST"""
# -*- coding: utf-8 -*-


class Node(object):
    """Creating class Node."""

    def __init__(self, data, right=None,left=None, parent=None):
        """Creating attribution to initializion to be used in the class Node."""
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

    def insert(self, data=None, node=None):
        """Creating the Insert method."""
        new_node = Node(data)
        if self.root is None
            self.root = new_node
        if node is None:
            node = self.root
        if node.data > data:
            if node.left is None:
                node.left = new_node
            else:
                insert(data, node.left)
        if node.data < data:
            if node.right is None:
                node.right = new_node
            else:
                insert(data, node.right)


    # def search(self, data=None, node=None):
    #     """Creating the search method."""
    #     current = Node(data)
    #     try:
    #         while data != current.data:
    #             current.data
    #
    #
    #     if self.root is None
    #         self.root = current
