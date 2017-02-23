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
