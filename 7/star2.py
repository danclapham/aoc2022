import time, os, re
from collections import defaultdict

start = time.perf_counter()
data_folder = os.path.dirname(__file__) + '/'
file_name = '7.txt'

root_dir = '/'
working_dir = root_dir
dirs = defaultdict()
dirs[root_dir] = 0

def get_parent_dir(dir):
    result = re.findall('(.*)\/.*', dir)
    if len(result) == 0 or result[0] == '':
        return '/'
    return result[0]

def get_full_path(parent_dir, dir):
    dir = dir.replace('\n', '')
    if parent_dir[-1] == '/':
        return parent_dir + dir
    return parent_dir + '/' + dir

def get_dir(full_path):
    result = re.findall('.*\/(.*)', full_path)
    if len(result) == 0 or result[0] == '':
        return '/'
    return result[0]

def parse_line(line):
    global working_dir

    if line[2:4] == 'cd':
        if line[5] == root_dir:
            working_dir = root_dir
        elif line[5:7] == '..':
            working_dir = get_parent_dir(working_dir)
        else:
            new_dir = line[5:].replace('\n', '')
            working_dir = get_full_path(working_dir, new_dir)
    elif line[2:4] == 'ls':
        pass
    elif line[0:3] == 'dir':
        dir = line[4:].replace('\n', '')
        dir_full_path = get_full_path(working_dir, dir)
        dirs[dir_full_path] = 0
    else:
        split = line.replace('\n', '').split(' ')
        size = int(split[0])
        dirs[working_dir] += size

def add_child_sizes_to_parents(dirs):
    for dir, size in dirs.items():
        while dir != root_dir:
            dir = get_parent_dir(dir)
            dirs[dir] += size
    return dirs

def get_smallest_dir_to_remove(needed_space):
    sorted_dirs = sorted(dirs.items(), key=lambda item: item[1])

    for dir, size in sorted_dirs:
        print(f'needed: {needed_space}, dir: {dir}, size: {size}')
        if size >= needed_space:
            return get_dir(dir)
    return '/'

if __name__ == "__main__":
    with open(data_folder + file_name) as f:
        lines = f.readlines()

        for line in lines:
            parse_line(line)

        dirs = add_child_sizes_to_parents(dirs)

        print(dirs[root_dir])

        total_space = 70_000_000
        needed_space = 30_000_000
        space_to_free = dirs[root_dir] - total_space + needed_space

        smallest_dir_to_remove = get_smallest_dir_to_remove(space_to_free)
        print(smallest_dir_to_remove)

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))