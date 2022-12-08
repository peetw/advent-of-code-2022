import os

from advent_of_code import day_4


class TestDay4Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_4_sample.txt')
        answer = day_4.part_1(file_path)
        assert answer == 2

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_4_input.txt')
        answer = day_4.part_1(file_path)
        assert answer == 588


class TestDay4Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_4_sample.txt')
        answer = day_4.part_2(file_path)
        assert answer == 4

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_4_input.txt')
        answer = day_4.part_2(file_path)
        assert answer == 911
