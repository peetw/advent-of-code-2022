import os

from advent_of_code import day_8


class TestDay8Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_8_sample.txt')
        answer = day_8.part_1(file_path)
        assert answer == 21

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_8_input.txt')
        answer = day_8.part_1(file_path)
        assert answer == 1851


class TestDay8Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_8_sample.txt')
        answer = day_8.part_2(file_path)
        assert answer == 8

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_8_input.txt')
        answer = day_8.part_2(file_path)
        assert answer == 574080
