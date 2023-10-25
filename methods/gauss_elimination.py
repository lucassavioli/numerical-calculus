def gaussian_elimination(matrix):
    """
    Performs Gaussian elimination on a given matrix.

    Args:
        matrix (List[List[float]]): The matrix to perform Gaussian elimination on.

    Returns:
        List[float]: The solution vector obtained from back substitution.
    """
    n = len(matrix)

    for i in range(n):
        # Find the maximum element in the current column
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Swap the maximum row with the current row (partial pivoting)
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Make the diagonal element 1
        divisor = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= divisor

        # Eliminate all other rows
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    # Back substitution
    solution = [row[n] for row in matrix]

    return solution


# Example usage:
if __name__ == "__main__":
    # Example system of linear equations in matrix form (Ax = b)
    A = [[2, -1, 1, 8], [-3, 2, -2, -11], [-2, 1, 2, -3]]

    solution = gaussian_elimination(A)

    print("Solution:")
    for i, x in enumerate(solution):
        print(f"x{i + 1} = {x}")
