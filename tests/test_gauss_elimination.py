import unittest
from methods.gauss_elimination import gaussian_elimination


class TestGaussianElimination(unittest.TestCase):
    def test_solution(self):
        A = [[2, -1, 1, 8], [-3, 2, -2, -11], [-2, 1, 2, -3]]
        expected_solution = [5.000000000000001, 3.666666666666668, 1.6666666666666667]
        result = gaussian_elimination(A)
        for i, x in enumerate(result):
            self.assertAlmostEqual(x, expected_solution[i], places=4)

    def test_another_case(self):
        A = [[1, 1, 1, 6], [2, 3, 1, 11], [1, 2, 3, 14]]
        expected_solution = [1, 2, 3]
        result = gaussian_elimination(A)
        self.assertEqual(result, expected_solution)


if __name__ == "__main__":
    unittest.main()
