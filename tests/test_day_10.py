import os

from advent_of_code import day_10


class TestDay10Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_10_sample.txt')
        answer = day_10.part_1(file_path)
        assert answer == 13140

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_10_input.txt')
        answer = day_10.part_1(file_path)
        assert answer == 14420


class TestDay10Part2:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        expected = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
        file_path = os.path.join(data_dir, 'day_10_sample.txt')
        answer = day_10.part_2(file_path)
        assert answer == expected

    def test_returns_correct_answer_for_input_data(self, data_dir):
        expected = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
        file_path = os.path.join(data_dir, 'day_10_input.txt')
        answer = day_10.part_2(file_path)
        assert answer == expected
