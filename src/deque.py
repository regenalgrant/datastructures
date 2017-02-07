# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dll import DoublyLinkedList


class Deque(object):
    """Creating template for deque."""

    def __init__(self, iterable=None):
        """Creating instances for the Deque."""
        self.dll = DoublyLinkedList(iterable)

    # def append(self, data):
    #     """Appending the value at the tail of the deque."""
    #     self.dll.append(data)
    #
    # def appendleft(self, data):
    #     """Adds a value to the front of the deque."""
    #     self.dll.append
    #
    # # def pop():
    # #     """Removes a value from the tail of the deque and returns."""
    # #
    # # def pop_left():
    # #     """removes a value from the front of the deque and returns."""
    #
    # def peek(self):
    #     """Return the value of the tail node."""
    #     if self.dll.tail is None:
    #         return
    #     return self.dll.tail.data
    #
    # # def peek_left():
    # #     Next value that would be returned by popleft
    #
    # def size(self):
    #     """Size of the deque returning zero."""
    #     count = 0
    #     current = self.dll.head
    #     while current is not None:
    #         count += 1
    #         current = current.next_node
    #     return count
