def sum_diagonals(matrix):
    n = len(matrix[0])
    return sum(matrix[i][i] + matrix[i][n - i - 1] for i in range(n)) if n else 0
