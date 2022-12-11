import time, os

def run_cmd(cmd, val):
    last_reg_value = reg[-1]

    if cmd == 'noop':
        reg.append(last_reg_value)
    elif cmd == 'addx':
        reg.append(last_reg_value)
        reg.append(last_reg_value + val)

def get_signal_strength_sum(num_strengths=6, start=20, increment=40):
    sum = 0
    end = num_strengths * increment + start

    for i in range(start, end, increment):
        sum += i * reg[i-1]

    return sum

def draw_crt_pixel(cycle, width):
    if cycle % width >= reg[cycle]-1 and cycle % width <= reg[cycle]+1:
        print('#', end='')
    else:
        print('.', end='')

if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '10.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()
        reg, crt = [1], []
        width, height = 40, 6

        for line in lines:
            split_line = line.replace('\n', '').split(' ')
            cmd = split_line[0]
            val = int(split_line[1]) if len(split_line) > 1 else 0
            
            run_cmd(cmd, val)

        print(get_signal_strength_sum())

        for i in range(len(reg)-1):
            if i % width == 0:
                print('')
            draw_crt_pixel(i, width)
        
    print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))