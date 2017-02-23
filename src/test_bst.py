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
    """Fun tree fixture."""
    fun_tree = Bst()
    insertions = [7, 6, 10, 5, 20, 11]
    for fun in insertions:
        fun_tree.insert(fun)
    return fun_tree
