import time, os
from collections import defaultdict

class Position:
    x = 0
    y = 0
    name = ''

    def __init__(self, x=0, y=0, name=''):
        self.x = x
        self.y = y
        self.name = name

def add_pos_to_visited(pos):
    pos_str = str(pos.x) + ':' + str(pos.y)
    visited[pos_str] += 1

def move(direction, object):
    match direction:
        case 'U':
            object.y += 1
        case 'D':
            object.y -= 1
        case 'R':
            object.x += 1
        case 'L':
            object.x -= 1

    return object

def follow(head, tail):
    x_dist = head.x - tail.x
    y_dist = head.y - tail.y

    if abs(x_dist) > 1:
        if x_dist > 0:
            tail.x += 1
        else:
            tail.x -= 1

        if abs(y_dist) == 1:
            tail.y = head.y
    if abs(y_dist) > 1:
        if y_dist > 0:
            tail.y += 1
        else:
            tail.y -= 1

        if abs(x_dist) == 1:
            tail.x = head.x

    return head, tail


if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '9.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()

        visited = defaultdict(int)
        num_segments = 10

        positions = [Position(0, 0, i) for i in range(num_segments)]

        add_pos_to_visited(positions[-1])

        for line in lines:
            direction, distance = line.replace('\n', '').split(' ')
            for _ in range(int(distance)):
                positions[0] = move(direction, positions[0])
                for i in range(1, num_segments):
                    positions[i-1], positions[i] = follow(positions[i-1], positions[i])
                add_pos_to_visited(positions[-1])

        print(len(visited))

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))