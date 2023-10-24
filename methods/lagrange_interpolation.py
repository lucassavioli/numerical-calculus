def lagrange_interpolation(x, y, point):
    """
    Perform Lagrange polynomial interpolation to estimate the value at a given point.

    :param x: List of x-coordinates of data points.
    :param y: List of corresponding y-coordinates of data points.
    :param point: The x-coordinate where you want to estimate the y-coordinate.
    :return: The estimated y-coordinate at the given point.
    """
    n = len(x)
    result = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (point - x[j]) / (x[i] - x[j])
        result += term

    return result


# Usage example
if __name__ == "__main__":
    # Sample data points
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [2.0, 1.0, 3.0, 4.0, 2.0]

    # Point at which we want to estimate the value
    point_to_estimate = 2.5

    # Perform Lagrange interpolation to estimate the value at the given point
    estimated_value = lagrange_interpolation(x, y, point_to_estimate)

    print(f"Estimated value at x = {point_to_estimate}: {estimated_value}")
