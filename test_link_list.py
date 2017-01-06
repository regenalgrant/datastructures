from __future__ import unicode_literals
import pytest 
from link_list import Link_List, Node


def test_init():
    """testing for init method of linklist."""
    test_instance = Link_List([1, 2, 3, 4])
    assert test_instance.head.data == 4


def test_push():
    """Testing push node to the link list."""
    test_instance = Link_List()
    test_instance.push(10)
    assert test_instance.head.data == 10
    assert test_instance.head is not None


def test_pop():
    """Testing pop node off the head."""
    test_instance = Link_List("newhead")
    assert test_instance.pop() == "d"


def test_pop_empty_list():
    """Test for error message when popping empty list."""
    test_instance = Link_List()
    with pytest.raises(AttributeError) as message:
        test_instance.pop()
    assert "Cannot pop from empty list" in str(message)


def test_size():
    """Testing size method for linklist."""
    test_instance = Link_List([1, 2, 3, 4])
    assert test_instance.size() == 4


def test_search_value_not_list():
    """"Testing for value."""
    test_instance = Link_List("NotHere")
    test_node = Node("notnode")
    with pytest.raises(IndexError) as message:
            test_instance.search(test_node.data)
    assert "Did not find value" in str(message)


def test_search_value():
    """Searching a value in a Node."""
    test_instance = Link_List("IamHere")
    test_node = Node("I")
    assert test_instance.search(test_node.data).data == "I"







