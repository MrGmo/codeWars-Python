def max_redigit(num): 
    if num < 0 or len(str(num)) != 3:
        return None
    n = sorted(list(map(int,list(str(num)))),reverse = True)
    return int(''.join(map(str,n)))