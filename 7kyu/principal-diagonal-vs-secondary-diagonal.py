def diagonal(matrix):
    prin = 0
    second = 0
    for i in range(len(matrix)):
        prin += matrix[i][i]
        second += matrix[::-1][i][i]
    if prin > second:
        return "Principal Diagonal win!"
    if prin < second:
        return "Secondary Diagonal win!"
    return "Draw!"
