def solve(st):
    s = ''.join(sorted(set(list(st))))
    if len(s) != len(st):
        return False
    for i in range(len(s)-1):
        if ord(s[i])+1 == ord(s[i+1]):
            pass
        else:
            return False
    return True