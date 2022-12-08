import time, os

def is_tree_taller(height1, height2):
    try:
        return int(height1) > int(height2)
    except ValueError:
        return False

def is_tree_visible(height, range):
    for tree in range:
        if not is_tree_taller(height, tree):
            return False
    return True

def get_sides_visible(patch, x, y):
    patch_height = len(patch)
    height = patch[y][x]
    sides_visible = 0

    column = []
    for i in range(patch_height):
        column.append(patch[i][x])

    sides_visible += 1 if is_tree_visible(height, patch[y][0:x]) else 0
    sides_visible += 1 if is_tree_visible(height, patch[y][x+1:-1]) else 0
    sides_visible += 1 if is_tree_visible(height, column[0:y]) else 0
    sides_visible += 1 if is_tree_visible(height, column[y+1:]) else 0

    return sides_visible

if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '8.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()

        lines_height = len(lines)
        lines_width = len(lines[0]) - 1 # ignore \n char

        visible_trees_count = lines_height*2 + lines_width*2 - 4

        for x in range(1, lines_width - 1):
            for y in range(1, lines_height - 1):
                sides_visible = get_sides_visible(lines, x, y)
                if sides_visible > 0:
                    visible_trees_count += 1

        print(visible_trees_count)

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))