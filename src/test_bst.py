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


    def test_new_tree(instance):
        """Test that our tree is a tree."""
        assert isinstance(instance, BST)


    def test_new_empty_tree(empty_instance):
        """Test that an empty tree is still a tree."""
        assert all
        ([
            test.empty_instance.date is None,
            test.empty_instance.root is None,
            test.empty_instance.left is None,
            test.empty_instance.right is None
        ])


    def test_insert_many(empty_instance):
        """Test insert method with many values."""
        insertions = list(range(10))
        for root in insertions:
            test.empty_instance.insert(root)
        for root in insertions:
            assert test.empty_instance.contains(root)


    def test_contains_false(instance):
        """Test false example for contains method."""
        assert not instance.contains(1000)
