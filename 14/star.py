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

def add_line_to_grid(start_coords, end_coords, grid, highest_y):
    start = Point(*start_coords.split(','))
    end = Point(*end_coords.split(','))

    if start.x != end.x: # horizontal line
        if start.y > highest_y:
            highest_y = start.y

        for x in range(min(start.x, end.x), max(start.x, end.x)+1):
            point = Point(x, start.y)
            grid[point] = 1

    if start.y != end.y: # vertical line
        max_y = max(start.y, end.y)

        for y in range(min(start.y, end.y), max_y+1):
            if max_y > highest_y:
                highest_y = max_y

            point = Point(start.x, y)
            grid[point] = 1

    return highest_y

def parse_input(lines):
    grid = {}
    highest_y = 0

    for line in lines:
        vertices = line.replace('\n', '').split(' -> ')

        for i in range(1, len(vertices)):
            highest_y = add_line_to_grid(vertices[i-1], vertices[i], grid, highest_y)

    return grid, highest_y 

def drop_sand(initial_pos, highest_y, use_floor):
    global grid

    if not use_floor and initial_pos.y > highest_y:
        return False
    else:
        if initial_pos.y == highest_y + 1:
            grid[initial_pos] = 2
            return True
        
        if Point(500, 0) in grid:
            return False

    pos = Point(initial_pos.x, initial_pos.y + 1)
    if pos not in grid:
        return drop_sand(pos, highest_y, use_floor)
    pos = Point(initial_pos.x - 1, initial_pos.y + 1)
    if pos not in grid:
        return drop_sand(pos, highest_y, use_floor)
    pos = Point(initial_pos.x + 1, initial_pos.y + 1)
    if pos not in grid:
        return drop_sand(pos, highest_y, use_floor)
    
    grid[initial_pos] = 2
    return True

def calc_sand_count(entry, highest_y, use_floor):
    count = 0

    while drop_sand(entry, highest_y, use_floor):
        count += 1
    return count

if __name__ == "__main__":
    start = time.perf_counter()
    file_name = os.path.dirname(__file__) + '/14.txt'
    use_floor = True

    with open(file_name) as f:
        lines = f.readlines()
        
        grid, highest_y = parse_input(lines)
        entry_point = Point(500, 0)

        sand_count = calc_sand_count(entry_point, highest_y, use_floor)
        print(f'\nSand units: {sand_count}')

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))