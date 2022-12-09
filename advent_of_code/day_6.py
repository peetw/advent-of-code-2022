def part_1(stream: str) -> int:
    return decode_stream(stream, 4)


def part_2(stream: str) -> int:
    return decode_stream(stream, 14)


def decode_stream(stream: str, length: int) -> int:
    stream = stream.replace('\n', '')
    for start in range(len(stream) - length):
        end = start + length
        window = stream[start:end]
        if len(set(window)) == length:
            return end
