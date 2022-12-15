import os

from advent_of_code import day_15


class TestDay15Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_15_sample.txt')
        answer = day_15.part_1(file_path, 10)
        assert answer == 26

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_15_input.txt')
        answer = day_15.part_1(file_path, 2000000)
        assert answer == 4502208


class TestDay15Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_15_sample.txt')
        answer = day_15.part_2(file_path, xy_max=20)
        assert answer == 56000011

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_15_input.txt')
        answer = day_15.part_2(file_path, xy_max=4000000)
        assert answer == 13784551204480
