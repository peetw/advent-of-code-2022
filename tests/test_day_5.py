import os

from advent_of_code import day_5


class TestDay5Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_5_sample.txt')
        answer = day_5.part_1(file_path)
        assert answer == 'CMZ'

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_5_input.txt')
        answer = day_5.part_1(file_path)
        assert answer == 'TQRFCBSJJ'


class TestDay5Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_5_sample.txt')
        answer = day_5.part_2(file_path)
        assert answer == 'MCD'

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_5_input.txt')
        answer = day_5.part_2(file_path)
        assert answer == 'RMHFJNVFP'
