import unittest
from part1 import part1
from part2 import part2


class TestDay08(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(102, part1("sample-1.txt"))

    def test_part1(self):
        self.assertEqual(785, part1("input.txt"))

    def test_part2_example_1(self):
        self.assertEqual(94, part2("sample-1.txt"))

    def test_part2_example_2(self):
        self.assertEqual(71, part2("sample-2.txt"))

    def test_part2(self):
        self.assertEqual(922, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
