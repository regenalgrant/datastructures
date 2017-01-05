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
