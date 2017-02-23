"""Test radix sort."""
import pytest


def test_radix_sort():
    """Assert that it works."""
    from radix import radix_sort
    radix_return_val = [56, 93, 7, 11]
    assert radix_sort(radix_return_val) == [7, 11, 56, 93]


def test_string_in_list():
    """Assert error is raised input."""
    from radix import radix_sort
    with pytest.raises(TypeError):
        radix_sort([1, 45, 'a', 5])


def test_empty_list():
    """Assert empty list is None."""
    from radix import radix_sort
    alist = []
    radix_sort(alist)
    assert radix_sort(alist) == []


def test_same_items_in_list():
    """Assert list remains the same."""
    from radix import radix_sort
    alist = [1, 1, 1, 1]
    radix_sort(alist)
    assert radix_sort(alist) == [1, 1, 1, 1]


def test_reverse_order_list():
    """Assert reversed list on sort."""
    from radix import radix_sort
    alist = [5, 4, 3, 2, 1]
    radix_sort(alist)
    assert radix_sort(alist) == [1, 2, 3, 4, 5]
