import star1
import os
from collections import defaultdict

data_folder = os.path.dirname(__file__) + '/'
file_name = '9_1.txt'

def test_add_pos_to_visited():
    visited = defaultdict(int)
    star1.visited = visited

    star1.add_pos_to_visited(star1.Position(8, 8))
    star1.add_pos_to_visited(star1.Position(1, 2))
    star1.add_pos_to_visited(star1.Position(1, 2))
    star1.add_pos_to_visited(star1.Position(2, 3))
    star1.add_pos_to_visited(star1.Position(8, 8))

    assert visited['1:2'] == 2
    assert visited['2:3'] == 1
    assert visited['8:8'] == 2

def get_pos_coords(pos):
    return (pos.x, pos.y)

def test_move():
    assert get_pos_coords(star1.move('U', star1.Position(0, 0))) == (0, 1)
    assert get_pos_coords(star1.move('D', star1.Position(3, 5))) == (3, 4)
    assert get_pos_coords(star1.move('R', star1.Position(10, 8))) == (11, 8)
    assert get_pos_coords(star1.move('L', star1.Position(-2, -4))) == (-3, -4)

def check_tail(initial_head, initial_tail, expected):
    _, tail = star1.follow(initial_head, initial_tail)
    assert get_pos_coords(tail) == expected

def test_follow():
    check_tail(star1.Position(0, 0), star1.Position(0, 0), (0, 0))
    check_tail(star1.Position(1, 0), star1.Position(0, 0), (0, 0))
    check_tail(star1.Position(-1, 0), star1.Position(0, 0), (0, 0))
    check_tail(star1.Position(0, 1), star1.Position(0, 0), (0, 0))
    check_tail(star1.Position(0, -1), star1.Position(0, 0), (0, 0))
    check_tail(star1.Position(2, 0), star1.Position(0, 0), (1, 0))
    check_tail(star1.Position(-2, 0), star1.Position(0, 0), (-1, 0))
    check_tail(star1.Position(0, 2), star1.Position(0, 0), (0, 1))
    check_tail(star1.Position(0, -2), star1.Position(0, 0), (0, -1))
    check_tail(star1.Position(1, 1), star1.Position(0, 0), (0, 0))
    check_tail(star1.Position(-1, -1), star1.Position(0, 0), (0, 0))
    check_tail(star1.Position(2, 1), star1.Position(0, 0), (1, 1))
    check_tail(star1.Position(-2, -1), star1.Position(0, 0), (-1, -1))
    check_tail(star1.Position(1, 2), star1.Position(0, 0), (1, 1))
    check_tail(star1.Position(-1, -2), star1.Position(0, 0), (-1, -1))
 
if __name__ == "__main__":
    test_add_pos_to_visited()
    test_move()
    test_follow()
    
    print('\nTesting completed with 0 failures')
