# _*_ encoding: utf-8 _*_
"""Tests for binary search tree."""
from bst import BST
import pytest


@pytest.fixture
def empty_instance():
    """Empty root fixture."""
    root = Bst()
    return root


@pytest.fixture
def instance():
    """Full tree fixture."""
    root = BST()
    for n in range(20):
        root.insert(n)
    return root


@pytest.fixture
def instance_root():
    """Fun tree fixture."""
    root = BST()
    insertions = [7, 6, 10, 5, 20, 11]
    for root in insertions:
        root.insert(fun)
    return root


    def test_new_tree(instance):
        """Test that our tree is a tree."""
        assert isinstance(instance, BST)


    def test_new_empty_tree(empty_instance):
        """Test that an empty tree exist."""
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


    def test_balance_left(instance_root):
        """Test balance method on left-unbalanced tree."""
        test.instance_root.insert(3)
        test.instance_root.insert(2)
        assert test.instance_root.balance() == 1


    def test_balance(instance_root):
        """Test balance method on right-unbalanced tree."""
        assert test.instance_root.balance() == -1


    def test_balance_balanced(instance_root):
        """Test balance method on balanced tree."""
        test.instance_root.insert(3)
        assert test.instance_root.balance() == 0

    def test_balance_ext_right(instance):
        """Test balance method on extreme-unbalanced tree."""
        assert instance.balance() == - 19


#------------------depth---------------------


    def test_depth_empty(empty_instance):
        """Test depth method on empty tree."""
        assert empty_instance.depth() == 0


    def test_depth(instance):
        """Test depth method."""
        assert instance.depth() == 20
