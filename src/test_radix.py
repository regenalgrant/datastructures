"""Test radix sort."""
import pytest


def test_radix_sort():
    """Assert that it works."""
    from radix import radix_sort
    radix_return_val = [56, 93, 7, 11]
    assert radix_sort(radix_return_val) == [7, 11, 56, 93]
