import time, os

def parse_input(lines):
    width = len(lines[0]) - 1
    heights = []

    for line in lines:
        heights.extend(list(line.replace('\n', '')))

    start_indices = [heights.index('S')]
    start_indices.extend([i for i, x in enumerate(heights) if x == 'a'])

    return (width, start_indices, heights)

def is_path_accessible(start, end):
    if start == 'S':
        start = 'a'
    if end == 'E':
        end = 'z'
    return ord(end) - ord(start) <= 1

def get_possible_path_indices(source_index, width, heights, paths):
    possible_path_indices = []

    if source_index % width > 0:
        possible_path_indices.append(source_index - 1)
    if source_index % width <= width - 2:
        possible_path_indices.append(source_index + 1)
    if source_index - width >= 0:
        possible_path_indices.append(source_index - width)
    if source_index + width < len(heights):
        possible_path_indices.append(source_index + width)

    path_indices = []

    for i in possible_path_indices:
        if paths[i] == -1 and is_path_accessible(heights[source_index], heights[i]):
            path_indices.append(i)

    path_indices.sort()
    return path_indices

def calc_fewest_steps(width, heights, paths, min_path_length):
    path_length = 0

    while True:
        if path_length > min_path_length:
            return -1

        indices_to_calc_paths_from = [i for i, x in enumerate(paths) if x == path_length]
        path_length += 1

        for i in indices_to_calc_paths_from:
            possible_path_indices = get_possible_path_indices(i, width, heights, paths)

            for possible_path in possible_path_indices:
                paths[possible_path] = path_length
            
            if heights[i] == 'E':
                return paths[i]

if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '12.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()

        width, start_indices, heights = parse_input(lines)

        path_lengths = []
        min_path_length = 999999
        find_scenic_route = True

        for i, start_index in enumerate(start_indices):
            if not find_scenic_route and i != 0:
                break

            paths = [-1 for _ in range(len(heights))]
            paths[start_index] = 0

            path_length = calc_fewest_steps(width, heights, paths, min_path_length)
            if path_length != -1:
                min_path_length = path_length

        print(min_path_length)

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))