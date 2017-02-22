"""Create priority queue."""


class P_Q(object):
    """
    Create a class of priority queue."""

    def __init__(self, iterable=None):
        """Creates an instance of the Priority_Q class."""
        self._priorityq = []
        if iterable and hasattr(iterable, "__iter__"):
            for i in iterable:
                self.insert(i[0], i[1])
        elif iterable:
            raise TypeError("Can't init with a non iterable.")


    def insert(self, value, priority=0):
        """Insert value into list."""
        self._priorityq.append((value, priority))


    def pop(self):
    """Remove high priority from the queue."""
    if not self._priorityq:
        raise IndexError("You may not pop from an empty queue.")
    top_priority = sorted(self._priorityq, key=lambda x: x[1])
    self._priorityq.remove(top_priority[0])


    def peek(self):
    """Return high priority from the queue."""
    if not self._priorityq:
        raise IndexError("You may not peek from an empty queue.")
    top_priority = sorted(self._priorityq, key=lambda x: x[1])
    return top_priority[0]




