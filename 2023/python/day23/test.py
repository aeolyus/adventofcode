import unittest
from part1 import part1
from part2 import part2


class TestDay23(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(94, part1("sample.txt"))

    def test_part1(self):
        self.assertEqual(2298, part1("input.txt"))

    def test_part2_example(self):
        self.assertEqual(154, part2("sample.txt"))

    def test_part2(self):
        self.assertEqual(6602, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
