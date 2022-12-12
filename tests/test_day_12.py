import os

from advent_of_code import day_12


class TestDay12Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_12_sample.txt')
        answer = day_12.part_1(file_path)
        assert answer == 31

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_12_input.txt')
        answer = day_12.part_1(file_path)
        assert answer == 534


class TestDay12Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_12_sample.txt')
        answer = day_12.part_2(file_path)
        assert answer == 29

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_12_input.txt')
        answer = day_12.part_2(file_path)
        assert answer == 525
