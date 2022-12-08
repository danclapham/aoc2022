from star1 import get_parent_dir, get_full_path

def test_get_parent_dir():
    assert get_parent_dir('/a/b/c/d/e') == '/a/b/c/d'
    assert get_parent_dir('/a') == '/'
    assert get_parent_dir('/') == '/'

def test_get_full_path():
    assert get_full_path('/', 'a') == '/a'
    assert get_full_path('/a', 'b') == '/a/b'
    assert get_full_path('/a/', 'b') == '/a/b'
    assert get_full_path('/a', 'b\n') == '/a/b'


if __name__ == "__main__":
    test_get_parent_dir()
    test_get_full_path()

    print('\nPassed all tests')
