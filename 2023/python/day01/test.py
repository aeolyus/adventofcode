import unittest
from part1 import part1
from part2 import part2


class TestDay01(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(142, part1("sample-1.txt"))

    def test_part1(self):
        self.assertEqual(55607, part1("input.txt"))

    def test_part2_example(self):
        self.assertEqual(281, part2("sample-2.txt"))

    def test_part2(self):
        self.assertEqual(55291, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
