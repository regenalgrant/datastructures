#  _*_coding:utf-8 _*_
"""Test heap."""

data = [1, 2, 3, 4]


def heap_init():
    """Test heap init."""
    from heap import Heap
    assert isinstance(Heap() == Heap)


def test_push():
    """Test push method."""
    from heap import Heap
    high_low = Heap()
    high_low.push(data[0])
    high_low.push(data[1])
    assert high_low.high_low[1] == data[1]
