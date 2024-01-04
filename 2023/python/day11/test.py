import unittest
from part1 import part1
from part2 import part2


class TestDay11(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(374, part1("sample.txt"))

    def test_part1(self):
        self.assertEqual(9591768, part1("input.txt"))

    def test_part2_example(self):
        self.assertEqual(1030, part2("sample.txt", 10))
        self.assertEqual(8410, part2("sample.txt", 100))

    def test_part2(self):
        self.assertEqual(746962097860, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
