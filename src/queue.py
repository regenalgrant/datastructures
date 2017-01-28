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
        try:
            old_tail = self.dll.shift()
            old_tail = old_tail.data
        except AttributeError:
            raise IndexError("Queue is Empty")
        return old_tail
