def part_1(file_path: str) -> int:
    cycle = 0
    x = 1
    signal_strengths = []
    with open(file_path, 'r') as f:
        for line in f:
            cycle += 1
            line_parts = line.split(' ')
            if line_parts[0] == 'addx':
                instruction = int(line_parts[1])
                check_signal_strength(cycle, signal_strengths, x)
                cycle += 1
                check_signal_strength(cycle, signal_strengths, x)
                x += instruction
            else:
                check_signal_strength(cycle, signal_strengths, x)

    signal_strengths_sum = sum(signal_strengths)
    return signal_strengths_sum


def check_signal_strength(cycle, signal_strengths, x):
    if (cycle - 20) % 40 == 0:
        signal_strength = cycle * x
        signal_strengths.append(signal_strength)


def part_2(file_path: str) -> str:
    cycle = 0
    x = 1
    pixels = ''
    with open(file_path, 'r') as f:
        for line in f:
            cycle += 1
            line_parts = line.split(' ')

            if line_parts[0] == 'addx':
                instruction = int(line_parts[1])
                pixels = update_pixels(pixels, cycle, x)
                cycle += 1
                pixels = update_pixels(pixels, cycle, x)
                x += instruction
            else:
                pixels = update_pixels(pixels, cycle, x)

    return pixels


def update_pixels(pixels: str, cycle: int, x: int) -> str:
    crt_position = (cycle - 1) % 40
    if x - 1 <= crt_position <= x + 1:
        pixels += '#'
    else:
        pixels += '.'

    if crt_position == 39:
        pixels += '\n'

    return pixels
