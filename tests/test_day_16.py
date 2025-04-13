import os

from advent_of_code import day_16


class TestDay16Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_16_sample.txt')
        answer = day_16.part_1(file_path)
        assert answer == 1651

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_16_input.txt')
        answer = day_16.part_1(file_path)
        assert answer == -1


class TestDay16Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_16_sample.txt')
        answer = day_16.part_2(file_path)
        assert answer == -1

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_16_input.txt')
        answer = day_16.part_2(file_path)
        assert answer == -1
