import unittest
from part1 import part1
from part2 import part2


class TestDay02(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(8, part1("sample.txt"))

    def test_part1(self):
        self.assertEqual(2239, part1("input.txt"))

    def test_part2_example(self):
        self.assertEqual(2286, part2("sample.txt"))

    def test_part2(self):
        self.assertEqual(83435, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
