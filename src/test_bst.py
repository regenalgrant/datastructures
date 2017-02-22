"""Tests for bst.py Binary Search Tree."""

import pytest
from bst import Node, BST


@pytest.fixture
def test_instance():
    """An empty binary search tree fixture."""
    bst = BST()
    return bst


@pytest.fixture
def filled_instance():
    """A filled bst."""
    bst = BST([10, 15, 5, 3, 20])
    return bst


@pytest.fixture
def left_leaning_bst(test_instance):
    """A left bst."""
    test_instance.insert(10)
    test_instance.insert(9)
    test_instance.insert(8)
    test_instance.insert(7)
    test_instance.insert(6)
    test_instance.insert(5)
    test_instance.insert(4)
    test_instance.insert(3)
    test_instance.insert(2)
    test_instance.insert(1)
    return test_instance


@pytest.fixture
def right_leaning_bst(test_instance):
    """A right  bst."""
    test_instance.insert(1)
    test_instance.insert(2)
    test_instance.insert(3)
    test_instance.insert(4)
    test_instance.insert(5)
    test_instance.insert(6)
    test_instance.insert(7)
    test_instance.insert(8)
    test_instance.insert(9)
    test_instance.insert(10)
    return test_instance


def test_empty_node_has_no_root():
    """Test that initializing a root has empoty attriubutes."""
    node = Node()
    assert node.value is None
    assert node.left_child is None
    assert node.right_child is None


def test_an_empty_bst_root_is_none():
    """Test that initalizing a bst results in a bst with no root and size 0."""
    bst = BST()
    assert bst.root is None
    assert bst.size() == 0


def test_adding_to_empty_tree_adds_new_root(test_instance):
    """Test that add to an emptyr tree rassigns root to the new node."""
    test_instance.insert(10)
    assert test_instance.root.value == 10
    assert test_instance.size() == 1


