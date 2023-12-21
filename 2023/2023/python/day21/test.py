import unittest
from part1 import part1
from part2 import part2


class TestDay08(unittest.TestCase):
    def test_part1_example_1(self):
        self.assertEqual(16, part1("sample.txt", 6))

    def test_part1(self):
        self.assertEqual(3773, part1("input.txt"))

    def test_part2_custom_sample(self):
        self.assertEqual(64, part2("custom-sample.txt", 7))

    def test_part2(self):
        self.assertEqual(625628021226274, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
