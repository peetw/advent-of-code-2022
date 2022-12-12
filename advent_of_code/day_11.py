import math


class Monkey:
    def __init__(self, items: list[int], operation: str, modulus: int, throw_to: dict[bool, int]):
        self.num_items_inspected = 0
        self.items = items
        self.operation = eval('lambda item: ' + operation)
        self.modulus = modulus
        self.throw_to = throw_to


def part_1(file_path: str) -> int:
    monkeys = parse_file(file_path)

    def item_func(item: int):
        return item // 3

    return calc_monkey_business(monkeys, 20, item_func)


def part_2(file_path: str) -> int:
    monkeys = parse_file(file_path)
    mod_factor = math.lcm(*[m.modulus for m in monkeys])

    def item_func(item: int) -> int:
        return item % mod_factor

    return calc_monkey_business(monkeys, 10000, item_func)


def parse_file(file_path: str) -> list[Monkey]:
    monkeys = []
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    for i in range(1, len(lines), 7):
        monkey = parse_monkey_lines(lines[i:i + 6])
        monkeys.append(monkey)

    return monkeys


def calc_monkey_business(monkeys: list[Monkey], num_rounds: int, item_func):
    for r in range(num_rounds):
        for monkey in monkeys:
            while (len(monkey.items)) > 0:
                monkey.num_items_inspected += 1
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                item = item_func(item)
                monkey_idx = monkey.throw_to[item % monkey.modulus == 0]
                monkeys[monkey_idx].items.append(item)

    most_active_monkeys = sorted([m.num_items_inspected for m in monkeys])[-2:]
    monkey_business = math.prod(most_active_monkeys)
    return monkey_business


def parse_monkey_lines(lines: list[str]) -> Monkey:
    starting_items = list(map(int, lines[0][18:].split(',')))
    operation = lines[1].split('=')[-1].replace('old', 'item')
    modulus = int(lines[2].split(' ')[-1])
    throw_to = {
        True: int(lines[3].split(' ')[-1]),
        False: int(lines[4].split(' ')[-1])
    }
    return Monkey(starting_items, operation, modulus, throw_to)
