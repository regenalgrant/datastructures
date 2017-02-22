# _*_ encoding: utf-8 _*_
"""Tests for binary search tree."""
from bst import BST
import pytest
import random


@pytest.fixture
def empty_bst():
    """Empty root fixture."""
    root = Bst()
    return root


# @pytest.fixture
# def bst():
#     """Full tree fixture."""
#     root = BST()
#     for n in range(20):
#         root.insert(n)
#     return root
#
#
# @pytest.fixture
# def instance_root():
#     """Fun tree fixture."""
#     root = BST()
#     insertions = [7, 6, 10, 5, 20, 11]
#     for root in insertions:
#         root.insert(fun)
#     return root
#
#
#     def test_new_tree(instance):
#         """Test that our tree is a tree."""
#         assert isinstance(instance, BST)
#
#
#     def test_new_empty_tree(empty_instance):
#         """Test that an empty tree exist."""
#         assert all
#         ([
#             test.empty_instance.date is None,
#             test.empty_instance.root is None,
#             test.empty_instance.left_child is None,
#             test.empty_instance.right_child is None
#         ])
#
#
#     def test_insert_many(empty_bst):
#         """Test insert method with many values."""
#         insertions = list(range(10))
#         for root in insertions:
#             test.empty_bst.insert(root)
#         for root in insertions:
#             assert test.empty_bst.contains(root)

# --------------------contains----------------

    # def test_empty_tree_contains(empty_bst):
    #     assert not empty_bst.contains(5)
    #
    #
    # def test_contains(empty_bst):
    #     """Assert that tree contains nodes."""
    #     empty_bst.insert(4)
    #     assert empty_bst.contains(4)
    #
    #
    # def test_contains_more_nodes(empty_bst):
    #     """Assert that tree contains nodes."""
    #     empty_bst.insert(4)
    #     empty_bst.insert(2)
    #     empty_bst.insert(3)
    #     empty_bst.insert(1)
    #     assert empty_bst.contains(4)
    #     assert empty_bst.contains(2)
    #     assert empty_bst.contains(3)
    #     assert empty_bst.contains(1)
    #
    #
    # def test_contains_is_false(empty_bst):
    #     """Assert that tree does not contain nodes."""
    #     empty_bst.insert(4)
    #     empty_bst.insert(2)
    #     empty_bst.insert(3)
    #     empty_bst.insert(1)
    #     assert not empty_bst.contains(7)
    #
    #
    # def test_contains_is_false_B(empty_bst):
    #     """Assert that tree does not contain value."""
    #     empty_bst.insert(4)
    #     empty_bst.insert(7)
    #     empty_bst.insert(6)
    #     assert not empty_bst.contains(3)

    # def test_contains_false_negative(instance):
    #     """Test false example for contains method."""
    #     assert not instance.contains(1000)

    #
    # def test_balance_left_child(instance_root):
    #     """Test balance method on left_child-unbalanced tree."""
    #     test.instance_root.insert(3)
    #     test.instance_root.insert(2)
    #     assert test.instance_root.balance() == 1
    #
    #
    def test_balance(instance_bst):
        """Test balance method on right_child-unbalanced tree."""
        assert test_instance_bst.balance() == -1
    #
    #
    # def test_balance_balanced(instance_root):
    #     """Test balance method on balanced tree."""
    #     test.instance_root.insert(3)
    #     assert test.instance_root.balance() == 0
    #
    # def test_balance_right_child(instance):
    #     """Test balance method on unbalanced tree."""
    #     assert instance.balance() == - 19


#------------------depth---------------------
#
#     def test_empty_tree_depth(empty_bst):
#         assert empty_bst.depth() == 0
#
#     def test_depth(empty_bst):
#         """Assert that calling depth returns maximum depth of tree."""
#         empty_bst.insert(4)
#         assert empty_bst.depth() == 1
#         empty_bst.insert(2)
#         assert empty_bst.depth() == 2
#         empty_bst.insert(5)
#         assert empty_bst.depth() == 2
#         empty_bst.insert(6)
#         empty_bst.insert(7)
#         empty_bst.insert(8)
#         empty_bst.insert(9)
#         empty_bst.insert(3)
#         empty_bst.insert(20)
#         assert empty_bst.depth() == 4
#
#     def test_bst_fixture_depth(bst_root):
#         assert bst_root.root.value == 50
#         assert bst_root.depth() == 3
# #------------------size---------------------
#
#     def test_empty_tree_size(empty_bst):
#         assert empty_bst.size() == 0
