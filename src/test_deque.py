# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from deque import Deque

TEST_DEQUE_DATA = [
    ([1, 2, 3, 4], 4),
    ("elephant", "t")
    ]

@pytest.mark.parametrize("iterable, output", TEST_DEQUE_DATA)
def test_deque_init(iterable, output):
    """Test for initialize deque."""
    test_deque = deque(iterable)
    assert test_deque.dll.head.data == output

@pytest.mark.parametrize("iterable, output", TEST_DEQUE_DATA)
def test_enqueue_on_extisting_deque(iterable, output):
    """Testing enqueue on extisting deque."""
    test_deque = deque(iterable)
    test_deque.enqueue(9)
    assert test_deque.dll.head.data == 9

# #---------------------peek---------------------------
# def test_peek_on_deque():
#     """Test peek on deque."""
#     test_deque = Deque([1, 2, 3, 4])
#     peek_tail_data = test_deque.peek()
#     assert peek_tail_data == test_deque.dll.tail.data
#
# def test_peek_on_empty_deque():
#     """Testing peek on an empty deque."""
#     test_deque = Deque()
#     peek_tail = test_deque.peek()
#     assert peek_tail is None
# # ------------------size------------------------------
# def test_length_of_empty_deque():
#     """Check that length of empty deque returns 0."""
#     test_deque = Deque()
#     assert test_deque.size() == 0
#
# def test_deque_size():
#     """Test that list initialized with data."""
#     test_deque = Deque([1, 2, 3, 4])
#     assert test_deque.size() == 4
#-------------------append----------------------------
# def test_append_to_deque():
#     """Testing append a value to the tail of the deque."""
#     test_deque = Deque(TEST_DEQUE_DATA)
#     test_deque.append.head(5)
#     assert test_deque.append.head == 5
