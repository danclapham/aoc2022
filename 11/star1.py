import time, os, math

class Monkey:
    items = []
    op_type = ''
    op_constant = 0
    op_use_input = False
    test_constant = 1
    throw_to_if_true = 0
    throw_to_if_false = 0
    num_inspected = 0

def parse_input(lines):
    monkeys = []
    for line in lines:
        if len(line) < 2:
            continue

        line = line.replace('\n', '')

        if line[0] == 'M':
            monkeys.append(Monkey())
        elif line[2] == 'S':
            items = line.replace('  Starting items: ', '').split(', ')
            monkeys[-1].items = [int(item) for item in items]
        elif line[2] == 'O':
            split = line.split(' ')
            monkeys[-1].op_type = split[-2]
            if split[-1].isnumeric():
                monkeys[-1].op_constant = int(split[-1])
            else:
                monkeys[-1].op_use_input = True
        elif line[2] == 'T':
            split = line.split(' ')
            monkeys[-1].test_constant = int(split[-1])
        elif line[4] == 'I':
            split = line.split(' ')
            if line[7] == 't':
                monkeys[-1].throw_to_if_true = int(split[-1])
            else:
                monkeys[-1].throw_to_if_false = int(split[-1])

    return monkeys

def item_gets_boring(level):
    return math.floor(level / 3)

def adjust_worry_level(initial, operation, constant=1, use_input=False):
    operand = initial if use_input else constant
    
    match operation:
        case '+':
            return initial + operand
        case '*':
            return initial * operand
        case _:
            return initial

def test_item(level, constant):
    return level % constant == 0

def run_round(monkeys):
    for i, m in enumerate(monkeys):
        if len(m.items) == 0:
            continue

        for item in m.items:
            inspected_item = adjust_worry_level(item, m.op_type, m.op_constant, m.op_use_input)
            boring_item = item_gets_boring(inspected_item)
            monkey_to_throw_to = m.throw_to_if_true if test_item(boring_item, m.test_constant) else m.throw_to_if_false
            monkeys[monkey_to_throw_to].items.append(boring_item)
            m.num_inspected += 1

            # print(f'Monkey {i}:\n  Initial level: {item}\n  Inspected: {inspected_item}\n  Boring: {boring_item}\n  Throw to: monkey {monkey_to_throw_to}\n')

        m.items = []

    return monkeys


if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '11.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()

        monkeys = parse_input(lines)
        num_rounds = 20

        for _ in range(num_rounds):
            monkeys = run_round(monkeys)

        monkeys.sort(key=lambda x: x.num_inspected, reverse=True)
        monkey_business = monkeys[0].num_inspected * monkeys[1].num_inspected
        print(monkey_business)

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))