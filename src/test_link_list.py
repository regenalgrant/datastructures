from __future__ import unicode_literals
import pytest
from link_list import LinkedList, Node


def test_init():
    """testing for init method of linklist."""
    test_instance = LinkedList([1, 2, 3, 4])
    assert test_instance.head.data == 4

def test_non_iter_init():
    """Testing for non-iterable data."""
    with pytest.raises(TypeError) as message:
        test_instance = LinkedList(1)
    assert "data must be iterable" in str(message)


def test_push():
    """Testing push node to the link list."""
    test_instance = LinkedList()
    test_instance.push(10)
    assert test_instance.head.data == 10
    assert test_instance.head is not None


def test_pop():
    """Testing pop node off the head."""
    test_instance = LinkedList("newhead")
    assert test_instance.pop() == "d"


def test_pop_empty_list():
    """Test for error message when popping empty list."""
    test_instance = LinkedList()
    with pytest.raises(AttributeError) as message:
        test_instance.pop()
    assert "Cannot pop from empty list" in str(message)


def test_size():
    """Testing size method for linklist."""
    test_instance = LinkedList([1, 2, 3, 4])
    assert test_instance.size() == 4


def test_search_value_not_list():
    """"Testing for value not found in list."""
    test_instance = LinkedList("NotHere")
    test_node = Node("notnode")
    assert test_instance.search(test_node.data) is None


def test_search_value():
    """Testing a value for value Node in a list."""
    test_instance = LinkedList("IamHere")
    test_node = Node("I")
    assert test_instance.search(test_node.data).data == "I"


def test_remove():
    """Testing node being actually removed from the list."""
    test_instance = LinkedList("list")
    search_node = test_instance.search("s")
    test_instance.remove(search_node)
    assert test_instance.head.next_node.data == 'i'


def test_remove_head():
    """Testing that node in the head is being removed."""
    test_instance = LinkedList("list")
    search_node = test_instance.search("t")
    test_instance.remove(search_node)
    assert test_instance.head.data == "s"


def test_remove_from_empty_list():
    """Testing for error when trying remove from an empty list."""
    test_instance = LinkedList()
    search_node = Node("s")
    with pytest.raises(IndexError) as message:
        test_instance.remove(search_node)
    assert "list is empty" in str(message)


def test_remove_node_far_head():
    """Testing for a removal of a node that is not close to head."""
    test_instance = LinkedList("people")
    search_node = test_instance.search("o")
    test_instance.remove(search_node)
    test_instance.pop()
    test_instance.pop()
    test_instance.pop()
    assert test_instance.head.data == "e"


def test_remove_value_not_found():
    """Testing for an error message when node to be removed not found."""
    test_instance = LinkedList("list")
    search_node = Node("u")
    with pytest.raises(IndexError)as message:
        test_instance.remove(search_node)
    assert "Value not found in list" in str(message)


def test_display():
    """Testing display returning a unicode within string."""
    test_instance = LinkedList("data")
    assert test_instance.display() == "(a, t, a, d)"
