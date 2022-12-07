import time, os

start = time.perf_counter()
data_folder = os.path.dirname(__file__) + '/'
file_name = '6.txt'

def find_num_processed(line, n):
    chars = [*line]

    for i in range(n-1, len(chars)):
        sublist = chars[i - n + 1: i + 1]
        if len(sublist) == len(set(sublist)):
            return i + 1
            
    return 0

with open(data_folder + file_name) as f:
    lines = f.readlines()
    marker_length = 4

    for line in lines:
        num_processed = find_num_processed(line, marker_length)
        print(num_processed)

    print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))