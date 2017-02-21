# _*_ encoding: utf-8 _*_
"""Tests for binary search tree."""
from bst import BST
import pytest


@pytest.fixture
def empty_instance():
    """Empty root fixture."""
    root = BST()
    return root


@pytest.fixture
def instance():
    """Full tree fixture."""
    root = BST()
    for n in range(20):
        root.insert(n)
    return root


    def test_new_root(instance):
        """Test that our root is a root."""
        assert isinstance(instance, BST)
