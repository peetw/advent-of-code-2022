import os

from advent_of_code import day_7


class TestDay7Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_7_sample.txt')
        answer = day_7.part_1(file_path)
        assert answer == 95437

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_7_input.txt')
        answer = day_7.part_1(file_path)
        assert answer == 1141028


class TestDay7Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_7_sample.txt')
        answer = day_7.part_2(file_path)
        assert answer == 24933642

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_7_input.txt')
        answer = day_7.part_2(file_path)
        assert answer == 8278005
