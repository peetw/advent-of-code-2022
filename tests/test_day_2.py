import os

from advent_of_code import day_2


class TestDay2Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_2_sample.txt')
        answer = day_2.part_1(file_path)
        assert answer == 15

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_2_input.txt')
        answer = day_2.part_1(file_path)
        assert answer == 11906


class TestDay2Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_2_sample.txt')
        answer = day_2.part_2(file_path)
        assert answer == 12

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_2_input.txt')
        answer = day_2.part_2(file_path)
        assert answer == 11186
