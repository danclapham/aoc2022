import os
data_folder = os.path.dirname(__file__) + '/'
file_name = '1.txt'

f = open(data_folder + file_name)
    
max_count_1 = 0
max_count_2 = 0
max_count_3 = 0
count = 0

for line in f:
    if line == '\n':
        if count > max_count_1:
            max_count_3 = max_count_2
            max_count_2 = max_count_1
            max_count_1 = count
        elif count > max_count_2:
            max_count_3 = max_count_2
            max_count_2 = count
        elif count > max_count_3:
            max_count_3 = count
        count = 0
        continue
    
    calories = int(line)
    count += calories

print(max_count_1 + max_count_2 + max_count_3)

f.close()