import star
import os

data_folder = os.path.dirname(__file__) + '/'
file_name = '10_1.txt'

def get_last_two_elements(arr):
    return (arr[-2], arr[-1])

def test_run_cmd():
    reg = [1, 2, 3]
    star.reg = reg

    star.run_cmd('noop', 9)
    assert get_last_two_elements(reg) == (3, 3)
    star.run_cmd('noop', -4)
    assert get_last_two_elements(reg) == (3, 3)
    star.run_cmd('addx', 9)
    assert get_last_two_elements(reg) == (3, 12)
    star.run_cmd('addx', -4)
    assert get_last_two_elements(reg) == (12, 8)

if __name__ == "__main__":
    test_run_cmd()
    
    print('\nTesting completed with 0 failures')
