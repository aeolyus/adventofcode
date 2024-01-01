import unittest
from part1 import part1
from part2 import part2


class TestDay08(unittest.TestCase):
    def test_part1_example_1(self):
        self.assertEqual(2, part1("sample-1.txt"))

    def test_part1_example_2(self):
        self.assertEqual(6, part1("sample-2.txt"))

    def test_part1(self):
        self.assertEqual(21409, part1("input.txt"))

    def test_part2_example(self):
        self.assertEqual(6, part2("sample-3.txt"))

    def test_part2(self):
        self.assertEqual(21165830176709, part2("input.txt"))


if __name__ == '__main__':
    unittest.main()
