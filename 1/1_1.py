import os
data_folder = os.path.dirname(__file__) + '/'
file_name = '1.txt'

f = open(data_folder + file_name)
    
max_count = 0
count = 0

for line in f:
    if line == '\n':
        if count > max_count:
            max_count = count
        count = 0
        continue
    
    calories = int(line)
    count += calories

print(max_count)

f.close()