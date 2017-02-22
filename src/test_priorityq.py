# -*- coding: utf-8 -*-
"""Prioityq tests."""
import pytest


def test_insert():
    """Test insert method."""
    from priorityq import PriorityQueue
    test_instance = PriorityQueue()
    test_instance.insert('data', 1)
    assert test_instance.dict[1] == ['data']


# def test_pop_empty():
#     """Test pop from empty PQ raises index error."""
#     from priorityq import PriorityQueue
#     test_instance = PriorityQueue()
#     with pytest.raises(IndexError):
#         test_instance.pop()
#
#
# def test_pop():
#     """Test pop method."""
#     from priorityq import PriorityQueue
#     test_instance = PriorityQueue()
#     test_instance.insert('data', 1)
#     assert test_instance.pop() == ('data')
#
#
# def test_pop_multiple():
#     """Test correct value returned from PriorityQ."""
#     from priorityq import PriorityQueue
#     test_instance = PriorityQueue()
#     test_instance.insert('data_one', 1)
#     test_instance.insert('data_two', 2)
#     test_instance.insert('data_three', 3)
#     assert test_instance.pop() == "data_one"
#
#
# def test_peek_empty():
#     """Test peek empty PriorityQ raises index error."""
#     from priorityq import PriorityQueue
#     test_instance = PriorityQueue()
#     with pytest.raises(IndexError):
#         test_instance.peek()
#
#
# def test_peek():
#     """Test peek method."""
#     from priorityq import PriorityQueue
#     test_instance = PriorityQueue()
#     test_instance.insert('data', 1)
#     assert test_instance.peek() == "data"
#
#
# def test_peek_multiple():
#     """Test correct value PriorityQ using multiple values."""
#     from priorityq import PriorityQueue
#     test_instance = PriorityQueue()
#     test_instance.insert('data_one', 1)
#     test_instance.insert('data_two', 2)
#     test_instance.insert('data_three', 3)
#     assert test_instance.peek() == "data_one"
