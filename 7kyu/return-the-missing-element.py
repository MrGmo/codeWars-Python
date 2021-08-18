def get_missing_element(seq):
    s = sorted(seq)
    for i in range(0,9):
        if s[i] != i:
            return s[i]-1
        else:
            pass
    return 9