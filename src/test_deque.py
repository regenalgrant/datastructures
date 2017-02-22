"""Testing Deque."""


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
    test_deque = Deque(iterable)
    assert test_deque.dll.head.data == output

# -------------------append--------------------------


def test_append_to_existing_deque():
    """Testing a value appended to the tail of the deque."""
    test_deque = Deque(TEST_DEQUE_DATA)
    test_deque.append(5)
    assert test_deque.dll.tail.data == 5


def test_append_on_empty_deque():
    """Testing append on an empty deque."""
    test_deque = Deque()
    test_deque.append(5)
    assert test_deque.dll.tail.data == 5


def test_append_after_append_on_deque():
    """Testing append after appending to deque."""
    test_deque = Deque('string')
    test_deque.append('s')
    test_deque.append('z')
    assert test_deque.dll.tail.data == ('z')


#  ----------------appendleft_child-------------------


def test_appendleft_child_to_existing_deque():
    """Testing a value added to the front of deque."""
    test_deque = Deque([1, 2, 4, 4])
    test_deque.appendleft_child([1, 2, 3, 5])
    assert test_deque.dll.head.data == ([1, 2, 3, 5])


def test_appendleft_child_to_empty_deque():
    """Testing a value added to the front of a empty deque."""
    test_deque = Deque()
    test_deque.appendleft_child([1, 2, 3, 5])
    assert test_deque.dll.head.data == ([1, 2, 3, 5])


def test_appendleft_child_after_appendleft_child_on_deque():
    """Testing appendleft_child after appending to deque."""
    test_deque = Deque()
    test_deque.appendleft_child('s')
    test_deque.appendleft_child('tring')
    assert test_deque.dll.head.data == ('tring')


#  ---------------------pop-------------------


def test_pop_from_existing_deque():
    """Testing pop method at the end of deque."""
    test_deque = Deque([1, 2, 3, 5])
    pop_value = test_deque.pop()
    assert pop_value == 1


def test_pop_from_empty_deque():
    """Testing pop method at the end of deque."""
    test_deque = Deque()
    with pytest.raises(IndexError) as message:
        test_deque.pop()
    assert "Deque is Empty" in str(message)


def test_pop_from_single_node_deque():
    """Testing pop method on single node deque."""
    test_deque = Deque([1])
    test_deque.pop()
    assert test_deque.dll.tail is None


def test_pop_after_pop():
    """Testing pop method after pop."""
    test_deque = Deque([1, 2, 3, 5])
    test_deque.pop()
    test_deque.pop()
    assert test_deque.dll.tail.data == 3


#  ---------------------popleft_child-----------------


def test_popleft_child_existing_deque():
    """Testing popleft_child method on a existing deque."""
    test_deque = Deque([1, 2, 3, 5])
    popleft_child_value = test_deque.popleft_child()
    assert popleft_child_value == 5


def test_popleft_child_empty_deque():
    """Testing popleft_child empty deque."""
    test_deque = Deque()
    with pytest.raises(IndexError) as message:
        test_deque.popleft_child()
    assert "Deque is Empty" in str(message)


def test_popleft_child_after_popleft_child_on_deque():
    """Testing popleft_child after appending to deque."""
    test_deque = Deque([1, 2, 3, 5])
    test_deque.popleft_child()
    test_deque.popleft_child()
    assert test_deque.dll.head.data == 2


#  ---------------------peek-------------------


def test_peek_on_deque():
    """Test peek on deque."""
    test_deque = Deque(TEST_DEQUE_DATA)
    peek_tail_data = test_deque.peek()
    assert peek_tail_data == test_deque.dll.tail.data


def test_peek_on_empty_deque():
    """Testing peek on an empty deque."""
    test_deque = Deque()
    peek_tail = test_deque.peek()
    assert peek_tail is None


def test_peek_existing_deque():
    """Testing peek method on a existing deque."""
    test_deque = Deque([1, 2, 3, 5])
    peek_value = test_deque.peek()
    assert peek_value == 1


# ------------------peekleft_child--------------------------


def test_peekleft_child_existing_deque():
    """Test peekleft_child on a existing deque."""
    test_deque = Deque([1, 2, 3, 5])
    peek_value = test_deque.peekleft_child()
    assert peek_value == 5


def test_peekleft_child_empty_deque():
    """Test peekleft_child on an empty deque."""
    test_deque = Deque()
    peek_value = test_deque.peekleft_child()
    assert peek_value is None


# ------------------size------------------------------


def test_length_of_empty_deque():
    """Check that length of empty deque returns 0."""
    test_deque = Deque()
    assert test_deque.size() == 0


def test_deque_size():
    """Test that size method works on existing deque."""
    test_deque = Deque([1, 2, 3, 4])
    assert test_deque.size() == 4


def test_peek_after_pop():
    """Testing peek method after pop."""
    test_deque = Deque([1, 2, 3, 5])
    test_deque.pop()
    assert test_deque.peek() == 2
