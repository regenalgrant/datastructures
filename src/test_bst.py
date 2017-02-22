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
    """Test initalizing a bst results in a bst with no root and size 0."""
    bst = BST()
    assert bst.root is None
    assert bst.size() == 0


def test_adding_to_empty_tree_adds_new_root(test_instance):
    """Test that add to an empty tree rassigns root to the new node."""
    test_instance.insert(10)
    assert test_instance.root.value == 10
    assert test_instance.size() == 1


def test_adding_value_greater_than_root_value_adds_right_child(test_instance):
    """Test that adding a value greater than the root value adds to the right child."""
    test_instance.insert(10)
    test_instance.insert(15)
    assert test_instance.root.right_child.value == 15
    assert test_instance.root.left_child is None


def test_adding_value_less_than_root_value_adds_left_child(test_instance):
    """Test that adding a value less than the root value adds to the leftchild."""
    test_instance.insert(10)
    test_instance.insert(5)
    assert test_instance.root.left_child.value == 5
    assert test_instance.root.right_child is None


def test_adding_value_equal_to_root_value_adds_nothing(test_instance):
    """Test that adding a value greater than the root value adds to the right child."""
    test_instance.insert(10)
    test_instance.insert(10)
    assert test_instance.root.right_child is None
    assert test_instance.root.left_child is None


def test_adding_values_adds_to_the_size_of_the_bst(test_instance):
    """Test that inserting adds to the size of the tree."""
    assert test_instance.size() == 0
    test_instance.insert(10)
    assert test_instance.size() == 1
    test_instance.insert(15)
    assert test_instance.size() == 2
    test_instance.insert(10)
    assert test_instance.size() == 2


def test_iterable_creates_proper_bst():
    """Test using an iterable properly fills the tree."""
    bst = BST([10, 15, 5, 3, 20])
    assert bst.root.value == 10
    assert bst.root.left_child.value == 5
    assert bst.root.left_child.left_child.value == 3
    assert bst.root.right_child.value == 15
    assert bst.root.right_child.right_child.value == 20
    assert bst.size() == 5


def test_create_bst_with_non_iterable_raises_type_error():
    """Test that initializing with a non iterable raises typeerror."""
    with pytest.raises(TypeError):
        BST(9)
