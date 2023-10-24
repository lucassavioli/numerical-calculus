import unittest
from methods.lagrange_interpolation import lagrange_interpolation


class TestLagrangeInterpolation(unittest.TestCase):
    def test_interpolation(self):
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        y = [2.0, 1.0, 3.0, 4.0, 2.0]

        # Test interpolation at x = 2.5
        result = lagrange_interpolation(x, y, 2.5)
        self.assertAlmostEqual(result, 1.9218, places=2)

        # Test interpolation at x = 4.5
        result = lagrange_interpolation(x, y, 4.5)
        self.assertAlmostEqual(result, 3.42188, places=2)


if __name__ == "__main__":
    unittest.main()
