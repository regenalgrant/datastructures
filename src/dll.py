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

    def pop(self):
        """Creating a pop method from DoublyLinkedList."""
        pop_head = self.head
        try:
            self.head.next_node.previous is None
            self.head = self.head.next_node
        except AttributeError:
            self.head is None
            self.tail is None
        return pop_head.data

    def append(self, data):
        """Appending the value at the tail of the list."""
        new_node = Node(data)
        new_node.next_node = None
        new_node.previous = self.tail
        if self.tail:
            self.tail.next_node = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def shift(self):
        """Creating a shift method to remove from the tail and return it."""
        shift_tail = self.tail
        try:
            self.tail = self.tail.previous
            self.tail.next_node = None
        except AttributeError:
            self.tail = None
            self.head = None
        return shift_tail

    def remove(self, value):
        """Create a 1st instance of a value remove from list starting with the head."""
        pointer = self.head
        try:
            while pointer.data != value:
                pointer = pointer.next_node
        except AttributeError:
            raise IndexError("Value does not exist in the list")
        if pointer.next_node is None and pointer.previous is None:
            self.head = None
            return
        if pointer.previous is None:
            self.head = pointer.next_node
        if pointer.previous:
            pointer.previous.next_node = pointer.next_node
        if pointer.next_node:
            pointer.next_node.previous = pointer.previous
        return pointer
