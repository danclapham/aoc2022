import time, os

def run_cmd(cmd, val):
    last_reg_value = reg[-1]

    if cmd == 'noop':
        reg.append(last_reg_value)
    elif cmd == 'addx':
        reg.append(last_reg_value)
        reg.append(last_reg_value + val)

def generate_sprite(cycle, width):
    if cycle < 0 or cycle >= len(reg):
        return ''
    pos = reg[cycle]
    sprite = ['.' for _ in range(width)]

    for i in range(pos-1, pos+2):
        if i < 0:
            continue
        if i >= width:
            break
        sprite[i] = '#'

    return ''.join(sprite)

def draw_crt_pixel(sprite, cycle, width):
    crt.append(sprite[cycle % width])

def render_image(width, height):
    for i in range(height*width):
        if i > len(crt):
            break
        if i % width == 0:
            print('')
        print(crt[i], end='')

if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '10.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()
        reg = [1]
        crt = []
        width, height = 40, 6

        for line in lines:
            split_line = line.replace('\n', '').split(' ')
            cmd = split_line[0]
            val = int(split_line[1]) if len(split_line) > 1 else 0
            run_cmd(cmd, val)

        for i in range(len(reg)-1):
            sprite = generate_sprite(i, width)
            draw_crt_pixel(sprite, i, width)

        render_image(width, height)
        
    print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))