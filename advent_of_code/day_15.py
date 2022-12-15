import re


def part_1(file_path: str, target_row: int) -> int:
    sensors, beacons = parse_file(file_path)

    covered = set()
    for (sx, sy), beacon_dist in sensors.items():
        target_row_dist = calc_distance(sx, sy, sx, target_row)
        if target_row_dist <= beacon_dist:
            offset = beacon_dist - target_row_dist
            for x in range(sx - offset, sx + offset + 1):
                covered.add((x, target_row))

    no_beacons = covered - beacons
    return len(no_beacons)


# Had to look up the approach for this part! :(
def part_2(file_path: str, xy_max: int) -> int:
    sensors, _ = parse_file(file_path)

    x, y = find_non_covered_point(sensors, xy_max)

    tuning_frequency = x * 4000000 + y
    return tuning_frequency


def parse_file(file_path: str) -> tuple[dict, set]:
    sensors = {}
    beacons = set()
    with open(file_path, 'r') as f:
        for line in f:
            sx, sy, bx, by = map(int, re.findall(r'(-?\d+)', line))
            beacon_dist = calc_distance(sx, sy, bx, by)
            sensors[(sx, sy)] = beacon_dist
            beacons.add((bx, by))

    return sensors, beacons


def calc_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def find_non_covered_point(sensors: dict, xy_max: int) -> tuple[int, int]:
    # y = x + a; y = -x + b
    a_coeffs, b_coeffs = set(), set()
    for (sx, sy), beacon_dist in sensors.items():
        a_coeffs.add(sy - sx + beacon_dist + 1)
        a_coeffs.add(sy - sx - beacon_dist - 1)
        b_coeffs.add(sy + sx + beacon_dist + 1)
        b_coeffs.add(sy + sx - beacon_dist - 1)

    for a in a_coeffs:
        for b in b_coeffs:
            px = (b - a) // 2
            py = (a + b) // 2
            if 0 < px < xy_max and 0 < py < xy_max:
                if all(calc_distance(sx, sy, px, py) > beacon_dist for (sx, sy), beacon_dist in sensors.items()):
                    return px, py
