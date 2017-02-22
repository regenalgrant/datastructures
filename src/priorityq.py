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
