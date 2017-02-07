
class Node(object):
    """Creating a template for a Node."""

    def __init__(self, data):
        """Providing attribute to Node."""
        self.data = data
        self.next_node = None


class LinkedList(object):
    """Creating a template for Link List."""

    def __init__(self, data=None):
        """
        Attribute of head available upon intitialization.
        If iterable date is available. Iters through data.
        """
        self.head = None
        if data is not None:
            try:
                for info in data:
                    self.push(info)
            except TypeError:
                raise TypeError("data must be iterable")

    def push(self, data):
        """Push data to head of list."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        """Pop head from linklist."""
        pop_old_node = self.head
        try:
            self.head = self.head.next_node
        except AttributeError:
            raise AttributeError("Cannot pop from empty list")
        return pop_old_node.data

    def size(self):
        """Size method finds length of linklist."""
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next_node
        return counter

    def search(self, data):
        """Searching for Node with a value."""
        current = self.head
        try:
            while data != current.data:
                current = current.next_node
            return current
        except AttributeError:
            return

    def remove(self, node):
        """Remove node from link list."""
        if self.head is None:
            raise IndexError("list is empty")
        current = self.head
        if current == node and current.next_node is not None:
            self.head = current.next_node
            current = None
            return self.head
        try:
            while current.next_node != node:
                current = current.next_node
            current.next_node = current.next_node.next_node
        except ValueError:
            raise IndexError("Error")

    def display(self):
        """Display unicode string of a tuple."""
        link_list_string = "("
        current = self.head
        while current:
            link_list_string = link_list_string + str(current.data) + ", "
            current = current.next_node
        link_list_string = link_list_string[:-2] + ")"
        return link_list_string
