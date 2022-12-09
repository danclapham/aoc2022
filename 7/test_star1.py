from star1 import get_parent_dir, get_full_path, add_child_sizes_to_parents, get_dir_sizes_under_max_size
from collections import defaultdict

def test_get_parent_dir():
    assert get_parent_dir('/a/b/c/d/e') == '/a/b/c/d'
    assert get_parent_dir('/a') == '/'
    assert get_parent_dir('/') == '/'

def test_get_full_path():
    assert get_full_path('/', 'a') == '/a'
    assert get_full_path('/a', 'b') == '/a/b'
    assert get_full_path('/a/', 'b') == '/a/b'
    assert get_full_path('/a', 'b\n') == '/a/b'

def test_add_child_sizes_to_parents():
    dirs = defaultdict()
    dirs['/'] = 0
    dirs['/a'] = 1000
    dirs['/a/b'] = 100
    dirs['/a/b/c'] = 10
    dirs['/a/d'] = 1
    dirs['/e'] = 10000

    new_dirs = add_child_sizes_to_parents(dirs)

    assert new_dirs['/'] == 11111
    assert new_dirs['/a'] == 1111
    assert new_dirs['/a/b'] == 110
    assert new_dirs['/a/b/c'] == 10
    assert new_dirs['/a/d'] == 1
    assert new_dirs['/e'] == 10000

if __name__ == "__main__":
    test_get_parent_dir()
    test_get_full_path()
    test_add_child_sizes_to_parents()

    print('\nPassed all tests')
