# _*_ encoding: utf-8 _*_
"""Tests for binary search tree."""
from bst import Bst
import pytest


@pytest.fixture
def empty_instance():
    """Empty tree fixture."""
    tree = Bst()
    return tree


@pytest.fixture
def instance():
    """Full tree fixture."""
    tree = Bst()
    for n in range(20):
        tree.insert(n)
    return tree


@pytest.fixture
def instance2():
    """extra tree fixture."""
    extra_tree = Bst()
    insertions = [7, 6, 10, 5, 20, 11]
    for extra in insertions:
        extra_tree.insert(extra)
    return extra_tree


def test_new_tree(instance):
    """Test that our tree is a tree."""
    assert isinstance(instance, Bst)


def test_new_empty_tree(empty_instance):
    """Test that an empty tree is still a tree."""
    assert all([
        empty_instance.value is None,
        empty_instance.parent is None,
        empty_instance.left_child is None,
        empty_instance.right_child is None])
