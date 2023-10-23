"""
The bisection method is a simple numerical technique for finding the root 
of a continuous function within a given interval.
"""


def bisection_method(func, a, b, tol, max_iterations):
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have different signs at endpoints a and b.")

    iterations = 0
    while (b - a) / 2.0 > tol and iterations < max_iterations:
        c = (a + b) / 2.0
        if func(c) == 0:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iterations += 1

    root = (a + b) / 2.0
    return root, iterations


# Example usage:
def example_function(x):
    return x**2 - 4


a = 0.0  # Lower bound of the interval
b = 3.0  # Upper bound of the interval
tolerance = 1e-6
max_iter = 100

root, iterations = bisection_method(example_function, a, b, tolerance, max_iter)
print(f"Approximate root: {root}")
print(f"Iterations: {iterations}")
