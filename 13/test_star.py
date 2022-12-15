from star import compare
import os

data_folder = os.path.dirname(__file__) + '/'
file_name = '13_1.txt'

def test_compare():
    assert compare([], []) == 0
    assert compare([1,1,3,1,1], [1,1,5,1,1]) < 0
    assert compare([9], [[8,7,6]]) > 0
    assert compare([[4,4],4,4], [[4,4],4,4,4]) < 0
    assert compare([7,7,7,7], [7,7,7]) > 0
    assert compare([], [3]) < 0
    assert compare([[[]]], [[]]) > 0
    assert compare([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]) > 0

    assert compare([[1],[2,3,4]], [[1],4]) < 0
    assert compare([[40]], [5]) > 0
    assert compare([[40]], [50]) < 0
    assert compare([[[[],9]]], [[[9]]]) < 0
    assert compare([[[[],9,7,[2,8,2,1],[6,3,7,6]],8]],[[[[9,8,2],[10],[9,0,3],0,[3,5,0]]],[]]) < 0
    assert compare([[6,0,8,6],[2,5,[[10,8,6,0],6,[3,10,7]],[4,[3,9],[4,6,3]],9],[]], [[10,[],[[10,5,6,1,10],5,[9,1,1,8]],[[2,8,8,6,5],10,4,[5,0,2,6,1],5]]]) < 0
    assert compare([[10,[[7,7,9,4,9]],2,[3,8,[],[],10]],[7,[[2,4],7,0,[9]],4,[[10]]]], [[1,4,7,4,8],[],[8,0,7,[],[]]]) > 0

if __name__ == "__main__":
    test_compare()
    
    print('\nTesting completed with 0 failures')