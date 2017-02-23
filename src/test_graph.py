# _*_ encoding: utf-8 _*_
"""Test graph.py."""
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
