# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    """Creating a template for a Node."""

    def __init__(self, data=None, next_node=None, previous=None):
        """Providing attributes to Node."""
        self.data = data
        self.next_node = next_node
        self.previous = previous


class DoublyLinkedList(object):
    """Creating template for DoublyLinkedList."""

    def __init__(self, data=None):
        """Providing a base-line for DoublyLinkedList."""
        self.head = None
        self.tail = None
        try:
            if data:
                for i in data:
                    self.push(i)
        except TypeError:
            raise IndexError("Need to pass an iterable value")

    def push(self, data):
        """Creating a push method that adds a new node to head of the DoublyLinkedList."""
        new_node = Node(data)
        new_node.previous = None
        new_node.next_node = self.head
        if self.head:
            self.head.previous = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    # def pop(self, data):
    #     """Creating a pop method from DoublyLinkedList."""
    #     pop_old_node = self.node
    #     try:
    #         self.head = self.head.next_node
    #     except TypeError:
    #         raise AttributeError("Cannot pop from empty list")
    #     return pop_old_node.data
