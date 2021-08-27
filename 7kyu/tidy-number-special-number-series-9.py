def tidyNumber(n):
    n = list(map(int,list(str(n))))
    for i in range(len(n)-1):
        if n[i] <= n[i+1]:
            pass
        else:
            return False
    return True