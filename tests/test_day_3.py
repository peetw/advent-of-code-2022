import os

from advent_of_code import day_3


class TestDay3Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_3_sample.txt')
        answer = day_3.part_1(file_path)
        assert answer == 157

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_3_input.txt')
        answer = day_3.part_1(file_path)
        assert answer == 7581


class TestDay2Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_3_sample.txt')
        answer = day_3.part_2(file_path)
        assert answer == 70

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_3_input.txt')
        answer = day_3.part_2(file_path)
        assert answer == 2525
