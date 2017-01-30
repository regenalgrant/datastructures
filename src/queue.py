# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dll import DoublyLinkedList


class Queue(object):
    """Creating template for Queue."""

    def __init__(self, iterable=None):
        """Creating instances for the Queue."""
        self.dll = DoublyLinkedList(iterable)

    def enqueue(self, data):
        """Adding to the back list via appending."""
        self.dll.push(data)

    def dequeue(self):
        """Remove tail from the queue."""
        old_tail = self.dll.shift()
        if old_tail is None:
            raise IndexError("Queue is Empty")
        return old_tail.data

    def peek(self):
        """Return the value of the tail node."""
        if self.dll.tail is None:
            return
        return self.dll.tail.data

    # def size(self, data):
    #     """Size of the queue returning zero."""
    #     try:
    #         while data != self.dll.data:
    #             self.dll = self.dll.next_node
    #         return self.dll
    #     except AttributeError:
    #         return
