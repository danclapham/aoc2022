import time, os
from treelib import Tree

start = time.perf_counter()
data_folder = os.path.dirname(__file__) + '/'
file_name = '7.txt'

root_dir = '/'
tree = Tree()
tree.create_node(root_dir, root_dir)
current_dir = root_dir

def parse_line(line):
    global current_dir

    if line[2:4] == 'cd':
        if line[5] == root_dir:
            current_dir = root_dir
        elif line[5:7] == '..':
            if current_dir != root_dir:
                current_dir = tree.parent(current_dir).identifier
        else:
            dir = line[5:].replace('\n', '')
            if not tree.contains(dir):
                tree.create_node(dir, dir, parent=current_dir, data={'type': 'dir', 'size': 0})
            current_dir = dir
    elif line[0:3] == 'dir':
        dir = line[4:].replace('\n', '')
        if not tree.contains(dir):
            tree.create_node(dir, dir, parent=current_dir, data={'type': 'dir', 'size': 0})
    elif line[2:4] != 'ls':
        split = line.replace('\n', '').split(' ')
        size = split[0]
        file = split[1]
        if not tree.contains(file):
            tree.create_node(file, file, parent=current_dir, data={'type': 'file', 'size': size})

def get_branch_size(branch):
    total_size = 0

    for b in tree.subtree(branch.identifier).all_nodes_itr():
        if b.data != None:
            size = int(b.data.get('size'))
            total_size += size
    
    return total_size

def get_dir_sizes(max_size):
    total_size = 0

    for branch in tree.all_nodes_itr():
        print(branch)
        if branch.data != None and branch.data.get('type') == 'dir':
            size = get_branch_size(branch)
            if size <= max_size:
                print(size)
                total_size += size

    return total_size


with open(data_folder + file_name) as f:
    lines = f.readlines()

    for line in lines:
        parse_line(line)

    tree.show()
    max_size = 100000

    total_size = get_dir_sizes(max_size)    

    print(total_size)

    print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))