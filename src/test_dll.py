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
        test_instance = DoublyLinkedList("l")
    assert "Need to pass an iterable value" in str(message)

def test_push_method():
    """Testing for nodes are being added the head of list."""
    test_instance = DoublyLinkedList("word")
    test_instance.push("two")
    assert test_instance.head.data == "two"

def test_push_return():

def test_pop_method():

def test_pop_retun():

def test_pop_empty():

def test_push_empty():

def test_append_method():
def test_append_to_tail():

def test_shift_method():

def test_remove_method():
