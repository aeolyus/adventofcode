import unittest
from part1 import part1
from part2 import part2


class TestDay08(unittest.TestCase):
    def test_part1_example_1(self):
        self.assertEqual(4, part1("sample-1.txt"))

    def test_part1_example_2(self):
        self.assertEqual(4, part1("sample-2.txt"))

    def test_part1_example_3(self):
        self.assertEqual(8, part1("sample-3.txt"))

    def test_part1(self):
        self.assertEqual(6890, part1("input.txt"))

    def test_part2_example_1(self):
        self.assertEqual(4, part2("sample-4.txt"))

    def test_part2_example_2(self):
        self.assertEqual(8, part2("sample-5.txt"))

    def test_part2_example_3(self):
        self.assertEqual(10, part2("sample-6.txt"))

    def test_part2(self):
        self.assertEqual(453, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
