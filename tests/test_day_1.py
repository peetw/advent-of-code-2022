import os

from advent_of_code import day_1


class TestDay1Part1:
    def test_returns_correct_answer_for_sample_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_1_sample.txt')
        answer = day_1.part_1(file_path)
        assert answer == 24000

    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_1_input.txt')
        answer = day_1.part_1(file_path)
        assert answer == 69177


class TestDay1Part2:
    def test_returns_correct_answer_for_input_data(self, data_dir):
        file_path = os.path.join(data_dir, 'day_1_input.txt')
        answer = day_1.part_2(file_path)
        assert answer == 207456
