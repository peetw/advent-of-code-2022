import os

from advent_of_code import day_18


class TestDay18Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_18_sample.txt')
        answer = day_18.part_1(file_path)
        assert answer == -1

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_18_input.txt')
        answer = day_18.part_1(file_path)
        assert answer == -1


class TestDay18Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_18_sample.txt')
        answer = day_18.part_2(file_path)
        assert answer == -1

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_18_input.txt')
        answer = day_18.part_2(file_path)
        assert answer == -1
