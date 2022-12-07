import os
data_folder = os.path.dirname(__file__) + '/'
file_name = '3.txt'

f = open(data_folder + file_name)

def find_repeated_char(line1_str, line2_str, line3_str):
    line1 = [*line1_str]
    line2 = [*line2_str]
    line3 = [*line3_str]

    char = list(set(line1).intersection(line2, line3))[0]
    return char

def char_to_priority(char):
    ascii_value = ord(char)
    if ascii_value >= 97: # if lowercase
        return ascii_value - 96
    return ascii_value - 38

priority_sum = 0
lines = f.readlines()

for i in range(0, len(lines), 3):
    repeated_char = find_repeated_char(lines[i].replace('\n',''), lines[i+1].replace('\n',''), lines[i+2].replace('\n',''))
    priority = char_to_priority(repeated_char)
    priority_sum += priority

print(priority_sum)

f.close()