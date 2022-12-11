from star2 import adjust_worry_level, test_item
import os

data_folder = os.path.dirname(__file__) + '/'
file_name = '11_1.txt'

def test_adjust_worry_level():
    assert adjust_worry_level(79, '*', 19, False) == 1501
    assert adjust_worry_level(54, '+', 6, False) == 60
    assert adjust_worry_level(60, '*', 1, True) == 3600

def test_test_item():
    assert test_item(500, 23) == False
    assert test_item(20, 19) == False
    assert test_item(2080, 13) == True

if __name__ == "__main__":
    test_adjust_worry_level()
    test_test_item()
    
    print('\nTesting completed with 0 failures')
