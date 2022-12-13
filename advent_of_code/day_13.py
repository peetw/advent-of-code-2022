import functools


def part_1(file_path: str) -> int:
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    indices = []
    for i in range(0, len(lines), 3):
        left = eval(lines[i])
        right = eval(lines[i + 1])
        if compare(left, right) < 0:
            indices.append(i // 3 + 1)

    sum_indices = sum(indices)
    return sum_indices


def part_2(file_path: str) -> int:
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    lines = [eval(line) for line in lines if line != '']
    lines.append([[2]])
    lines.append([[6]])
    sorted_lines = sorted(lines, key=functools.cmp_to_key(compare))

    first_index = sorted_lines.index([[2]]) + 1
    second_index = sorted_lines.index([[6]]) + 1
    decoder_key = first_index * second_index
    return decoder_key


def compare(left: list, right: list) -> int:
    comparison = 0
    i_max = max(len(left), len(right))
    for i in range(i_max):
        if i == len(left):
            return -1

        if i == len(right):
            return 1

        l = left[i]
        r = right[i]
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return -1
            elif l > r:
                return 1
            elif i == i_max - 1:
                return 0
        elif isinstance(l, list) and isinstance(r, list):
            comparison = compare(l, r)
        elif isinstance(l, int):
            comparison = compare([l], r)
        else:
            comparison = compare(l, [r])

        if comparison != 0:
            return comparison

    return comparison
