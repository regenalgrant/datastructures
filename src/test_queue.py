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

def test_dequeue_from_existing_queue():
    """Testing dequeue removes tail from queue."""
    test_queue = Queue([1, 2, 3, 4])
    old_tail = test_queue.dequeue()
    assert old_tail == 1

def test_dequeue_from_empty_queue():
    """Testing dequeue from an empty queue."""
    test_queue = Queue()
    with pytest.raises(IndexError):
        test_queue.dequeue()
    assert "Queue is Empty"

def test_dequeue_after_dequeue():
    """Testing dequeue on queue and test dequeue again."""
    test_queue = Queue(['w', 'e', 'r'])
    test_queue.dequeue()
    old_tail = test_queue.dequeue()
    assert old_tail == 'e'

def test_peek_on_queue():
    """Test peek on queue."""
    test_queue = Queue([1, 2, 3, 4])
    peek_tail_data = test_queue.peek()
    assert peek_tail_data == test_queue.dll.tail.data

def test_peek_on_empty_queue():
    """Testing peek on an empty queue."""
    test_queue = Queue()
    peek_tail = test_queue.peek()
    assert peek_tail is None

def test_length_of_empty_queue():
    """Check that length of empty queue returns 0."""
    test_queue = Queue()
    assert test_queue.size() == 0

def test_queue_size():
    """Test that list initialized with data."""
    test_queue = Queue(DATA_TABLE_TEST)
    assert test_queue.size() == 2

def test_more_size():
    """Test enqueue and dequeue with data."""
    test_queue = Queue(DATA_TABLE_TEST)
    test_queue.enqueue(1)
    test_queue.enqueue(7)
    test_queue.dequeue()
    assert test_queue.size() == 3
