#  _*_coding:utf-8 _*_
"""Test create a heap data structure."""

data = [1, 2, 3, 4]


def heap_init():
    """Test heap init."""
    from heap import Heap
    assert isinstance(Heap() == Heap)
