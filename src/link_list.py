class Node(object):
    """Creating a template for a Node."""

    def __init__(self, data):
        """providing attribute to Node."""
        self.data = data
        self.next_node = None


class Link_List(object):
    """Creating a template for Link List."""

    def __init__(self, data=None):
        """Attribute of head is
        available upon intitialization,
        if iterable date is available, iters through data."""
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
            data.current = None
        except AttributeError:
            return

    def remove(self, node):
        """Remove node from link list."""
        current = self.head
        try:
            while node.data != current.data:
                previous = current
                current = current.next_node
            previous.next_node = current.next_node
        except AttributeError:
            raise IndexError("Error")


    def display(self):
        """Display unicode string of a tuple."""
        link_list_string = "("
        current = self.head
        while current:
            link_list_string = "".join(link_list_string + str(current.data) + ", ")
            current = current.next_node
        link_list_string = link_list_string[:-2] + ")"
        return link_list_string
