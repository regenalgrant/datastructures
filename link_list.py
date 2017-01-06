class Node(object):
    """Creating a template for a Node."""

    def __init__(self, data):
        """providing attribute to Node."""
        self.data = data
        self.next_node = None


class Link_List(object):
    """Creating a template for Link List."""

    def __init__(self, data=None):
        """providing attribute of head is
        available upon for intitialization,
        if head is none iters through data."""
        self.head = None
        if data is not None:
            try:
                for info in data:
                    self.push(info)
            except TypeError:
                raise TypeError("need to add something")

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
            return None
