import numpy as np


def part_1(file_path: str) -> int:
    heights_2d = parse_file(file_path)
    visible_cols = np.apply_along_axis(find_visible, axis=0, arr=heights_2d)
    visible_rows = np.apply_along_axis(find_visible, axis=1, arr=heights_2d)

    num_visible = np.count_nonzero(visible_cols | visible_rows)

    return num_visible


def part_2(file_path: str) -> int:
    heights_2d = parse_file(file_path)
    scores = calc_scores(heights_2d)
    max_score = np.max(scores)
    return max_score


def parse_file(file_path) -> np.ndarray:
    heights = []
    with open(file_path, 'r') as f:
        for line in f:
            row_heights = list(map(int, list(line.rstrip('\n'))))
            heights.append(row_heights)
    heights_2d = np.array(heights)
    return heights_2d


def find_visible(heights_1d: np.ndarray) -> np.ndarray:
    mask = find_visible_impl(heights_1d)
    mask |= np.flipud(find_visible_impl(np.flipud(heights_1d)))
    return mask


def find_visible_impl(heights_1d: np.ndarray) -> np.ndarray:
    mask = np.zeros_like(heights_1d).astype(bool)
    max_height = -1
    for i, height in enumerate(heights_1d):
        visible = height > max_height
        mask[i] = visible
        if visible:
            max_height = height

    return mask


def calc_scores(heights_2d: np.ndarray) -> np.ndarray:
    scores = np.zeros_like(heights_2d)
    for i, j in np.ndindex(*heights_2d.shape):
        height = heights_2d[i, j]
        left = calc_score(height, heights_2d[i, :j][::-1])
        right = calc_score(height, heights_2d[i, j+1:])
        up = calc_score(height, heights_2d[:i, j][::-1])
        down = calc_score(height, heights_2d[i+1:, j])
        scores[i, j] = left * right * up * down

    return scores


def calc_score(current_height: int, heights_1d: np.ndarray) -> int:
    score = 0
    for height in heights_1d:
        score += 1
        if height >= current_height:
            break

    return score
