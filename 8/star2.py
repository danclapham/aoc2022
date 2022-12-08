import time, os

def is_tree_taller(height1, height2):
    try:
        return int(height1) > int(height2)
    except ValueError:
        return False

def how_many_trees_visible(height, range):
    if range == []:
        return 1
    trees_visible = 0
    for tree in range:
        trees_visible += 1
        if not is_tree_taller(height, tree):
            break
    return trees_visible

def get_scenic_score(patch, x, y):
    patch_height = len(patch)
    height = patch[y][x]
    scenic_score = 1

    column = []
    for i in range(patch_height):
        column.append(patch[i][x])

    row = [*patch[y].replace('\n', '')]
    
    left = row[0:x]
    left.reverse()
    up = column[0:y]
    up.reverse()

    scenic_score *= how_many_trees_visible(height, left)
    scenic_score *= how_many_trees_visible(height, row[x+1:])
    scenic_score *= how_many_trees_visible(height, up)
    scenic_score *= how_many_trees_visible(height, column[y+1:])

    return scenic_score

if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '8.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()

        lines_height = len(lines)
        lines_width = len(lines[0]) - 1 # ignore \n char

        highest_scenic_score = 0

        for y in range(1, lines_height - 1):
            for x in range(1, lines_width - 1):
                scenic_score = get_scenic_score(lines, x, y)
                if scenic_score > highest_scenic_score:
                    highest_scenic_score = scenic_score
                
        print(highest_scenic_score)

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))