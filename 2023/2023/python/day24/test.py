import unittest
from part1 import part1
from part2 import part2, gaussian_elimination


class TestDay08(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(2, part1("sample.txt", [7, 27]))

    def test_part1(self):
        self.assertEqual(12343, part1("input.txt"))

    def test_part2_example(self):
        self.assertEqual(47, part2("sample.txt"))

    def test_part2(self):
        self.assertEqual(769281292688187, part2("input.txt"))


class TestGaussianElimination(unittest.TestCase):
    def test_gaussian_elimination(self):
        A = [
            [2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2],
        ]
        b = [8, -11, -3]

        actual = gaussian_elimination(A, b)
        expected = [2, 3, -1]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
