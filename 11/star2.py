import time, os
import numpy as np

class Monkey:
    items = []
    op_type = ''
    op_constant = 0
    op_use_input = False
    test_constant = 1
    throw_to_if_true = 0
    throw_to_if_false = 0
    num_inspected = 0

    def __init__(self, type='', constant=0, use_input=False, t_constant=1, if_true=0, if_false=0):
        self.op_type = type
        self.op_constant = constant
        self.op_use_input = use_input
        self.test_constant = t_constant
        self.throw_to_if_true = if_true
        self.throw_to_if_false = if_false

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

def adjust_worry_level(initial, operation, constant=1, use_input=False):
    operand = initial if use_input else constant
    
    match operation:
        case '+':
            return initial + operand
        case '*':
            return int(np.multiply(initial, operand))
        case _:
            return initial

def test_item(level, constant):
    return level % constant == 0

def run_round(monkeys):
    for m in monkeys:
        num_items = len(m.items)
        if num_items == 0:
            continue

        for item in m.items:
            inspected_item = adjust_worry_level(item, m.op_type, m.op_constant, m.op_use_input)
            inspected_item %= supermod
            monkey_to_throw_to = m.throw_to_if_true if test_item(inspected_item, m.test_constant) else m.throw_to_if_false
            monkeys[monkey_to_throw_to].items.append(inspected_item)

        m.num_inspected += num_items
        m.items = []

    return monkeys

if __name__ == "__main__":
    start = time.perf_counter()
    data_folder = os.path.dirname(__file__) + '/'
    file_name = '11.txt'

    with open(data_folder + file_name) as f:
        lines = f.readlines()

        monkeys = parse_input(lines)
        num_rounds = 10_000

        supermod = 1
        for m in monkeys:
            supermod *= m.test_constant

        for i in range(num_rounds):
            monkeys = run_round(monkeys)

        for m in monkeys:
            print(m.num_inspected)

        monkeys.sort(key=lambda x: x.num_inspected, reverse=True)
        monkey_business = monkeys[0].num_inspected * monkeys[1].num_inspected
        print(monkey_business)

        print('\nCompleted in {:.5f}s'.format(time.perf_counter() - start))