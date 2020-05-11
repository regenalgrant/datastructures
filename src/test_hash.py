"""Tests for Hash Table."""
from hash import HashTable
import pytest
import io


@pytest.fixture()
def word_file():
    file = io.open('/usr/share/dict/words')
    words = file.read()
    file.close
    dic = {}
    for word in words:
        dic[word] = len(dic)


def test_get():
    """Test get method."""
    hT = HashTable()
    hT.set("test", "test")
    assert hT.get("test") == "test"


def test_set_empty():
    """Test set on empty table."""
    string = "test"
    ht = HashTable()
    check = ht._hashing(string, ht._size)
    ht.set("test", "test")
    assert ht._table[check] == [(check, "test")]
