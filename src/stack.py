
from __future__ import unicode_literals
from link_list import LinkedList



class Stack(object):
    """implemention of a stack class."""

    def __init__(self, data=None):
        """Init stack, with nodes containing information
        provided as long as data is iterable.
        """
        self.linklist = LinkedList(data)

    def push(self, data):
        """Push method add a node to stack."""
        self.linklist.push(data)

    
