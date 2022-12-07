import time, re, os

start = time.perf_counter()
data_folder = os.path.dirname(__file__) + '/'
file_name = '5.txt'

def get_setup_line_count(lines):
    for i, line in enumerate(lines):
        if line[0] == 'm':
            return i

def get_initial_stacks(lines):
    num_stacks = int(len(lines[0]) / 4)
    print(f'Number of stacks: {num_stacks}\n')
    
    stacks = [[] for _ in range(num_stacks)]
    empty_crate = '.'

    for line in lines:
        row = line.replace('[', '').replace(']', '').replace('\n', '').replace('    ', empty_crate).replace(' ', '')
        if row[0].isnumeric():
            break
        crates = [*row]

        for i in range(num_stacks):
            crate = crates[i]
            if crate != empty_crate:
                stacks[i].append(crate)

    for stack in stacks:
        stack = stack.reverse()
    
    print(f'Initial stacks:\n{stacks}\n')
    return stacks

def get_commands(str):
    return [int(s) for s in re.findall(r'\b\d+\b', str)]

def move_crates(lines, stacks):
    for line in lines:
        if line[0] != 'm':
            continue

        commands = get_commands(line)
        num_to_move = commands[0]
        start_stack = commands[1] - 1
        end_stack = commands[2] - 1

        print(f'Moving {num_to_move} from {start_stack} to {end_stack}')

        height = len(stacks[start_stack])
        moved_crates = stacks[start_stack][-num_to_move:]
        print(f'Moving crates: {moved_crates}')

        stacks[start_stack] = stacks[start_stack][:-num_to_move]
        for c in reversed(moved_crates):
            stacks[end_stack].append(c)

        print(f'Start crate now: {stacks[start_stack]}')
        print(f'End crate now:   {stacks[end_stack]}')
        print(' ')

    return stacks


with open(data_folder + file_name) as f:
    lines = f.readlines()
    setup_line_count = get_setup_line_count(lines)

    initial_stacks = get_initial_stacks(lines[:setup_line_count])

    end_stacks = move_crates(lines[setup_line_count:], initial_stacks)

    print(end_stacks)
    print(' ')
    for stack in end_stacks:
        print(stack[-1], end='')

    print('\n\nCompleted in {:.5f}s'.format(time.perf_counter() - start))