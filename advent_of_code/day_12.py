from collections import deque
import numpy as np


def part_1(file_path: str) -> int:
    heights_2d = parse_file(file_path)
    start = np.where(heights_2d == ord('S'))
    end = np.where(heights_2d == ord('E'))
    heights_2d[start] = ord('a')
    heights_2d[end] = ord('z')
    heights_2d = heights_2d - ord('a')

    distances = calc_distances(heights_2d, end)

    return distances[start]


def part_2(file_path: str) -> int:
    heights_2d = parse_file(file_path)
    start = np.where(heights_2d == ord('S'))
    end = np.where(heights_2d == ord('E'))
    heights_2d[start] = ord('a')
    heights_2d[end] = ord('z')
    heights_2d = heights_2d - ord('a')

    distances = calc_distances(heights_2d, end)

    start_locations = np.where(heights_2d == 0)
    min_dist = np.min(distances[start_locations])
    return min_dist


def parse_file(file_path: str) -> np.ndarray:
    heights = []
    with open(file_path, 'r') as f:
        for line in f:
            row_heights = list(map(ord, list(line.rstrip('\n'))))
            heights.append(row_heights)
    heights_2d = np.array(heights)
    return heights_2d


def calc_distances(heights_2d: np.ndarray, end: np.ndarray) -> np.ndarray:
    distances = np.full_like(heights_2d, 999999)
    distances[end] = 0

    bfs = deque()
    bfs.append((end, 0))
    while bfs:
        (i, j), distance = bfs.popleft()
        distance += 1
        height = heights_2d[i, j]
        update_distances(heights_2d, height, distances, distance, bfs, i, j - 1)
        update_distances(heights_2d, height, distances, distance, bfs, i, j + 1)
        update_distances(heights_2d, height, distances, distance, bfs, i - 1, j)
        update_distances(heights_2d, height, distances, distance, bfs, i + 1, j)

    return distances


def update_distances(heights_2d: np.ndarray, height: int, distances: np.ndarray, distance: int, bfs: deque, i: int, j: int):
    if i < 0 or i > distances.shape[0] - 1 or j < 0 or j > distances.shape[1] - 1:
        return

    height_adjacent = heights_2d[i, j]
    if height_adjacent + 1 >= height and distances[i, j] == 999999:
        distances[i, j] = distance
        bfs.append(((i, j), distance))
