from star2 import is_tree_taller, how_many_trees_visible
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

def test_how_many_trees_visible():
    assert how_many_trees_visible(5, [2, 5]) == 2
    assert how_many_trees_visible(5, [5, 2]) == 1
    assert how_many_trees_visible(5, []) == 1
    assert how_many_trees_visible(5, [5]) == 1

if __name__ == "__main__":
    test_is_tree_taller()
    test_how_many_trees_visible()
    
    print('Testing completed with 0 failures')
