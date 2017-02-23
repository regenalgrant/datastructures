# _*_ encoding: utf-8 _*_
"""Test graph.py."""
import pytest


@pytest.fixture()
def new_graph():
    """Fixture for graph."""
    from graph import Graph
    test_graph = Graph()
    test_graph.add_node("codefellows")
    test_graph.add_node("python")
    return test_graph


@pytest.fixture()
def full_graph():
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


def test_init(new_graph):
    """Test initilization."""
    from graph import Graph
    assert isinstance(new_graph, Graph)


def test_add_node(new_graph):
    """Testing for node addition."""
    assert "python" in new_graph.nodes()


def test_nodes(my_graph):
    """Test nodes."""
    assert "codefellows" in new_graph.nodes()
    assert "python" in new_graph.nodes()
