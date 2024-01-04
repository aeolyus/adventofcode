import unittest
from part1 import part1
from part2 import part2


class TestDay19(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(19114, part1("sample.txt"))

    def test_part1(self):
        self.assertEqual(398527, part1("input.txt"))

    def test_part2_example(self):
        self.assertEqual(167409079868000, part2("sample.txt"))

    def test_part2(self):
        self.assertEqual(133973513090020, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
