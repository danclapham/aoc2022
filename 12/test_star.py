from star import is_path_accessible, get_possible_path_indices
import os

data_folder = os.path.dirname(__file__) + '/'
file_name = '12_1.txt'

def test_is_path_accessible():
    assert is_path_accessible('a', 'b') == True
    assert is_path_accessible('b', 'b') == True
    assert is_path_accessible('a', 'c') == False
    assert is_path_accessible('b', 'a') == True
    assert is_path_accessible('c', 'a') == True
    assert is_path_accessible('S', 'b') == True
    assert is_path_accessible('a', 'E') == False
    assert is_path_accessible('y', 'E') == True

def test_get_possible_path_indices():
    paths = [0, -1, -1, -1, -1, -1, -1, -1, -1]
    heights = ['S', 'b', 'd', 'b', 'b', 'd', 'c', 'd', 'e']
    width = 3

    assert get_possible_path_indices(0, width, heights, paths) == [1, 3]
    assert get_possible_path_indices(1, width, heights, paths) == [4]
    assert get_possible_path_indices(2, width, heights, paths) == [1, 5]
    assert get_possible_path_indices(4, width, heights, paths) == [1, 3]
    assert get_possible_path_indices(7, width, heights, paths) == [4, 6, 8]

if __name__ == "__main__":
    test_is_path_accessible()
    test_get_possible_path_indices()
    
    print('\nTesting completed with 0 failures')
