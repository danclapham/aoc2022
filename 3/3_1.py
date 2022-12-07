import os
data_folder = os.path.dirname(__file__) + '/'
file_name = '3.txt'

f = open(data_folder + file_name)

def find_repeated_char(line):
    half_length = int(len(line)/2)
    first_half_str = line[:half_length]
    second_half_str = line[half_length:]

    first_half = [*first_half_str]
    second_half = [*second_half_str]

    return list(set(first_half).intersection(second_half))[0]

def char_to_priority(char):
    ascii_value = ord(char)
    if ascii_value >= 97: # if lowercase
        return ascii_value - 96
    return ascii_value - 38

priority_sum = 0

for line in f:
    repeated_char = find_repeated_char(line)
    priority = char_to_priority(repeated_char)
    priority_sum += priority

print(priority_sum)

f.close()