import os

from advent_of_code import day_14


class TestDay14Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_14_sample.txt')
        answer = day_14.part_1(file_path)
        assert answer == 24

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_14_input.txt')
        answer = day_14.part_1(file_path)
        assert answer == 979


class TestDay14Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_14_sample.txt')
        answer = day_14.part_2(file_path)
        assert answer == 93

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_14_input.txt')
        answer = day_14.part_2(file_path)
        assert answer == 29044
