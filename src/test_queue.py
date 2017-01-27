# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from queue import Queue


DATA_TABLE_TEST = [
    ([1, 2, 3, 4], 4),
    ("elephant", "t")
    ]


@pytest.mark.parametrize("iterable, output", DATA_TABLE_TEST)
def test_queue_init(iterable, output):
    """Test for initialize queue."""
    test_queue = Queue(iterable)
    assert test_queue.dll.head.data == output

@pytest.mark.parametrize("iterable, output", DATA_TABLE_TEST)
def test_enqueue_on_extisting_queue(iterable, output):
    """Testing enqueue on extisting queue."""
    test_queue = Queue(iterable)
    test_queue.enqueue(9)
    assert test_queue.dll.head.data == 9

def test_enqueue_on_empty_queue():
    """Testing enqueue on empty queue."""
    test_queue = Queue()
    test_queue.enqueue(9)
    assert test_queue.dll.head.data == 9

def test_enqueue_after_enqueue():
    """Testing enqueue after ennqueue nodes to queue."""
    test_queue = Queue()
    test_queue.enqueue(9)
    test_queue.enqueue(8)
    assert test_queue.dll.head.data ==  8
