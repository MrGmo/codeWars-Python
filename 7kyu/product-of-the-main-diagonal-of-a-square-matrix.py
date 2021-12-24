def main_diagonal_product(mat):
    mult = 1
    for i in range(len(mat)):
        mult *= mat[i][i]
    return mult
