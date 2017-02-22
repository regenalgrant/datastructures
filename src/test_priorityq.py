# -*- coding: utf-8 -*-
"""Prioityq tests."""
import pytest


def test_insert():
    """Test insert method."""
    from priorityq import PriorityQueue
    test_instance = PriorityQueue()
    test_instance.insert('data', 1)
    assert test_instance.dict[1] == ['data']
