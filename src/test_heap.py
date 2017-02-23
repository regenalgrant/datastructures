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


def test_get_parent():
    """Test parent method."""
    from heap import Heap
    high_low = Heap()
    high_low.high_low.append(data[0])
    high_low.high_low.append(data[1])
    high_low.high_low.append(data[2])
    assert high_low.high_low[high_low.get_parent(1)] == data[0]
    assert high_low.high_low[high_low.get_parent(2)] == data[0]


def test_get_left():
    """Test left method."""
    from heap import Heap
    high_low = Heap()
    high_low.push(data[0])
    high_low.push(data[1])
    high_low.push(data[2])
    assert high_low.high_low[high_low.get_left(0)] == data[1]


def test_get_right():
    """Test left method."""
    from heap import Heap
    high_low = Heap()
    high_low.push(data[0])
    high_low.push(data[1])
    high_low.push(data[2])
    assert high_low.high_low[high_low.get_right(0)] == data[2]


def test_compare_parent():
    """Test method."""
    from heap import Heap
    high_low = Heap()
    high_low.push(data[2])
    high_low.push(data[1])
    high_low.push(data[3])
    high_low.compare_parent(0)
    assert high_low.high_low == [data[3], data[1], data[2]]


def test_pop():
    """Test pop method."""
    from heap import Heap
    high_low = Heap()
    high_low.push(data[2])
    high_low.push(data[1])
    high_low.push(data[3])
    assert high_low.pop() == data[2]
