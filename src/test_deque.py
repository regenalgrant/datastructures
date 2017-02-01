# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from deque import Deque


#---------------------peek---------------------------
def test_peek_on_deque():
    """Test peek on deque."""
    test_deque = Deque([1, 2, 3, 4])
    peek_tail_data = test_deque.peek()
    assert peek_tail_data == test_deque.dll.tail.data

def test_peek_on_empty_deque():
    """Testing peek on an empty deque."""
    test_deque = Deque()
    peek_tail = test_deque.peek()
    assert peek_tail is None
# ------------------size------------------------------
def test_length_of_empty_deque():
    """Check that length of empty deque returns 0."""
    test_deque = Deque()
    assert test_deque.size() == 0

def test_deque_size():
    """Test that list initialized with data."""
    test_deque = Deque([1, 2, 3, 4])
    assert test_deque.size() == 4
#-------------------append----------------------------
def test_append_value_to_tail():
    """Testing append a value to the tail of the deque."""
    test_deque = Deque([1, 2, 3, 4])
    test_deque.append(5)
    assert test_deque.append.tail.data() == 5
