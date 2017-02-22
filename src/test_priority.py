"""Tests for priority queue data structure."""

import pytest

@pytest.fixture
def empty_pqueue():
    """Fixture for empty priority queue."""
    from priority_queue import Priority_Q
    empty_prio_q = Priority_Q()
    return empty_prio_q


@pytest.fixture
def populated_pqueue():
    """Fixture for full heap."""
    from priority_queue import Priority_Q
    populated_q = Priority_Q([('Queens', 1), ('Hollis', 3), ('BK', 5)])
    return populated_q


def test_cant_init_noniterable():
    """Test init doesn't work with non-iterable."""
    from priority_queue import Priority_Q
    with pytest.raises(TypeError):
        Priority_Q(8675309)


def test_init_q_exist_in_q(populated_pqueue):
    """Test initialized queue pop."""
    assert populated_pqueue._priorityq[2] == ('BK', 5)


def test_insert_negative_priority(populated_pqueue):
    """Test that a negative priority can be added to a populated queue."""
    populated_pqueue.insert(5, -1)
    assert populated_pqueue._priorityq[3] == (5, -1)


def test_insert_adds_to_existing_q(empty_pqueue):
    """Test that inserted value."""
    empty_pqueue.insert('BX', 2)
    assert empty_pqueue._priorityq[0] == ('BX', 2)


def test_cant_pop_from_empty(empty_pqueue):
    """Test that pop raises error on empty queue."""
    with pytest.raises(IndexError):
        empty_pqueue.pop()


def test_pop_from_full(populated_pqueue):
    """Test that pop full queue."""
    populated_pqueue.pop()
    assert len(populated_pqueue._priorityq) == 2


def test_pop_from_full_removes_high_priority_tuple(populated_pqueue):
    """Test that pop removes highest priority."""
    populated_pqueue.pop()
    assert ('Queens', 1) not in populated_pqueue._priorityq


def test_pop_two_items_same_priority(populated_pqueue):
    """Test that pop removes duplicated high priority."""
    populated_pqueue.insert('New York', 1)
    populated_pqueue.pop()
    assert ('Queens', 1) not in populated_pqueue._priorityq
    assert ('New Jersey', 1) in populated_pqueue._priorityq


def test_pop_negative_priority(empty_pqueue):
    """Test that pop, sorts, removes negative number."""
    empty_pqueue.insert(5, 0)
    empty_pqueue.insert(10, -1)
    empty_pqueue.pop()
    assert empty_pqueue._priorityq[0][0] == 5


def test_peek_from_empty(empty_pqueue):
    """Test can't peek at empty."""
    with pytest.raises(IndexError):
        empty_pqueue.peek()


def test_peek_from_populated_q(populated_pqueue):
    """Test peek queue."""
    assert populated_pqueue.peek() == ('Seattle', 1)


def test_peek_w_two_at_same_priority(populated_pqueue):
    """Test peek returns multiple same priority."""
    populated_pqueue.insert('New Jersey', 1)
    assert populated_pqueue.peek() == ('New York', 1)


def test_peek_returns_lowest_neg_priority(empty_pqueue):
    """Test that peek sorts, lowest number."""
    empty_pqueue.insert(5, 0)
    empty_pqueue.insert(10, -1)
    empty_pqueue.insert(8, -3)
    assert empty_pqueue.peek() == (8, -3)









    