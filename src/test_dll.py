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
    """Testing is push node to a empty list."""
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



# def test_pop():
#
# def test_pop_retun():
#
# def test_pop_empty():

#
# def test_append_method():
# def test_append_to_tail():
#
# def test_shift_method():
#
# def test_remove_method():
