import numpy as np


def part_1(file_path: str) -> int:
    return count_positions_visited(file_path, 2)


def part_2(file_path: str) -> int:
    return count_positions_visited(file_path, 10)


def count_positions_visited(file_path: str, num_knots: int) -> int:
    starting_position = (0, 0)
    knot_positions = [starting_position] * num_knots
    head_x, head_y = knot_positions[0]
    positions_visited = [starting_position]

    with open(file_path, 'r') as f:
        for line in f:
            direction, num_steps = line.split(' ')
            for _ in range(int(num_steps)):
                if direction == 'L':
                    head_x -= 1
                elif direction == 'R':
                    head_x += 1
                elif direction == 'U':
                    head_y += 1
                elif direction == 'D':
                    head_y -= 1
                knot_positions[0] = (head_x, head_y)

                for i in range(1, num_knots):
                    knot_positions[i] = calc_knot_position(*knot_positions[i - 1], *knot_positions[i])

                positions_visited.append(knot_positions[num_knots - 1])

    unique_positions = set(positions_visited)
    return len(unique_positions)


def calc_knot_position(head_x: int, head_y: int, tail_x: int, tail_y: int) -> tuple[int, int]:
    x_dist = head_x - tail_x
    y_dist = head_y - tail_y
    if abs(x_dist) > 1 and y_dist == 0:
        tail_x += np.sign(x_dist)
    elif x_dist == 0 and abs(y_dist) > 1:
        tail_y += np.sign(y_dist)
    elif abs(x_dist) > 1 or abs(y_dist) > 1:
        tail_x += np.sign(x_dist)
        tail_y += np.sign(y_dist)

    return tail_x, tail_y
