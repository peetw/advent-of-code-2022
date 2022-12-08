from typing import Callable


def part_1(file_path: str) -> int:
    def range_overlaps(first_lo, first_hi, second_lo, second_hi):
        return ((first_lo <= second_lo and first_hi >= second_hi) or
                (second_lo <= first_lo and second_hi >= first_hi))

    return get_num_pairs(file_path, range_overlaps)


def part_2(file_path: str) -> int:
    def range_intersects(first_lo, first_hi, second_lo, second_hi):
        return ((first_lo <= second_lo <= first_hi) or
                (second_lo <= first_lo <= second_hi))

    return get_num_pairs(file_path, range_intersects)


def get_num_pairs(file_path: str, predicate: Callable) -> int:
    num_pairs = 0
    with open(file_path, 'r') as f:
        for line in f:
            first, second = line.split(',')
            first_lo, first_hi = map(int, first.split('-'))
            second_lo, second_hi = map(int, second.split('-'))
            if predicate(first_lo, first_hi, second_lo, second_hi):
                num_pairs += 1

    return num_pairs
