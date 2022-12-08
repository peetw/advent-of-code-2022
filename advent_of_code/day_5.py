import re


def part_1(file_path: str) -> str:
    num_stacks, stack_lines, instruction_lines = parse_file(file_path)
    stacks = parse_stack_lines(num_stacks, stack_lines)

    for instruction_line in instruction_lines:
        num_crates, src, dst = parse_instruction_line(instruction_line)
        for _ in range(num_crates):
            crate = stacks[src-1].pop()
            stacks[dst-1].append(crate)

    return get_top_crates(stacks)


def part_2(file_path: str) -> str:
    num_stacks, stack_lines, instruction_lines = parse_file(file_path)
    stacks = parse_stack_lines(num_stacks, stack_lines)

    for instruction_line in instruction_lines:
        num_crates, src, dst = parse_instruction_line(instruction_line)
        crates = stacks[src - 1][-num_crates:]
        stacks[dst - 1].extend(crates)
        for _ in range(num_crates):
            stacks[src - 1].pop()

    return get_top_crates(stacks)


def parse_file(file_path: str) -> tuple[int, list[str], list[str]]:
    stack_lines = []
    instruction_lines = []
    with open(file_path, 'r') as f:
        for line in f:
            if '[' in line:
                stack_lines.append(line)
            elif line.startswith(' 1'):
                num_stacks = int(line.split(' ')[-1])
            elif not line.isspace():
                instruction_lines.append(line)

    return num_stacks, stack_lines, instruction_lines


def parse_stack_lines(num_stacks: int, stack_lines: list[str]) -> list[list[str]]:
    stacks = [[] for _ in range(num_stacks)]
    for stack_line in reversed(stack_lines):
        for i in range(0, num_stacks):
            crate_index = i * 4 + 1
            if crate_index < len(stack_line):
                crate = stack_line[crate_index]
                if not crate.isspace():
                    stacks[i].append(crate)

    return stacks


def parse_instruction_line(instruction_line: str) -> tuple[int, int, int]:
    m = re.match(r'move (\d+) from (\d+) to (\d+)', instruction_line)
    num_crates, src, dst = map(int, m.groups())
    return num_crates, src, dst


def get_top_crates(stacks: list[list[str]]) -> str:
    top_crates = str.join('', [stack[-1] for stack in stacks])
    return top_crates
