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


def test_edges(ample_graph):
    """Test edges function."""
    assert sorted(ample_graph.edges()) == [('a', 'b'), ('a', 'd'),
                                          ('b', 'd'), ('c', 'b'),
                                          ('c', 'd'), ('d', 'a')]


def test_node_exist(ample_graph):
    """Test node exist."""
    assert ample_graph.has_node("a") is True
    assert ample_graph.has_node("z") is False
    assert ample_graph.has_node("") is False


def test_delete_node(ample_graph):
    """Test delete without node."""
    with pytest.raises(IndexError):
        ample_graph.delete_node("")


def test_node_deleted():
    """Test delete function no value."""
    from graph import Graph
    empty_graph = Graph()
    with pytest.raises(IndexError):
        empty_graph.delete_node('a')


def test_delete_edge(ample_graph):
    """Test delete edge function."""
    ample_graph.delete_edge('d', 'a')
    assert sorted(ample_graph.edges()) == [('a', 'b'), ('a', 'd'),
                                          ('b', 'd'), ('c', 'b'),
                                          ('c', 'd')]


def test_neighbors_for_brown_sugar(ample_graph):
    """Test neighbors function."""
    assert sorted(ample_graph.neighbors('b')) == ['a', 'c', 'd']


def test_neighbors_1_for_brown_sugar(ample_graph):
    """Test neighbors function."""
    with pytest.raises(IndexError):
        ample_graph.neighbors('z')


def test_adjacent(ample_graph):
    """Test adjacent function with bad values."""
    with pytest.raises(IndexError):
        ample_graph.adjacent('y', 'z')


def test_adjacent_0(ample_graph):
    """Test adjacent function with good values."""
    assert ample_graph.adjacent('a', 'b')


def test_adjacent_1(ample_graph):
    """Test adjacent function with good values."""
    assert not ample_graph.adjacent('a', 'c')
