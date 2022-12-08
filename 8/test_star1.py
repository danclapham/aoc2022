from star1 import is_tree_taller, is_tree_visible, get_sides_visible
import os

data_folder = os.path.dirname(__file__) + '/'
file_name = '8_1.txt'

def test_is_tree_taller():
    assert is_tree_taller("4", 2) == True
    assert is_tree_taller("4", 5) == False
    assert is_tree_taller(4, "2") == True
    assert is_tree_taller(4, "5") == False
    assert is_tree_taller("4", "2") == True
    assert is_tree_taller("4", "5") == False
    assert is_tree_taller("4", 2) == True
    assert is_tree_taller("4", 5) == False
    assert is_tree_taller(4, "pie") == False
    assert is_tree_taller("pie", 2) == False

def test_is_tree_visible():
    assert is_tree_visible(5, [2, 5]) == False
    assert is_tree_visible(5, [1, 2]) == True
    assert is_tree_visible(5, [3]) == True
    assert is_tree_visible(5, [3, 5, 3]) == False

def test_get_sides_visible():
    with open(data_folder + file_name) as f:
        lines = f.readlines()

        assert get_sides_visible(lines, 1, 1) == 2
        assert get_sides_visible(lines, 1, 2) == 1
        assert get_sides_visible(lines, 1, 3) == 0
        assert get_sides_visible(lines, 2, 1) == 2
        assert get_sides_visible(lines, 2, 2) == 0
        assert get_sides_visible(lines, 2, 3) == 2
        assert get_sides_visible(lines, 3, 1) == 0
        assert get_sides_visible(lines, 3, 2) == 1
        assert get_sides_visible(lines, 3, 3) == 0

if __name__ == "__main__":
    test_is_tree_taller()
    test_is_tree_visible()
    test_get_sides_visible()
    
    print('Testing completed with 0 failures')
