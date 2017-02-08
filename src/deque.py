"""Implementing A Deque."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dll import DoublyLinkedList


class Deque(object):
    """Creating template for deque."""

    def __init__(self, iterable=None):
        """Creating instances for the Deque."""
        self.dll = DoublyLinkedList(iterable)

    def append(self, data):
        """Appending the value at the tail of the deque."""
        self.dll.append(data)

    def appendleft(self, data):
        """Add a value to the front of the deque."""
        self.dll.push(data)

    def pop(self):
        """Remove a value from the tail of the deque and returns it."""
        old_tail = self.dll.shift()
        if old_tail is None:
            raise IndexError("Deque is Empty")
        return old_tail.data

    def popleft(self):
        """Remove a value from the front of the deque and returns."""
        old_head_value = self.dll.pop()
        if old_head_value is None:
            raise IndexError("Deque is Empty")
        return old_head_value

    def peek(self):
        """Return the value of the tail node."""
        if self.dll.tail is None:
            return
        return self.dll.tail.data

    def peekleft(self):
        """Next value that would be returned by popleft."""
        if self.dll.head is None:
            return
        return self.dll.head.data

    def size(self):
        """Size of the deque returning zero."""
        count = 0
        current = self.dll.head
        while current is not None:
            count += 1
            current = current.next_node
        return count
