def change(s):
    result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    s = s.lower()
    for char in s:
        num = ord(char)-96
        if 1 <= num <= 26:
            result.insert(num-1,1)
            del result[num]
        else:
            pass
    return ''.join(map(str,result))