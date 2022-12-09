import star2
from collections import defaultdict

def test_get_dir():
    assert star2.get_dir('/') == '/'
    assert star2.get_dir('/a') == 'a'
    assert star2.get_dir('/a/b') == 'b'

def test_get_smallest_dir_to_remove():
    dirs = defaultdict()
    dirs['/'] = 11111
    dirs['/a'] = 1111
    dirs['/a/b'] = 110
    dirs['/a/b/c'] = 10
    dirs['/a/d'] = 1
    dirs['/e'] = 10000

    star2.dirs = dirs

    assert star2.get_smallest_dir_to_remove(2) == 'c'
    assert star2.get_smallest_dir_to_remove(10) == 'c'
    assert star2.get_smallest_dir_to_remove(100) == 'b'
    assert star2.get_smallest_dir_to_remove(1000) == 'a'
    assert star2.get_smallest_dir_to_remove(10000) == 'e'
    assert star2.get_smallest_dir_to_remove(100000) == '/'

if __name__ == "__main__":
    test_get_dir()
    test_get_smallest_dir_to_remove()

    print('\nPassed all tests')
