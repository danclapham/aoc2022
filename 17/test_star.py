from star import Point, move_rock
import os

file_name = os.path.dirname(__file__) + '/17_1.txt'

def test_move_rock():
    rock_coords = [Point(0,0), Point(1,3), Point(4,-2)]

    assert move_rock(rock_coords, 0, 0) == rock_coords
    assert move_rock(rock_coords, 11, 0) == [Point(11,0), Point(12,3), Point(15,-2)]
    assert move_rock(rock_coords, -3, 0) == [Point(-3,0), Point(-2,3), Point(1,-2)]
    assert move_rock(rock_coords, 0, 4) == [Point(0,4), Point(1,7), Point(4,2)]
    assert move_rock(rock_coords, 0, -123) == [Point(0,-123), Point(1,-120), Point(4,-125)]
    assert move_rock(rock_coords, 9, -6) == [Point(9,-6), Point(10,-3), Point(13,-8)]

if __name__ == "__main__":
    test_move_rock()
    
    print('\nTesting completed with 0 failures')