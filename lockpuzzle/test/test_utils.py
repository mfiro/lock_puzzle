from lockpuzzle.utils import analyse

def test_analyse():
    assert analyse("345", "456") == (0,2)
    assert analyse("555", "456") == (1,0)
    assert analyse("555", "455") == (2,0)
    assert analyse("555", "555") == (3,0)
    assert analyse("999", "123") == (0,0)

