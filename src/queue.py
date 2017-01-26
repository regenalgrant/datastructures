# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dll import DoublyLinkedList


class Queue(object):
    """Creating template for Queue."""

    def __init__(self, head=None, value=None, iterable=None):
        """Creating instances for the Queue."""
        self.head = DoublyLinkedList(iterable)

    # def enqueue(self, value):
    #     """Adding to the back list via appending."""
    #     self.queue.append(value)
