# -*- coding: utf-8 -*-
"""Prioityq Class."""


class PriorityQueue:
    """PriorityQ Class."""

    def __init__(self):
        """Priority Queue constructor method."""
        self.dict = {}


    def insert(self, data, priority):
        """Priority Queue insert method."""
        if not isinstance(priority, int):
            raise TypeError("Priority must be an integer")
        if priority in self.dict:
            self.dict[priority].append(data)
        else:
            self.dict[priority] = [data]
        print(self.dict)


    def pop(self):
        """Priority Queue pop method."""
        if len(self.dict):
            cursor = 0
            while cursor not in self.dict:
                cursor += 1
            next_node = self.dict[cursor][0]
            self.dict[cursor] = self.dict[cursor][1:]
            return next_node
        else:
            raise IndexError("The Priority Queue is empty")
