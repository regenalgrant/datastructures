# _*_ encoding: utf-8 _*_
"""Binary Search Tree Implementation."""

from queue import Queue
import random
import time


class Bst(object):
    """Implement Binary Search Tree."""

    def __init__(self, value=None, parent=None, left_child=None,
                 right_child=None):
        """Init Tree."""
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    @property
    def left_child(self):
        """Left child."""
        return self._left_child

    @left_child.setter
    def left_child(self, other_node):
        self._left_child = other_node
        if other_node is not None:
            other_node.parent = self

    @property
    def right_child(self):
        """Right child."""
        return self._right_child

    @right_child.setter
    def right_child(self, other_node):
        self._right_child = other_node
        if other_node is not None:
            other_node.parent = self

    def _children(self):
        """Yield any children which are not None."""
        for child in (self.left_child, self.right_child):
            if child is not None:
                yield child

    def insert(self, value):
        """Insert value into tree if not present."""
        if self.value is None:
            self.value = value
        if not isinstance(value, type(self.value)):
            raise TypeError("Cannot mix types in a binary search tree.")
        if value == self.value:
            return
        if value > self.value:
            insert_name = "right_child"
        else:
            insert_name = "left_child"
        insert_child = getattr(self, insert_name)
        if insert_child is None:
            setattr(self, insert_name, Bst(parent=self, value=value))
        else:
            insert_child.insert(value)
        self.rebalance()

#--------------trie-------------------------

    def rebalance(self):
        """Rotate in place as necessary to ensure tree is balanced."""
        new_balance = self.balance()
        if new_balance < -1:
            self._rotate_left()
        elif new_balance > 1:
            self._rotate_right()

    def _rotate_left(self):
        pivot = self.right_child
        if pivot.balance() > 0:
            pivot._rotate_right()
        rr_grandchild = pivot.right_child
        other_node = self.left_child
        floater = pivot.left_child

        self.value, pivot.value = pivot.value, self.value
        self.right_child = rr_grandchild

        if other_node is not None:
            other_node.parent = floater
        pivot.right_child, pivot.left_child = floater, other_node

        self.left_child = pivot

    def _rotate_right(self):
        pivot = self.left_child
        if pivot.balance() < 0:
            pivot._rotate_left()
        ll_grandchild = pivot.left_child
        other_node = self.right_child
        floater = pivot.right_child

        self.value, pivot.value = pivot.value, self.value
        self.left_child = ll_grandchild

        if other_node is not None:
            other_node.parent = floater
        pivot.left_child, pivot.right_child = floater, other_node

        self.right_child = pivot

#-------------------bst------------------------------

    def _search(self, value):
        """Search for value in tree."""
        if self.value == value:
            return self
        for child in self._children():
            result = child._search(value)
            if result:
                return result
        return None

    def contains(self, value):
        """Return True if value in tree."""
        return bool(self._search(value))

    def size(self):
        """Return size of tree."""
        if self.value is None:
            return 0
        sizes = [child.size() for child in self._children()]
        return sum(sizes + [1])

    def depth(self):
        """Return number of levels in the tree."""
        if self.value is None:
            return 0
        depths = [child.depth() for child in self._children()] or [0]
        return max(depths) + 1

    def balance(self):
        """Return number expressing balance or lack thereof of tree."""
        left_depth = 0
        right_depth = 0
        if self.left_child is not None:
            left_depth = self.left_child.depth()
        if self.right_child is not None:
            right_depth = self.right_child.depth()
        return left_depth - right_depth

    def in_order(self):
        """Traverse tree with in-order traversal."""
        if self.left_child is not None:
            for item in self.left_child.in_order():
                yield item
        if self.value is not None:
            yield self.value
        if self.right_child is not None:
            for item in self.right_child.in_order():
                yield item

    def pre_order(self):
        """Traverse tree with pre-order traversal."""
        if self.value is not None:
            yield self.value
        for child in self._children():
            for item in child.pre_order():
                yield item

    def post_order(self):
        """Traverse tree with post-order traversal."""
        for child in self._children():
            for item in child.post_order():
                yield item
        if self.value is not None:
            yield self.value

    def breadth_first(self):
        """Traverse tree with breadth-first traversal."""
        q = Queue()
        q.enqueue(self)
        while q.size() > 0:
            tree = q.dequeue()
            if tree.value is not None:
                yield tree.value
            for child in tree._children():
                q.enqueue(child)

#------------------delete--------------------------------

    def delete(self, value):
        """Delete value from tree."""
        if self.value == value:
            deleteable = self
            nullable = ['left_child', 'right_child']
        elif self.left_child is not None and self.left_child.value == value:
            deleteable = self.left_child
            nullable = ['left_child']
        elif self.right_child is not None and self.right_child.value == value:
            deleteable = self.right_child
            nullable = ['right_child']
        try:
            deleteable.value = None
            vals = [val for val in deleteable.breadth_first()]
            for attr in nullable:
                setattr(self, attr, None)
            for val in vals:
                self.insert(val)
        except NameError:
            for child in self._children():
                child.delete(value)
        self.rebalance()

#------------------timit-----------------------------

if __name__ == "__main__":
    values = random.sample(range(1000), 100)
    big_tree = Bst()
    for val in values:
        big_tree.insert(val)
    search_val = random.choice(values)

    timescores = []
    for n in range(1000):
        start = time.time()
        big_tree.contains(search_val)
        delta = time.time() - start
        timescores.append((delta, search_val))

    timescores.sort()
    print("The fastest search in {} seconds for {}".format(*timescores[0]))
    print("The slowest search in {} seconds for {}".format(*timescores[-1]))
