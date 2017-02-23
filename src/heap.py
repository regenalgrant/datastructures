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
