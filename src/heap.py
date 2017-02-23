#  _*_coding:utf-8 _*_
"""Create a heap data structure."""
from __future__ import division
import math


class Heap(object):
    """Create class Heap."""

    def __init__(self):
        """Initilializating for Heap class."""
        self.high_low = []

    def get_parent(self, index):
        """Index number of Node's parent."""
        return (index - 1) // (2)

    def get_left(self, index):
        """Left child."""
        return 2 * index + 1

    def get_right(self, index):
        """Right child."""
        return 2 * index + 2

    def compare_parent(self, index):
        """Compare node it parent."""
        while True:
            left = self.get_left(index)
            right = self.get_right(index)
            if left <= len(self.high_low) and self.high_low[left] > self.high_low[index]:
                largest = left
            else:
                largest = index
            if right <= len(self.high_low) and self.high_low[right] > self.high_low[largest]:
                largest = right
            if largest != index:
                temp = self.high_low[index]
                self.high_low[index] = self.high_low[largest]
                self.high_low[largest] = temp
            else:
                break
