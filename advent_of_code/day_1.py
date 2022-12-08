def part_1(file_path: str):
    return sum_top_n_calories(file_path, 1)


def part_2(file_path: str):
    return sum_top_n_calories(file_path, 3)


def sum_top_n_calories(file_path: str, n: int):
    sum_calories = 0
    calories = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.isspace():
                calories.append(sum_calories)
                sum_calories = 0
            else:
                sum_calories += int(line)

    sum_top_n = sum(sorted(calories)[-n:])
    return sum_top_n
