import os

from advent_of_code import day_11


class TestDay11Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_11_sample.txt')
        answer = day_11.part_1(file_path)
        assert answer == 10605

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_11_input.txt')
        answer = day_11.part_1(file_path)
        assert answer == 61005


class TestDay11Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_11_sample.txt')
        answer = day_11.part_2(file_path)
        assert answer == 2713310158

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_11_input.txt')
        answer = day_11.part_2(file_path)
        assert answer == 20567144694
