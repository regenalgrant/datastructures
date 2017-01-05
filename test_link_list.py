import pytest 
from link_list import Link_List

# TEST_INIT_DATA = [1, 2, 3, 4]

# @pytest.mark.paramatrize("data", TEST_INIT_DATA)
def test_init():
    """testing for init method of linklist."""
    test_instance = Link_List([1, 2, 3, 4])
    assert test_instance.head.data == 4

def test_push():
    """Testing push node to the link list."""
    test_instance = Link_List()
    # test_instance.push(10)
    # assert test_instance.head.data == 10
    assert test_instance.head is not None



