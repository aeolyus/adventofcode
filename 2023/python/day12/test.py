import unittest
from part1 import part1
from part2 import part2


class TestDay12(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(21, part1("sample.txt"))

    def test_part1(self):
        self.assertEqual(7705, part1("input.txt"))

    def test_part2_example_1(self):
        self.assertEqual(1, part2("sample-2.txt"))

    def test_part2_example_2(self):
        self.assertEqual(16384, part2("sample-3.txt"))

    def test_part2_example_3(self):
        self.assertEqual(1, part2("sample-4.txt"))

    def test_part2_example_4(self):
        self.assertEqual(16, part2("sample-5.txt"))

    def test_part2_example_5(self):
        self.assertEqual(2500, part2("sample-6.txt"))

    def test_part2_example_6(self):
        self.assertEqual(506250, part2("sample-7.txt"))

    def test_part2(self):
        self.assertEqual(50338344809230, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
