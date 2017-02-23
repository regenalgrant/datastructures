# _*_ encoding: utf-8 _*_
"""Test graph.py."""
from graph  import Graph
import pytest


@pytest.fixture()
def native_graph():
    """Fixture for graph."""
    from graph import Graph
    test_graph = Graph()
    test_graph.add_node("codefellows")
    test_graph.add_node("python")
    return test_graph


@pytest.fixture()
def ample_graph():
    """Fixture that makes a full graph."""
    from graph import Graph
    ample_graph = Graph()
    ample_graph.add_edge("a", "b")
    ample_graph.add_edge("c", "d")
    ample_graph.add_edge("c", "b")
    ample_graph.add_edge("a", "d")
    ample_graph.add_edge("b", "d")
    ample_graph.add_edge("d", "a")
    print(ample_graph.graph)
    return ample_graph


@pytest.fixture()
def deep_cyclic_graph():
    """Fixture that makes a deeper graph."""
    from graph import Graph
    ample_graph = Graph()
    ample_graph.graph = {'A': {'B': 0, 'C': 0}, 'B': {'D': 0, 'E': 0},
                        'C': {'D': 0, 'E': 0}, 'D': {'E': 0}, 'E': {'A': 0}}
    return ample_graph


def test_init(native_graph):
    """Test initilization."""
    from graph import Graph
    assert isinstance(native_graph, Graph)


def test_add_node(native_graph):
    """Testing for node addition."""
    assert "python" in native_graph.nodes()


def test_nodes(native_graph):
    """Test nodes."""
    assert "codefellows" in native_graph.nodes()
    assert "python" in native_graph.nodes()


def test_add_edge():
    """Test add_edge function for nodes in empty graph."""
    from graph import Graph
    native_graph = Graph()
    native_graph.add_edge("codefellows", "python")
    assert native_graph.graph["codefellows"] == ["python"]
    assert native_graph.graph["python"] == []


# def test_edges(ample_graph):
#     """Test edges function."""
#     print(ample_graph.graph)
#     answers = [{('a', 'b'): 0},
#                {('a', 'd'): 0},
#                {('b', 'd'): 0},
#                {('c', 'b'): 0},
#                {('c', 'd'): 0},
#                {('d', 'a'): 0}]
#     for edge in ample_graph.edges():
#         answers.remove(edge)
#     assert answers == []
#
#
# def test_node_exist(ample_graph):
#     """Test node exist."""
#     assert ample_graph.has_node("a") is True
#     assert ample_graph.has_node("z") is False
#     assert ample_graph.has_node("") is False


# def test_delete_node(ample_graph):
#     """Test delete without node."""
#     ample_graph.delete_node("a")
#     assert ample_graph.graph == {'d': {}, 'c': {'d': 0, 'b': 0}, 'b': {'d': 0}}
#
#
# def test_delete_node_0(ample_graph):
#     """Test delete function when no value is passed in.."""
#     with pytest.raises(IndexError):
#         ample_graph.delete_node("")
#
#
# def test_node_deleted():
#     """Test delete function no value."""
#     from graph import Graph
#     empty_graph = Graph()
#     with pytest.raises(IndexError):
#         empty_graph.delete_node('a')
#
#
# def test_delete_edge(ample_graph):
#     """Test delete edge function."""
#     assert ample_graph.adjacent('d', 'a')
#     ample_graph.delete_edge('d', 'a')
#     assert not ample_graph.adjacent('d', 'a')
#
#
# def test_neighbors_for_brown_sugar(ample_graph):
#     """Test neighbors function."""
#     assert sorted(ample_graph.neighbors('b')) == ['a', 'c', 'd']
#
#
# def test_neighbors_1_for_brown_sugar(ample_graph):
#     """Test neighbors function."""
#     with pytest.raises(IndexError):
#         ample_graph.neighbors('z')
#
#
# def test_adjacent(ample_graph):
#     """Test adjacent function with bad values."""
#     with pytest.raises(IndexError):
#         ample_graph.adjacent('y', 'z')
#
#
# def test_adjacent_zero(ample_graph):
#     """Test adjacent function with good values."""
#     assert ample_graph.adjacent('a', 'b')
#
#
# def test_adjacent_one(ample_graph):
#     """Test adjacent function with good values."""
#     assert not ample_graph.adjacent('a', 'c')
#
#
# #--------------------weighted-----------------
#
#
# def test_depth_traversal(deep_cyclic_graph):
#     """Test depth-first traversal method on a cyclic graph."""
#     assert deep_cyclic_graph.depth_traversal('A') in [['A', 'B', 'D', 'E', 'C'],
#                                                       ['A', 'C', 'D', 'E', 'B'],
#                                                       ['A', 'C', 'E', 'D', 'B'],
#                                                       ['A', 'B', 'E', 'D', 'C']]
#
#
# def test_depth_traversal_01(native_graph):
#     """Test depth-first traversal method on a non-cyclic graph."""
#     native_graph.add_edge("codefellows", "python")
#     assert native_graph.depth_traversal('codefellows') == ['codefellows',
#                                                         'python']
#
#
# def test_depth_traversal_02():
#     """Test depth-first traversal method on an empty graph."""
#     from graph import Graph
#     empty_graph = Graph()
#     assert empty_graph.depth_traversal('A') == []
#     assert empty_graph.depth_traversal('') == []
#
#
# def test_breadth_traversal(deep_cyclic_graph):
#     """Test breadth-first traversal method on a cyclic graph."""
#     assert deep_cyclic_graph.breadth_traversal('A') in [['A', 'B', 'C', 'D', 'E'],
#                                                         ['A', 'B', 'C', 'D', 'E'],
#                                                         ['A', 'C', 'B', 'D', 'E'],
#                                                         ['A', 'C', 'B', 'E', 'D']]
#
#
# def test_breadth_traversal_01(native_graph):
#     """Test breadth-first traversal method on a non-cyclic graph."""
#     native_graph.add_edge("codefellows", "python")
#     assert native_graph.breadth_traversal('codefellows') == ['codefellows',
#                                                           'python']
#
#
# def test_breadth_traversal_02():
#     """Test depth-first traversal method on an empty graph."""
#     from graph import Graph
#     empty_graph = Graph()
#     assert empty_graph.breadth_traversal('A') == []
#     assert empty_graph.breadth_traversal('') == []
