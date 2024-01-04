import unittest
from part1 import part1
from part2 import part2


class TestDay09(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(114, part1("sample.txt"))

    def test_part1(self):
        self.assertEqual(1581679977, part1("input.txt"))

    def test_part2_example(self):
        self.assertEqual(2, part2("sample.txt"))

    def test_part2(self):
        self.assertEqual(889, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
