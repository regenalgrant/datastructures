# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dll import DoublyLinkedList, Node
import pytest

def test_init_check_head():
    """Testing for init functions on DoubleyLinkedList."""
    test_instance = DoublyLinkedList("double")
    assert test_instance.head.data == "e"

def test_init_check_tail():
    """Testing for init functions on DoubleyLinkedList."""
    test_instance = DoublyLinkedList("double")
    assert test_instance.tail.data == "d"

def test_init_not_iterable():
    """Testing for non-iterable data."""
    with pytest.raises(IndexError) as message:
        test_instance = DoublyLinkedList(7)
    assert "Need to pass an iterable value" in str(message)

def test_push_existing_list():
    """Testing for nodes are being added the head of list."""
    test_instance = DoublyLinkedList("word")
    test_instance.push("two")
    assert test_instance.head.data == "two"

def test_push_empty():
    """Testing for push node to an empty list."""
    test_instance = DoublyLinkedList()
    test_instance.push(1)
    assert test_instance.head.data == test_instance.tail.data

def test_push_mutiple_nodes():
    """Testing for push method mutiple time."""
    test_instance = DoublyLinkedList()
    test_instance.push(4)
    test_instance.push(5)
    test_instance.push(6)
    test_instance.push(7)
    assert test_instance.head.next_node.data == test_instance.tail.previous.previous.data

def test_push_pop():
    """Testing both pushing and popping nodes on a DoublyLinkedList."""
    test_instance = DoublyLinkedList()
    test_instance.push(4)
    popped_head = test_instance.pop()
    assert popped_head == 4

def test_pop():
    """testing for pop method."""
    test_instance = DoublyLinkedList([1, 2, 3, 4])
    test_instance.pop()
    assert test_instance.head.data == 3

def test_append_empty_list():
    """Testing for method appending node to empty list."""
    test_instance = DoublyLinkedList()
    test_instance.append(4)
    assert test_instance.tail.data == 4

def test_append_to_existing_list():
    """Testing for method to append node to the tail of a existing list."""
    test_instance = DoublyLinkedList({"bob": "her",
                                      "jack": "danials"})
    test_instance.append(10)
    assert test_instance.tail.data == 10

def test_append_single_in_list():
    """Test append of a node on a tail of a list with one node."""
    test_instance = DoublyLinkedList({"bob": "hairy"})
    test_instance.append(4)
    assert test_instance.tail.data == 4

def test_shift_from_empty_list():
    """Testing a method of removal of a node from a empty list."""
    test_instance = DoublyLinkedList()
    tail_test = test_instance.shift()
    assert tail_test is None

def test_shift_to_existing_list():
    """Testing a method of shift to a existing list."""
    test_instance = DoublyLinkedList([1, 2, 3, 4])
    test_instance.shift()
    assert test_instance.tail.data == 2

def test_shift_after_append():
    """Testing shift after append on a DoublyLinkedList."""
    test_instance = DoublyLinkedList([1, 2, 3, 4])
    test_instance.append(5)
    test_instance.shift()
    assert test_instance.tail.data == 1

def test_remove_from_existing_list():
    """Testing for node removal from the existing list."""
    test_instance = DoublyLinkedList([1, 2, 3, 4])
    test_instance.remove(4)
    assert test_instance.head.data == 3

def test_remove_empty_list():
    """Testing method of removel node to empty list."""
    test_instance = DoublyLinkedList()
    with pytest.raises(IndexError) as message:
        test_instance.remove(5)
    assert "Value does not exist in the list" in str(message)

def test_remove_not_head():
    """Testing a value that is not head."""
    test_instance = DoublyLinkedList([1, 2, 3, 4])
    test_instance.remove(2)
    assert test_instance.head.next_node.next_node.data == 1

def test_remove_single_node_list():
    """Testing remove method on a list with only one node."""
    test_instance = DoublyLinkedList([1])
    test_instance.remove(1)
    assert test_instance.head is None
