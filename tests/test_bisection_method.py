import unittest
from methods.bisection_method import bisection_method


class TestBisectionMethod(unittest.TestCase):
    def test_bisection(self):
        # Test the bisection method with the example function
        a = 0.0
        b = 3.0
        tolerance = 1e-6
        max_iter = 100
        example_function = lambda x: x**2 - 4

        root, iterations = bisection_method(example_function, a, b, tolerance, max_iter)
        expected_root = 2.0  # The expected root of x^2 - 4 within [0, 3]

        self.assertAlmostEqual(
            root,
            expected_root,
            places=6,
            msg=f"Root is not approximately {expected_root}",
        )
        self.assertLess(
            iterations, max_iter, msg=f"Exceeded the maximum number of iterations"
        )


if __name__ == "__main__":
    unittest.main()
