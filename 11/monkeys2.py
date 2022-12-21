import io

example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


class Monkey:

    def __init__(self, number, items, operation_str, divisor, case_true, case_false):
        self.number = number
        self.initial_items = items
        self.items = []
        self.operation_str = operation_str
        self.operation = make_operation(operation_str)
        self.divisor = divisor
        self.case_true = case_true
        self.case_false = case_false
        self.true_monkey = None
        self.false_monkey = None
        self.inspections = 0
        self.divisors = []

    def __repr__(self):
        return f"Monkey({self.number}, {self.items}, {self.operation_str}, {self.divisor}, {self.case_true}, {self.case_false}, {self.inspections})"

    def add_item(self, x):
        self.items.append(x)

    def initialize(self, divisors):
        self.divisors = divisors
        for x in self.initial_items:
            to_append = tuple(x % div for div in self.divisors)
            self.items.append(to_append)

    def wire(self, monkeys):
        self.true_monkey = monkeys[self.case_true]
        self.false_monkey = monkeys[self.case_false]

    def turn(self):
        self.inspections += len(self.items)
        for x in self.items:
            worries = tuple(self.operation(rem) % div for (rem, div) in zip(x, self.divisors))
            target_monkey = self.true_monkey if worries[self.number] == 0 else self.false_monkey
            target_monkey.add_item(worries)
        self.items = []
        


def make_operation(s):
    if s == "old * old":
        return lambda x: x * x
    (_, op, y) = s.split()
    if op == '+':
        other = int(y)
        return lambda x: x + other
    if op == '*':
        other = int(y)
        return lambda x: x * other
    raise ValueError(f"unrecognised operation: {s}")

def parse_monkey(f):
    line = f.readline()
    xx = line.strip()
    (_, monkey_number_str) = xx.split()
    monkey_number = int(monkey_number_str[:-1])
    line = f.readline()
    (_, items_str) = line.split(":")
    items = [int(x.strip()) for x in items_str.split(',')]
    line = f.readline()
    op_str = line.split("=")[-1].strip()
    line = f.readline()
    divisor_str = line.split("by")[-1]
    divisor = int(divisor_str.strip())
    line = f.readline()
    case_true_str = line.split()[-1]
    case_true = int(case_true_str.strip())
    line = f.readline()
    case_false_str = line.split()[-1]
    case_false = int(case_false_str.strip())
    f.readline()
    return Monkey(monkey_number, items, op_str, divisor, case_true, case_false)

def setup(sio):
    monkeys = []
    while True:
        try:
            monkeys.append(parse_monkey(sio))
        except Exception as ex:
            print(ex)
            break
    for m in monkeys:
        m.wire(monkeys)
    divisors = tuple(m.divisor for m in monkeys)
    for m in monkeys:
        m.initialize(divisors)
    return monkeys

def play(monkeys):
    for m in monkeys:
        m.turn()
    return monkeys

def task2():
    monkeys = []
    with open('input') as f:
        monkeys = setup(f)
    for _ in range(10000):
        monkeys = play(monkeys)
    result = [m.inspections for m in monkeys]
    print(result)
    result.sort()
    print(result[-1] * result[-2])