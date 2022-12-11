import os
import pytest

from advent_of_code import day_9


class TestDay9Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_9_sample_a.txt')
        answer = day_9.part_1(file_path)
        assert answer == 13

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_9_input.txt')
        answer = day_9.part_1(file_path)
        assert answer == 5907


class TestDay9Part2:
    sample_data = [
        ('day_9_sample_a.txt', 1),
        ('day_9_sample_b.txt', 36)
    ]

    @pytest.mark.parametrize('file_name, expected', sample_data)
    def test_returns_correct_answer_for_sample_data(self, data_dir, file_name, expected):
        file_path = os.path.join(data_dir, file_name)
        answer = day_9.part_2(file_path)
        assert answer == expected

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_9_input.txt')
        answer = day_9.part_2(file_path)
        assert answer == 2303
