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

# def test_append_method():
    """Testing for method appending value to a node."""
    # test_instance = DoublyLinkedList()
    # test_instance.append(4)
    # assert test_instance.append.data == 4

# def test_append_to_tail():
    """Testing for method to append value to the tail."""
    # test_instance = DoublyLinkedList()
    # test_instance.append(10)
    # assert test_instance.append.tail.data == 10
    # assert test_instance.append.tail is not None

#
# def test_shift_method():
    # test_instance = DoublyLinkedList()
#
# def test_remove_method():
# test_instance = DoublyLinkedList("list")
# search_node = test_instance.search("s")
# test_instance.remove(search_node)
# assert test_instance.head.next_node.data == 'i'
