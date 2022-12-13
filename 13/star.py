import time, os, re
from functools import cmp_to_key

def get_full_number_str(str):
    return re.findall('\d+', str)[0]

def is_left_number_smaller(left, right):
    return int(get_full_number_str(left)) < int(get_full_number_str(right))

def get_number_string_length(str):
    return len(get_full_number_str(str))
    
def is_pair_in_order(left, right):
    i = 0

    while True:
        if i == len(left) and i == len(right): # end of both lists
            return True
        if i == len(left)-1 and i == len(right)-1: # end of both lists
            return True
        if i == len(left)-1 and i < len(right)-1: # left side ran out 
            return True
        if i < len(left)-1 and i == len(right)-1: # right side ran out
            return False

        left_char = left[i]
        right_char = right[i]

        if left_char == right_char and left_char.isdigit(): # same digits, skip
            if get_full_number_str(left[i:]) != get_full_number_str(right[i:]):
                return is_left_number_smaller(left[i:], right[i:])
            i += 1
            continue

        if left_char == right_char and left_char == '[': # both lists, skip
            i += 1
            continue

        if left_char != right_char:
            if left_char.isdigit() and right_char.isdigit(): # both ints, left/right side smaller
                return is_left_number_smaller(left[i:], right[i:])

            if left_char == '[':
                if right_char == ']': # right side smaller
                    return False
                length = get_number_string_length(right[i:])
                right = right[0:i] + '[' + right[i:i+length] + ']' + right[i+length:]
                continue # left only is list, convert right and skip

            if right_char == '[':
                if left_char == ']': # left side smaller
                    return True
                length = get_number_string_length(left[i:])
                left = left[0:i] + '[' + left[i:i+length] + ']' + left[i+length:]
                continue # right only is list, convert left and skip

            if left_char == ']': # left side smaller
                return True

            if right_char == ']': # right side smaller
                return False

            if left_char == ',': # left side smaller if right is digit
                return right_char.isdigit()

            if right_char == ',': # right side smaller if left is digit
                return left_char.isdigit()

        i += 1

if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '13.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()

        packets = []
        for line in lines:
            if line != '\n':
                packets.append(line.replace('\n', ''))
        sum_of_indices = 0

        for i in range(0, len(packets), 2):
            if is_pair_in_order(packets[i], packets[i+1]):
                sum_of_indices += int(i/2) + 1

        print(f'\nSum: {sum_of_indices}\n')

        divider_packets = ['[[2]]', '[[6]]']
        packets.append(divider_packets[0])
        packets.append(divider_packets[1])

        sorted_packets = sorted(packets, key=cmp_to_key(lambda x, y: -1 if is_pair_in_order(x, y) else 1))

        first_divider = sorted_packets.index(divider_packets[0]) + 1
        second_divider = sorted_packets.index(divider_packets[1]) + 1

        print(f'Decoder key: {first_divider * second_divider}')

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))