"""Test for Stack."""
from __future__ import unicode_literals
from stack import Stack
import pytest

TEST_INIT_DAT = [
    ([1, 2, 3], 3),
    ("run", "n"),
]

TEST_PUSH_DAT = [
    ("n", "n"),
    (4, 4),
    ("node", "node"),

]


@pytest.mark.parametrize("start, result", TEST_INIT_DAT)
def test_init(start, result):
    """Testing for init method."""
    test_instance = Stack(start)
    assert test_instance.linklist.head.data == result


def test_init_not_iterable():
    """Test for typeerror message if not iterable."""
    with pytest.raises(TypeError) as message:
        Stack(3)
    assert "data must be iterable" in str(message)


def test_int_no_data():
    """Testing that empty stack is being created."""
    test_instance = Stack()
    assert test_instance.linklist.head is None


@pytest.mark.parametrize("new_node, result", TEST_PUSH_DAT)
def test_push_empty_stack(new_node, result):
    """Testing for push method to an empty stack."""
    test_instance = Stack()
    test_instance.push(new_node)
    assert test_instance.linklist.head.data == result


@pytest.mark.parametrize("new_node, result", TEST_PUSH_DAT)
def test_push_existing_stack(new_node, result):
    """Testing for push method to an existing stack."""
    test_instance = Stack([4, 3, 2, ])
    test_instance.push(new_node)
    assert test_instance.linklist.head.data == result


def test_pop_empty_stack():
    """Testing pop method on a empty stack consisting with an error message."""
    test_instance = Stack()
    with pytest.raises(AttributeError) as message:
        test_instance.pop()
    assert "Cannot pop from empty list" in str(message)


def test_pop_existing_stack():
    """Testing for a pop method on a existing stack."""
    test_instance = Stack([5, 4, 3, ])
    assert test_instance.pop() == 3


def test_pop_after_push():
    """Testing for a pop method after push."""
    test_instance = Stack([7, 8, 9, ])
    test_instance.push([3, 4, 5, ])
    assert test_instance.pop() == [3, 4, 5, ]
