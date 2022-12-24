import time, os

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return "{x}:{y}".format(x = self.x, y = self.y)

def create_rock(x, y, type):
    match type:
        case 0:
            return [Point(x, y), Point(x+1, y), Point(x+2, y), Point(x+3, y)]
        case 1:
            return [Point(x+1, y+2), Point(x, y+1), Point(x+1, y+1), Point(x+2, y+1), Point(x+1, y)]
        case 2:
            return [Point(x+2, y+2), Point(x+2, y+1), Point(x, y), Point(x+1, y), Point(x+2, y)]
        case 3:
            return [Point(x, y+3), Point(x, y+2), Point(x, y+1), Point(x, y)]
        case _:
            return [Point(x, y+1), Point(x+1, y+1), Point(x, y), Point(x+1, y)]

def move_rock(rock_coords, x_mov, y_mov):
    return [Point(c.x+x_mov, c.y+y_mov) for c in rock_coords]

def is_rock_colliding(tower_coords, rock_coords, width):
    for coord in rock_coords:
        if coord in tower_coords:
            return True
        if coord.x < 0 or coord.x >= width or coord.y == 0:
            return True

    return False

def apply_force(tower_coords, rock_coords, width, force_dir='V'):
    if force_dir == '<':           
        moved_rock_coords = move_rock(rock_coords, -1, 0)
    elif force_dir == '>':
        moved_rock_coords = move_rock(rock_coords, 1, 0)
    else:
        moved_rock_coords = move_rock(rock_coords, 0, -1)

    return rock_coords if is_rock_colliding(tower_coords, moved_rock_coords, width) else moved_rock_coords

def find_repeats(seq):
    min_size = 5
    length = len(seq)
    repeats = []

    for runlen in range(min_size, length // 2):
        i = 0
        while i < length - runlen * 2:
            s1 = seq[i : i+runlen]
            s2 = seq[i+runlen : i+runlen*2]
            if s1 == s2:
                repeats.append((i, runlen, s1))
                i += runlen
            else:
                i += 1
    
    return repeats

def drop_rocks():
    width, height = 7, 0
    num_rocks = 1_000_000_000_000

    wind_index, rock_index = -1, 0
    tower_coords = {}

    column_heights = [0 for _ in range(width)]
    winds_when_rocks_set, repeats = [], []

    tallest_column_index, stop_index = -1, -1
    i = 0
    
    while True:
        rock_coords = create_rock(2, height + 4, rock_index)
        rock_index = (rock_index + 1) % 5

        while True:
            wind_index = (wind_index + 1) % len(wind_dirs)
            wind_dir = wind_dirs[wind_index:wind_index+1]

            blown_rock_coords = apply_force(tower_coords, rock_coords, width, wind_dir)
            rock_coords = apply_force(tower_coords, blown_rock_coords, width)

            if rock_coords == blown_rock_coords: # set rock in tower if not moving
                break

        for coord in rock_coords:
            tower_coords[coord] = 1

            if coord.y > height:
                height = coord.y

            if coord.y > column_heights[coord.x]:
                column_heights[coord.x] = coord.y

        if rock_index == 0 and len(repeats) == 0:
            winds_when_rocks_set.append(wind_index)

            repeats = find_repeats(winds_when_rocks_set)

            if len(repeats) != 0:
                cycle_length = repeats[0][1] * 5
                rocks_to_move_forward = (num_rocks - i - 1) % cycle_length
                print(f'\nFound repeats\n  i: {i}\n  Cycle length: {cycle_length}\n  Rocks to move forward: {rocks_to_move_forward}')
                stop_index = i + rocks_to_move_forward

        if i == stop_index and tallest_column_index == -1:
            tallest_column_index = column_heights.index(height)
            height_before_repeat = height

            print(f'\nMoved forward\n  i: {i}\n  Heights: {column_heights}\n  Tallest col: {tallest_column_index}\n  Rocks to move forward: {cycle_length}')
            
            stop_index += cycle_length 
        
        if i == stop_index and tallest_column_index != -1:
            cycle_height = height - height_before_repeat
            cycles_to_top = int((num_rocks - i - 1) / cycle_length)
            total_height = height + cycles_to_top * cycle_height

            print(f'\nCycled forward\n  i: {i}\n  Height: {height}\n  Cycle height: {cycle_height}\n  Cycles left: {cycles_to_top}\n\nTotal height: {total_height}')
            return
        else:
            i += 1

if __name__ == "__main__":
    start = time.perf_counter()
    file_name = os.path.dirname(__file__) + '/17.txt'

    with open(file_name) as f:
        wind_dirs = f.read().replace('\n', '')
        
        drop_rocks()

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))