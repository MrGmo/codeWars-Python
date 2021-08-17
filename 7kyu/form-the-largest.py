def max_number(n):
    return int(''.join(list(map(str,sorted(list(map(int,list(str(n)))),reverse = True)))))