def connotation(strng):
    s = strng.lower().split()
    alpha = "abcdefghijklm"
    pos = 0
    neg = 0
    for i in range(len(s)):
        if s[i][0] in alpha:
            pos += 1
        else:
            neg += 1
    return True if pos >= neg else False
