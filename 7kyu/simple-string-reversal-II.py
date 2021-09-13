def solve(st,a,b):
    result = ''
    s = list(st)
    for i in range(len(s)):
        if i == a:
            result += ''.join(s[a:b+1][::-1])
        elif a < i <= b:
            pass
        else:
            result += s[i]
    return result