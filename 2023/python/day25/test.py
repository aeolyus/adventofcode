import unittest
from part1 import part1


class TestDay08(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(54, part1("sample.txt"))

    def test_part1(self):
        self.assertEqual(546804, part1("input.txt"))


if __name__ == '__main__':
    unittest.main()
