def part_1(file_path: str) -> int:
    sum_priorities = 0
    with open(file_path, 'r') as f:
        for line in f:
            half = len(line)//2
            first_items = set(line[:half])
            second_items = set(line[half:])
            common_item_type = (first_items & second_items).pop()
            sum_priorities += get_priority(common_item_type)

    return sum_priorities


def part_2(file_path: str) -> int:
    n = 0
    sum_priorities = 0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            n += 1
            if n % 3 == 1:
                first = set(line)
            elif n % 3 == 2:
                second = set(line)
            else:
                third = set(line)
                common_item_type = (first & second & third).pop()
                sum_priorities += get_priority(common_item_type)

    return sum_priorities


def get_priority(item_type: str) -> int:
    if item_type.isupper():
        return ord(item_type) - 38
    else:
        return ord(item_type) - 96
