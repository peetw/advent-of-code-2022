import os

from advent_of_code import day_13


class TestDay13Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_13_sample.txt')
        answer = day_13.part_1(file_path)
        assert answer == 13

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_13_input.txt')
        answer = day_13.part_1(file_path)
        assert answer == 6272


class TestDay13Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_13_sample.txt')
        answer = day_13.part_2(file_path)
        assert answer == 140

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_13_input.txt')
        answer = day_13.part_2(file_path)
        assert answer == 22288
