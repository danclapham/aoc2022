from star1 import parse_input, item_gets_boring, adjust_worry_level, test_item
import os

data_folder = os.path.dirname(__file__) + '/'
file_name = '11_1.txt'

def test_parse_input():
    with open(data_folder + file_name) as f:
        lines = f.readlines()

        monkeys = parse_input(lines)

        assert monkeys[0].items == [79, 98]
        assert monkeys[1].items == [54, 65, 75, 74]
        assert monkeys[0].op_type == '*'
        assert monkeys[1].op_type == '+'
        assert monkeys[0].op_constant == 19
        assert monkeys[2].op_constant == 0
        assert monkeys[0].op_use_input == False
        assert monkeys[2].op_use_input == True
        assert monkeys[0].test_constant == 23
        assert monkeys[1].test_constant == 19
        assert monkeys[0].throw_to_if_true == 2
        assert monkeys[1].throw_to_if_true == 2
        assert monkeys[0].throw_to_if_false == 3
        assert monkeys[1].throw_to_if_false == 0

def test_item_gets_boring():
    assert item_gets_boring(1501) == 500
    assert item_gets_boring(1862) == 620
    assert item_gets_boring(60) == 20
    assert item_gets_boring(71) == 23

def test_adjust_worry_level():
    assert adjust_worry_level(79, '*', 19, False) == 1501
    assert adjust_worry_level(54, '+', 6, False) == 60
    assert adjust_worry_level(60, '*', 1, True) == 3600

def test_test_item():
    assert test_item(500, 23) == False
    assert test_item(20, 19) == False
    assert test_item(2080, 13) == True

if __name__ == "__main__":
    test_parse_input()
    test_item_gets_boring()
    test_adjust_worry_level()
    test_test_item()
    
    print('\nTesting completed with 0 failures')
