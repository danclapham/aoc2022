import star2
import os

data_folder = os.path.dirname(__file__) + '/'
file_name = '10_1.txt'

def test_generate_sprite():
    reg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    star2.reg = reg

    assert star2.generate_sprite(0, 10) == '###.......'
    assert star2.generate_sprite(1, 10) == '.###......'
    assert star2.generate_sprite(2, 10) == '..###.....'
    assert star2.generate_sprite(6, 10) == '......###.'
    assert star2.generate_sprite(7, 10) == '.......###'
    assert star2.generate_sprite(8, 10) == '........##'
    assert star2.generate_sprite(9, 10) == '.........#'
    assert star2.generate_sprite(10, 10) == '..........'
    assert star2.generate_sprite(12, 100) == ''

if __name__ == "__main__":
    test_generate_sprite()
    
    print('\nTesting completed with 0 failures')
