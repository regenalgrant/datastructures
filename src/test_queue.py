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

# def test_dequeue_from_empty_queue():
#     """Testing dequeue from an empty queue."""
#     test_queue = Queue()
#     with pytest.raises(AttributeError) as message:
#         test_queue.dequeue()
#     assert "IndexError: Queue is Empty" in str(message)

def test_dequeue_after_dequeue():
    """Testing dequeue on queue and test dequeue again."""
    test_queue = Queue(['w', 'e', 'r'])
    test_queue.dequeue()
    old_tail = test_queue.dequeue()
    assert old_tail == 'e'
