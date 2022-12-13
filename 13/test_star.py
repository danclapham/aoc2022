from star import is_pair_in_order, is_left_number_smaller
import os

data_folder = os.path.dirname(__file__) + '/'
file_name = '13_1.txt'

def test_is_left_number_smaller():
    assert is_left_number_smaller('1', '2') == True
    assert is_left_number_smaller('9x', '2x') == False
    assert is_left_number_smaller('1x', '20') == True
    assert is_left_number_smaller('9x', '20') == True
    assert is_left_number_smaller('10', '2x') == False
    assert is_left_number_smaller('1x', '2x') == True
    assert is_left_number_smaller('10', '20') == True
    assert is_left_number_smaller('10x', '20x') == True
    assert is_left_number_smaller('10,', '1,4') == False

def test_is_pair_in_order():
    assert is_pair_in_order('', '') == True
    assert is_pair_in_order('[1,1,3,1,1]', '[1,1,5,1,1]') == True
    assert is_pair_in_order('[9]', '[[8,7,6]]') == False
    assert is_pair_in_order('[[4,4],4,4]', '[[4,4],4,4,4]') == True
    assert is_pair_in_order('[7,7,7,7]', '[7,7,7]') == False
    assert is_pair_in_order('[]', '[3]') == True
    assert is_pair_in_order('[[[]]]', '[[]]') == False
    assert is_pair_in_order('[1,[2,[3,[4,[5,6,7]]]],8,9]', '[1,[2,[3,[4,[5,6,0]]]],8,9]') == False

    assert is_pair_in_order('[[1],[2,3,4]]', '[[1],4]') == True
    assert is_pair_in_order('[[40]]', '[5]') == False
    assert is_pair_in_order('[[40]]', '[50]') == True
    assert is_pair_in_order('[[[[],9]]]', '[[[9]]]') == True
    assert is_pair_in_order('[[[[],9,7,[2,8,2,1],[6,3,7,6]],8]]','[[[[9,8,2],[10],[9,0,3],0,[3,5,0]]],[]]') == True
    assert is_pair_in_order('[[6,0,8,6],[2,5,[[10,8,6,0],6,[3,10,7]],[4,[3,9],[4,6,3]],9],[]]', '[[10,[],[[10,5,6,1,10],5,[9,1,1,8]],[[2,8,8,6,5],10,4,[5,0,2,6,1],5]]]') == True
    assert is_pair_in_order('[[10,[[7,7,9,4,9]],2,[3,8,[],[],10]],[7,[[2,4],7,0,[9]],4,[[10]]]]', '[[1,4,7,4,8],[],[8,0,7,[],[]]]') == False

if __name__ == "__main__":
    test_is_left_number_smaller()
    test_is_pair_in_order()
    
    print('\nTesting completed with 0 failures')