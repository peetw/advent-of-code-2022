import os

from advent_of_code import day_17


class TestDay17Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_17_sample.txt')
        answer = day_17.part_1(file_path)
        assert answer == -1

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_17_input.txt')
        answer = day_17.part_1(file_path)
        assert answer == -1


class TestDay17Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_17_sample.txt')
        answer = day_17.part_2(file_path)
        assert answer == -1

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_17_input.txt')
        answer = day_17.part_2(file_path)
        assert answer == -1
