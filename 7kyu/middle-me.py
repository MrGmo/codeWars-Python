def middle_me(N, X, Y):
    if N % 2 != 0:
        return X
    st = Y*N
    return st[:len(st)//2] + X + st[len(st)//2:]