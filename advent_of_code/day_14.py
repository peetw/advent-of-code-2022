import numpy as np


def part_1(file_path: str) -> int:
    cave, j_start = parse_cave(file_path)

    count = 0
    i_start = 0
    while True:
        position = get_final_sand_position(cave, i_start, j_start)
        if position is None:
            break
        else:
            count += 1
            cave[position] = 2

    return count


def part_2(file_path: str) -> int:
    cave, j_start = parse_cave(file_path)

    cave = np.pad(cave, ((0, 1), (0, 0)), mode='constant', constant_values=0)
    cave = np.pad(cave, ((0, 1), (0, 0)), mode='constant', constant_values=1)

    count = 1
    first_row = get_row(cave, 0, j_start)
    first_row[2] = 2
    rows = [first_row]
    for i in range(1, cave.shape[0] - 1):
        prev_row = rows[i - 1]
        curr_row = get_row(cave, i, j_start)
        for j in range(2, i * 2 + 3):
            if curr_row[j] != 1 and 2 in prev_row[j - 2:j + 1]:
                count += 1
                curr_row[j] = 2

        rows.append(curr_row)

    return count


def parse_cave(file_path: str) -> tuple[np.ndarray, int]:
    x_min = 999
    x_max, y_max = 0, 0
    coords_list = []
    with open(file_path, 'r') as f:
        for line in f:
            coords = [(x, y) for x, y in [map(int, c.split(',')) for c in line.split(' -> ')]]
            x_coords = [c[0] for c in coords]
            y_coords = [c[1] for c in coords]
            x_min = min(x_min, min(x_coords))
            x_max = max(x_max, max(x_coords))
            y_max = max(y_max, max(y_coords))
            coords_list.append(coords)

    x_max -= x_min
    cave = np.zeros((y_max + 1, x_max + 1), int)
    for coords in coords_list:
        for idx in range(len(coords) - 1):
            x1, y1 = coords[idx]
            x2, y2 = coords[idx + 1]
            dx = x2 - x1
            dy = y2 - y1
            multi = -1 if dx < 0 or dy < 0 else 1
            i, j = (y1, x1 - x_min)
            for dj in range(abs(dx) + 1):
                cave[i, j + dj * multi] = 1
            for di in range(abs(dy) + 1):
                cave[i + di * multi, j] = 1

    j_start = 500 - x_min
    return cave, j_start


def get_final_sand_position(cave: np.ndarray, i: int, j: int) -> tuple[int, int] or None:
    if i + 1 >= cave.shape[0] or j - 1 < 0 or j + 1 >= cave.shape[1]:
        return None

    if cave[i + 1, j] == 0:
        return get_final_sand_position(cave, i + 1, j)
    if cave[i + 1, j - 1] == 0:
        return get_final_sand_position(cave, i + 1, j - 1)
    if cave[i + 1, j + 1] == 0:
        return get_final_sand_position(cave, i + 1, j + 1)

    return i, j


def get_row(cave, i, j_start):
    row_len = 5 + i * 2
    half_row_len = row_len // 2
    j_begin = j_start - half_row_len
    j_end = j_start + half_row_len + 1
    row = [0] * row_len
    row_begin = 0
    row_end = row_len
    if j_begin < 0:
        row_begin = abs(j_begin)
        j_begin = 0
    if j_end >= cave.shape[1]:
        row_end = cave.shape[1] - j_end
        j_end = cave.shape[1]
    row[row_begin:row_end] = cave[i, j_begin:j_end]
    return row
