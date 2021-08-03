def solution(s):
    result = ''
    for i in range(len(s)):
        if s[i].islower():
            result += s[i]
        else:
            result += ' ' + s[i]
    return result