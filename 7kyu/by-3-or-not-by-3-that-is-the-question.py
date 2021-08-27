def divisible_by_three(st):
    s = sum(list(map(int,list(st))))
    while s >= 0:
        s -= 3
        if s == 0:
            return True
    return False