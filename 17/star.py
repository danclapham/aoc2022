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

def is_rock_colliding(tower_coords, rock_coords):
    for coord in rock_coords:
        if coord in tower_coords:
            return True
        if coord.x < 0 or coord.x >= width or coord.y == 0:
            return True

    return False

def apply_force(tower_coords, rock_coords, force_dir='V'):
    if force_dir == '<':           
        moved_rock_coords = move_rock(rock_coords, -1, 0)
    elif force_dir == '>':
        moved_rock_coords = move_rock(rock_coords, 1, 0)
    else:
        moved_rock_coords = move_rock(rock_coords, 0, -1)

    return rock_coords if is_rock_colliding(tower_coords, moved_rock_coords) else moved_rock_coords

if __name__ == "__main__":
    start = time.perf_counter()
    file_name = os.path.dirname(__file__) + '/17_1.txt'

    with open(file_name) as f:
        wind_dirs = f.read().replace('\n', '')
        width = 7
        wind_index, rock_index = -1, 0
        tower_coords = {}

        floor_height = 0
        height = 0
        column_heights = [0 for _ in range(width)]
        repeated_column_heights = [[0 for _ in range(width)]]
        repeats = []

        num_rocks = 10    
        num_rocks = 2022
        # num_rocks = 1_000_000
        # num_rocks = 1_000_000_000_000

        for i in range(num_rocks):
            # if i % 1_000_000 == 0:
            #     print(f'i: {i}\nTime: {(time.perf_counter() - start):.5f}')

            rock_coords = create_rock(2, height + 4, rock_index)
            rock_index = (rock_index + 1) % 5

            while True:
                wind_index = (wind_index + 1) % len(wind_dirs)
                wind_dir = wind_dirs[wind_index:wind_index+1]

                blown_rock_coords = apply_force(tower_coords, rock_coords, wind_dir)
                rock_coords = apply_force(tower_coords, blown_rock_coords)

                if rock_coords == blown_rock_coords: # if rock hasn't fallen, stop loop
                    break

            for coord in rock_coords:
                tower_coords[coord] = 1

                if coord.y > height:
                    height = coord.y

                if coord.y > column_heights[coord.x]:
                    column_heights[coord.x] = coord.y

            print(f'i: {i+1}\nnew_heights: {column_heights}')

            if i > 100:
                break

            # print(wind_index)

            if wind_index == 0 and i != 0:
                repeated_column_heights.append(column_heights.copy())
                repeats.append(i)
                print("Wind index 0!")
                print(f'  heights: {column_heights}')

        for i in range(1, len(repeated_column_heights)):
            print(f'\n{repeated_column_heights[i]}')
            for c in range(width):
                print(repeated_column_heights[i][c] - repeated_column_heights[i-1][c] , end=' ')
            print(f'\nRock number: {repeats[i]+1}')

        print(f'\nHighest cols: {column_heights}')
        print(f'\nHighest point: {height}')

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))