import time, os
from ast import literal_eval

def compare(left, right):
    match left, right:
        case int(), int():
            return left - right
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])
        case list(), list():
            for x in map(compare, left, right):
                if x:
                    return x
            return compare(len(left), len(right))

if __name__ == "__main__":
    start = time.perf_counter()
    file_name = os.path.dirname(__file__) + '/13.txt'

    with open(file_name) as f:
        lines = f.read().split('\n\n')
        pairs = [[*map(literal_eval, x.split())] for x in lines]

        sum_indices = sum(i for i, p in enumerate(pairs, 1) if compare(*p) < 0)

        packets = [p for pair in pairs for p in pair]

        dividers = [[[2]], [[6]]]
        first_divider = 1 + sum(1 for p in packets if compare(p, dividers[0]) < 0)
        second_divider = 2 + sum(1 for p in packets if compare(p, dividers[1]) < 0)

        print(f'\nSum: {sum_indices}\nDecoder key: {first_divider * second_divider}')

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))